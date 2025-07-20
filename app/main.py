from fastapi import FastAPI
from app.core.config import settings
from app.api.routers import main_router
from app.core.init_db import create_first_superuser


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    redoc_url=None
)
app.include_router(main_router)


# При старте приложения запускаем корутину create_first_superuser.
@app.on_event('startup')
async def startup():
    await create_first_superuser()


@app.on_event('shutdown')
async def shutdown_event():
    print("Приложение остановлено")
