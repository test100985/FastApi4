import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base




engine_test = create_engine('postgresql://postgres:1234@localhost/postgres')
session_test = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)
Base = declarative_base()


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)