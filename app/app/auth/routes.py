from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from ..core import security
from ..core.dependencies import get_db
from ..user import actions as user_action
from . import schemas

router = APIRouter()


@router.post('/token', response_model=schemas.Token)
def auth_token(
        db: Session = Depends(get_db), from_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = user_action.user.authenticate(
        db, email=from_data.username, password=from_data.password)
    if not user:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Invalid email or password')

    return {
        'access_token': security.create_access_token(user.id),
        'token_type': 'bearer',
    }
