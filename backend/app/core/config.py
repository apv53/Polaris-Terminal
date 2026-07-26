from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache
from pathlib import Path
from typing import Literal
import os

BASE_DIR = Path(__file__).resolve().parents[2]
CURRENT_ENV = os.getenv("APP_ENVIRONMENT", "local")
ENV_FILE_PATH = BASE_DIR / f".env.{CURRENT_ENV}"

class Settings(BaseSettings):
    
    #Application Specific Configuration   
    app_name: str = "Polaris Terminal"
    app_version: str = "0.1.0"
    app_environment: Literal[
        "local", "docker",
        "testing", "production"] = CURRENT_ENV
    
    debug: bool = True
    
    #Database Configuration
    database_url: str 
    database_echo: bool = False
    
    model_config = SettingsConfigDict(
            env_file = ENV_FILE_PATH,
            env_file_encoding = "utf-8",
            extra = "ignore"
        )
    
@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()