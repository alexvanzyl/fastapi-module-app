from sqlalchemy.orm import Session

from app.user import actions
from app.user.schemas import UserCreate
from tests.utils.user import (create_random_user, random_email,
                              random_lower_string)


def test_get_by_email(db_session: Session) -> None:
    user = create_random_user(db_session)
    user_by_email = actions.user.get_by_email(db=db_session, email=user.email)

    assert user_by_email
    assert user_by_email.email == user.email


def test_create_user(db_session: Session) -> None:
    email = random_email()
    plain_password = random_lower_string()
    user_in = UserCreate(email=email, password=plain_password)
    user = actions.user.create(db=db_session, obj_in=user_in)

    assert user.email == email
    assert hasattr(user, 'password')
    assert user.password != plain_password


def test_authenticate(db_session: Session) -> None:
    plain_password = random_lower_string()
    user = create_random_user(db_session, password=plain_password)
    auth_user = actions.user.authenticate(
        db=db_session, email=user.email, password=plain_password)

    assert auth_user
    assert user.email == auth_user.email
