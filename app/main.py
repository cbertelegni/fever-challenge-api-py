from fastapi import FastAPI
from app.core.config import settings
from app.api import api


app = FastAPI(title=settings.PROJECT_NAME)


app.include_router(api.router)
