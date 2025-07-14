from fastapi import FastAPI
from loguru import logger
from app.api.v1.routes import health
from app.api.v1.routes import user
from app.db.base import Base
from app.db.models import *
from app.db.session import engine
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import engine, init_db
from app.db.base import Base
from app.api.v1.routes import auth, user, tenant
from app.core.security import get_current_user
from contextlib import asynccontextmanager
import asyncio

logger.add("stdout", format="{time} {level} {message}", level="INFO")

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.on_event("shutdown") 
async def on_shutdown():
    await engine.dispose()

@app.get("/")
async def root():
    return {"message": "E-Mahhir API"}

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": current_user}

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health&db_time"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(tenant.router, prefix="/api/v1/tenants", tags=["tenants"])
# app.include_router(role.router, prefix="/api/v1/roles", tags=["roles"])