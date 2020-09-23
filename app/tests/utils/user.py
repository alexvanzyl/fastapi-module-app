import random
import string

from sqlalchemy.orm import Session

from app.user import actions
from app.user.models import User
from app.user.schemas import UserCreate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def create_random_user(db: Session, *, email: str = None, password: str = None) -> User:
    email = email or random_email()
    password = password or random_lower_string()
    user_in = UserCreate(email=email, password=password)
    return actions.user.create(db=db, obj_in=user_in)
