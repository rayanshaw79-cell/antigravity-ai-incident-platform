from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Antigravity AI Incident Platform"
    environment: str = "development"
    log_level: str = "INFO"
    slack_webhook_url: str | None = None


    class Config:
        env_file = ".env"

settings = Settings()
