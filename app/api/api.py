from fastapi import APIRouter
from app.api.endpoints import events


router = APIRouter()

router.include_router(events.router, tags=["Events"])