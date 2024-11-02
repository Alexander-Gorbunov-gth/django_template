from functools import lru_cache
from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict


@final
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".dev.env", ".env"),
        env_file_encoding="utf-8",
    )
    DEBUG: bool
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_SCHEMAS: str
    SECRET_KEY: str
    ALLOWED_HOSTS: str
    CSRF_TRUSTED_ORIGINS: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
