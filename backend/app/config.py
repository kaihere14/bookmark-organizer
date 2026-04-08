from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = None
    database_port: str = None
    database_password: str = None
    database_name: str = None
    database_user: str = None
    
    model_config = {"env_file": ".env"}

settings = Settings()