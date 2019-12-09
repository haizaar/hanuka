import asyncio
import logging
from contextlib import AsyncExitStack

import click
import structlog
import uberlogging
import uvicorn
from fastapi import FastAPI

from .settings import Settings
from . import api
from . import bindings as b

logger = structlog.get_logger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        title="hanuka",
    )
    app.include_router(api.router, prefix="/api")
    return app


def create_server(app: FastAPI, s: Settings) -> uvicorn.Server:
    config = uvicorn.Config(app,
                            port=s.server.port,
                            log_config=None)
    config.load()
    return uvicorn.Server(config=config)


async def _main(s: Settings) -> None:
    async with AsyncExitStack() as estack:
        await b.bind(s, estack)
        app = create_app()
        server = create_server(app, s)

        logger.info("Starting...", port=s.server.port)
        await server.serve()


@click.command("hanuka")
@click.option("-v", "--verbose", is_flag=True, show_default=True,
              help="Switch root logger to DEBUG")
def main(verbose: bool):
    """
    Light the given amount of candles
    """
    settings = Settings()
    root_level = logging.DEBUG if verbose else logging.INFO
    uberlogging.configure(root_level=root_level)

    asyncio.run(_main(settings))
