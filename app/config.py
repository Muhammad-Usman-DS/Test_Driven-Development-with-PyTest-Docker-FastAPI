import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file = "app/.env")

    environment : str = "dev"
    testing : bool = bool(0)

@lru_cache()
def get_Settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()