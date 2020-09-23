from typing import Optional

from sqlalchemy.orm import Session

from ..core.security import get_hashed_password, verify_password
from .models import User
from .schemas import UserCreate


class UserActions():
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(email=obj_in.email, password=get_hashed_password(obj_in.password))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(user.password, password):
            return None
        return user


user = UserActions()
