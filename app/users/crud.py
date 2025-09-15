from sqlmodel import Session, select
from ..users.models import User
from .security import hash_password


def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email)).first()


def create_user(session: Session, email: str, password: str) -> User:
    user = User(email=email, hashed_password=hash_password(password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
