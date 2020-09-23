from typing import Any, List

from fastapi import APIRouter

from . import schemas

auth_router = APIRouter()
router = APIRouter()


@auth_router.post('/login')
def login():
    pass


@router.get('/', response_model=List[schemas.User])
def list_users() -> Any:
    users = [
        schemas.UserCreate(email="a@abc.com", password="hello"),
        schemas.UserCreate(email="b@abc.com", password="hello")
    ]
    return users
