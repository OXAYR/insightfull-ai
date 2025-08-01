from pydantic import BaseModel, EmailStr

# For creating a new user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# For sending user data back to the client (excluding sensitive info)
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True  # This tells Pydantic to convert from ORM models to JSON
