from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Fever Providers API - Cristian Bertelegni"
    PROVIDER_BASE_URL: str = "https://provider.code-challenge.feverup.com"

    class Config:
        case_sensitive = True
        # env_file = ".env"


settings = Settings()
