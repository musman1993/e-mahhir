from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.stock_movement import StockMovement
from app.schemas.stock_movement import StockMovementCreate, StockMovementRead

async def create_stock_movement(db: AsyncSession, movement_in: StockMovementCreate) -> StockMovement:
    db_movement = StockMovement(**movement_in)
    db.add(db_movement)
    await db.commit()
    await db.refresh(db_movement)
    return db_movement

async def get_stock_movement(db: AsyncSession, movement_id: UUID) -> StockMovement | None:
    result = await db.execute(select(StockMovement).where(StockMovement.id == movement_id))
    return result.scalars().first()

async def get_stock_movements(db: AsyncSession) -> list[StockMovement]:
    result = await db.execute(select(StockMovement))
    return result.scalars().all()

async def update_stock_movement(db: AsyncSession, movement_id: UUID, movement_in: StockMovementCreate) -> StockMovement | None:
    await db.execute(update(StockMovement).where(StockMovement.id == movement_id).values(**movement_in))
    await db.commit()
    return await get_stock_movement(db, movement_id)

async def delete_stock_movement(db: AsyncSession, movement_id: UUID) -> None:
    await db.execute(delete(StockMovement).where(StockMovement.id == movement_id))
    await db.commit()
