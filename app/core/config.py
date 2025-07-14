# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LOGURU_LEVEL: str
    DATABASE_URI: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OTP_EXPIRE_MINUTES: int = 5
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587

    class Config:
        env_file = ".env"

settings = Settings()
