from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import get_db

router = APIRouter()

@router.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT NOW()"))
    current_time = result.scalar_one()
    return {"current_time": str(current_time), "DB": "Running", "status": "ok"}
