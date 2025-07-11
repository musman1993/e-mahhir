# app/db/session.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings
from app.db.base import Base

engine = create_async_engine(settings.DATABASE_URI, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    # """Initialize database with proper ENUM creation order"""
    async with engine.begin() as conn:
        await Base.create_enum_types(engine)
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    # """Dependency for FastAPI routes"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
        
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
# from app.utils.utils import read_secret

# DATABASE_URL = read_secret("DATABASE_URI")

# engine = create_async_engine(
#     DATABASE_URL,
#     echo=True,          # logs SQL queries; turn off in prod
#     future=True,
# )
    
# # Create sessionmaker factory
# AsyncSessionLocal = sessionmaker(
#     bind=engine,
#     expire_on_commit=False,
#     class_=AsyncSession,
# )
