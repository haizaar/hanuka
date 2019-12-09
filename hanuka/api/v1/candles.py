from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException

from ...models.candle import Candle
from ... import bindings as b

router = APIRouter()


@router.get(
    "",
    summary="List candle status",
    response_model=List[Candle],
)
async def list():
    return await b.svc.candle_db.list()


@router.post(
    "/{candle_id}/_light",
    summary="Light the candle by ID",
    response_model=Candle,
)
async def light(candle_id: int):
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
    candle.id = candle_id
    return await b.svc.candle_db.add(candle)
