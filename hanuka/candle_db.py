from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

import structlog

from .models.candle import Candle

logger = structlog.get_logger(__name__)


@dataclass
class CandleDb:
    host: str = "localhost"
    port: int = 3134

    candles: Dict[int, Candle] = field(init=False)

    def __post_init__(self) -> None:
        self.candles = {
            1: Candle(id=1),
            2: Candle(id=2),
            3: Candle(id=3),
        }

    async def list(self) -> List[Candle]:
        logger.info("Preparing candle list")
        return list(self.candles.values())

    async def light(self, candle_id: int) -> Candle:
        self.candles[candle_id].is_lit = True
        logger.info("Lit the candle", id=candle_id)
        return self.candles[candle_id]

    async def exists(self, candle_id: int) -> bool:
        logger.info("Checking for candle existence")
        return candle_id in self.candles

    async def add(self, candle: Candle) -> Candle:
        self.candles[candle.id] = candle
        logger.info("Added new candle")
        return candle

    async def __aenter__(self) -> CandleDb:
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        logger.info("Shutting down the candle database")
