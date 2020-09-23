from fastapi import FastAPI

from ..config import settings
from .routes import router


def init_app(app: FastAPI):
    app.include_router(
        router, prefix=f'{settings.API_V1_STR}/users', tags=['users'])
