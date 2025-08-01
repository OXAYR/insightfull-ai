from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Due to circular import issue writing the import here (Circular import issue is basically when two files try to import each other at the same time )

from app.models.user import User  

def init_db():
    User.metadata.create_all(bind=engine)