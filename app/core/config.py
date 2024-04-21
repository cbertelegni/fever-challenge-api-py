from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Fever Providers API - Cristian Bertelegni"
    PROVIDER_BASE_URL: str = "https://provider.code-challenge.feverup.com"
    DATABASE_SCHEME: str
    DATABASE_USER: str
    DATABASE_PASS: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    DATABASE_ARGS: str = ""
    SQLALCHEMY_POOL_SIZE: int = 15
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
