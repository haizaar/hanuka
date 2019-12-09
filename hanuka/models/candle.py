from pydantic import BaseModel


class Candle(BaseModel):
    id: int
    is_lit: bool = False
