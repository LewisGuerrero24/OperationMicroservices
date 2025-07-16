
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_ALGORITHM: str
    ACCESS_TOKEN_SECRET: str
    REFRESH_TOKEN_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    class Config:
        env_file = ".env"

# Instancia para usar en toda la app
settings = Settings()