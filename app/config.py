from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL_NAME: str
    BACKEND_URL: str

    EMAIL: str
    PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra = "ignore",
    )

settings = Settings()