from pydantic import BaseSettings, AnyHttpUrl
from typing import List, Optional
import secrets

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI GraphQL"
    PROJECT_DESCRIPTION: Optional[str]
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # Db configs
    DRIVER: str
    HOST: str
    DATABASE: str
    USER: str
    PASSWORD: str
    PORT: str

    class Config:
        env_file = ".env"

settings = Settings()
