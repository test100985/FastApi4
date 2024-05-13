from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Base

import os

DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "db")
DB_PASS = os.environ.get("DB_PASS", "password")
DB_USER = os.environ.get("DB_USER", "user")

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker()

async def init_db():
    Base.metadata.create_all(bind=engine)
