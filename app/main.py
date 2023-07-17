from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.routers import main_router
from app.core.config import settings
from app.core.db import DATABASE_CONFIG

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)

app.include_router(main_router)


register_tortoise(
    app,
    config=DATABASE_CONFIG,
    generate_schemas=True,
    add_exception_handlers=True,
)
