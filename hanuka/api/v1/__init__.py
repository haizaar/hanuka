from fastapi import APIRouter

from . import candles


router = APIRouter()
router.include_router(candles.router, prefix="/candles", tags=["candles"])
