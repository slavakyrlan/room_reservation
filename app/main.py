from fastapi import FastAPI
from app.core.config import settings
from app.api.meeting_room import router


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    redoc_url=None
)
app.include_router(router)
