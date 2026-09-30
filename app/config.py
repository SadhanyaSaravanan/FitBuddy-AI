from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = Field(
        default="FitBuddy",
        validation_alias="APP_NAME",
    )

    database_url: str = Field(
        default=f"sqlite:///{(BASE_DIR / 'fitbuddy.db').as_posix()}",
        validation_alias="DATABASE_URL",
    )

    gemini_api_key: str | None = Field(
        default=None,
        validation_alias="GEMINI_API_KEY",
    )

    workout_model: str = Field(
        default="gemini-1.5-pro",
        validation_alias="WORKOUT_MODEL",
    )

    nutrition_model: str = Field(
        default="gemini-1.5-flash",
        validation_alias="NUTRITION_MODEL",
    )

    ai_mode: str = Field(
        default="mock",
        validation_alias="AI_MODE",
    )

    admin_token: str | None = Field(
        default=None,
        validation_alias="ADMIN_TOKEN",
    )

    @property
    def is_mock(self) -> bool:
        return self.ai_mode.strip().lower() == "mock"


@lru_cache
def get_settings() -> Settings:
    return Settings()
