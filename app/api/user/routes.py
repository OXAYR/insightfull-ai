# app/api/v1/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
@router.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Database connected!"}