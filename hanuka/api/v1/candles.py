from http import HTTPStatus
from typing import List

import structlog
from fastapi import APIRouter, HTTPException

from ...models.candle import Candle
from ... import bindings as b

router = APIRouter()
logger = structlog.get_logger(__name__)


@router.get(
    "",
    summary="List candle status",
    response_model=List[Candle],
)
async def list():
    logger.info("Listing handles")
    return await b.svc.candle_db.list()


@router.post(
    "/{candle_id}/_light",
    summary="Light the candle by ID",
    response_model=Candle,
)
async def light(candle_id: int):
    logger.info("Lighting the candle", candle_id=candle_id)
    if not (await b.svc.candle_db.exists(candle_id)):
        raise HTTPException(
            HTTPStatus.NOT_FOUND.value,
            detail="No such candle, darling"
        )

    return await b.svc.candle_db.light(candle_id)


@router.put(
    "/{candle_id}",
    summary="Create candle by ID",
    response_model=Candle,
)
async def create_by_id(candle_id: int, candle: Candle):
    logger.info("Creating candle", candle_id=candle_id)
    candle.id = candle_id
    return await b.svc.candle_db.add(candle)
