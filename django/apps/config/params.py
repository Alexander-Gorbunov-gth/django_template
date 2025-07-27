from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".dev.env", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_SCHEMAS: str


class DjangoSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".dev.env", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )
    DEBUG: bool
    SECRET_KEY: str
    ALLOWED_HOSTS: str
    CSRF_TRUSTED_ORIGINS: str


class Config(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    django: DjangoSettings = DjangoSettings()

    @property
    def db_url(self) -> str:
        return f"postgresql://{self.db.DB_USER}:{self.db.DB_PASSWORD}@{self.db.DB_HOST}:{self.db.DB_PORT}/{self.db.DB_NAME}"


cfg = Config()
