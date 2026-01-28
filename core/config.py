import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
#creates engine which wraps around the database

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#base class from where all the base data model so we know which models we have
#from core.config import settings

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()