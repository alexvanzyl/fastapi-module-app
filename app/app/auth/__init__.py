from fastapi import FastAPI

from ..config import settings
from .routes import router


def init_app(app: FastAPI) -> None:
    app.include_router(router, prefix=f'{settings.API_V1_STR}/auth', tags=['auth'])
