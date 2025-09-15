from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..main import engine
from .schemas import UserCreate, UserRead
from .crud import get_user_by_email, create_user

router = APIRouter()


def get_session():
    with Session(engine) as session:
        yield session


@router.post("/register", response_model=UserRead)
def register(data: UserCreate, session: Session = Depends(get_session)):
    if get_user_by_email(session, data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_user(session, data.email, data.password)
    # TODO: send verification email async (MailHog in dev)
    return UserRead.from_orm(user)
