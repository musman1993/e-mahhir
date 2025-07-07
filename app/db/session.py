import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.environ["DB_URI"]

# Create SQLAlchemy async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # logs SQL queries; turn off in prod
    future=True,
)

# Create sessionmaker factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
