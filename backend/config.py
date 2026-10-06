from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Business Operations Agent Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    DATABASE_URL: str = "postgresql://admin:securepassword123@localhost:5432/ai_ops_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL_NAME: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()