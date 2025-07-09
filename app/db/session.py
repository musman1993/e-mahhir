from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.utils import read_secret

DATABASE_URL = read_secret("DB_URI")

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
