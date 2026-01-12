import os
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    DEBUG: bool = True
    PROJECT_NAME: str = "Todo Web Application"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "0.1.0"

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_ECHO: bool = True
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 30

    # Authentication
    JWT_SECRET_KEY: str = "todo-app-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"

    @property
    def allowed_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    # Security
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "0.0.0.0"]
    HTTPS_REDIRECT: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()