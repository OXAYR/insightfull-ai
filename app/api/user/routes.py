# app/api/v1/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, UserLogin
from app.utils.security import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# The depend in the params is basically managin the session for db opening and closing for the request otherwise we have to do it manually and it will cause memory leak if we forgot to close it 
# NOTE: It only opens on the request initiation 
# we dont have request.body in the fast api in this we use the schema directly for validate it properly 
@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    db_user = models.User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
@router.post('/login')
def login_user(user: UserLogin, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == UserLogin.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not verify_password(UserLogin.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_user