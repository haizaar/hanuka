from contextlib import AsyncExitStack
from dataclasses import dataclass

from .candle_db import CandleDb
from .settings import Settings

settings: Settings = None


@dataclass
class Services:
    candle_db: CandleDb


svc: Services = None


async def bind(s: Settings, estack: AsyncExitStack) -> None:
    global settings, svc

    candle_db = await estack.enter_async_context(CandleDb())

    settings = s

    svc = Services(
        candle_db=candle_db,
    )
