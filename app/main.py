from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI(title="RusLang API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(users_router, prefix="/api/auth", tags=["auth"])
