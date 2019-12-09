from pydantic import BaseSettings


env_prefix = "HANUKA"


class ServerSettings(BaseSettings):
    port: int = 8000

    class Config:
        env_prefix = f"{env_prefix}__SERVER__"


class Settings(BaseSettings):
    candle_amount: int = 5
    server: ServerSettings = ServerSettings()

    class Config:
        env_prefix = f"{env_prefix}_"
