from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str = "gridiq"
    postgres_password: str = "gridiq_password"
    postgres_db: str = "gridiq"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    # Load from .env at project root if present
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        case_sensitive=False,
    )

    @property
    def database_url(self) -> str:
        # SQLAlchemy 2.x URL with psycopg3 driver
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


settings = Settings()


