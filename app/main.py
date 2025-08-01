from fastapi import FastAPI
from app.api.v1.routes import router as v1_router
from app.core.database import Base, engine
from app.models.user import User
from app.api.user.routes import router as user_router

app = FastAPI(title="AI Assistant")

Base.metadata.create_all(bind=engine)

app.include_router(v1_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/user")
