from sqlmodel import SQLModel, create_engine, Session
import os

sqlite_url = "sqlite:///database.db"
engine_url = os.getenv("DATABASE_URL", sqlite_url)

engine = create_engine(engine_url, connect_args={"check_same_thread": False} if "sqlite" in engine_url else {})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session