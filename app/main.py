import time
from fastapi import FastAPI, Request
from app.core.config import settings
from app.api import api
from app.services.events import EventService
from app.db.session import get_db


app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
def startup_event():
    """This method must be moved to a celery task"""
    db = next(get_db())
    try:
        event_service = EventService.create(db=db)
        event_service.update_events_from_provider()
    finally:
        db.close()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    response.headers["X-Process-Time"] = f"{process_time} ms"
    return response

app.include_router(api.router)
