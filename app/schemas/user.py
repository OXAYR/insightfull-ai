from pydantic import BaseModel, EmailStr

# In Fast api schemas work as transformer like in other frameworks that it will provide the data only what we required

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

class UserLogin(BaseModel):
    email: EmailStr
    password: str