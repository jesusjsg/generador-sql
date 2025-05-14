from typing import Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        env_prefix="APP_",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    API_NAME: str
    DATABASE_AUTH_TOKEN: SecretStr
    DATABASE_URL: str
    DEBUG: bool
    # Agregar los cors en produccion


settings = Settings()
