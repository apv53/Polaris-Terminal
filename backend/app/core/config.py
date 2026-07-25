from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache

class Settings(BaseSettings):
    
    #Application Specific Configuration   
    app_name: str = "Polaris Terminal"
    app_version: str = "0.1.0"
    app_environment: str = "development"
    debug: bool = True
    
    #Database Configuration
    database_url: str 
    database_echo: bool = False
    
    model_config = SettingsConfigDict(
            env_file = ".env",
            env_file_encoding = "utf-8",
            extra = "ignore"
        )
    
@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()