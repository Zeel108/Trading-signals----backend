from sqlalchemy import create_engine
#creates engine which wraps around the database

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#base class from where all the base data model so we know which models we have
#from core.config import settings

DATABASE_URL = "sqlite:///test.db"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()