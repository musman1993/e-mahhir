from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.inventory_product import InventoryProduct
from app.schemas.inventory_product import InventoryProductCreate, InventoryProductRead

async def create_inventory_product(db: AsyncSession, product_in: InventoryProductCreate) -> InventoryProduct:
    db_product = InventoryProduct(**product_in)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_inventory_product(db: AsyncSession, product_id: UUID) -> InventoryProduct | None:
    result = await db.execute(select(InventoryProduct).where(InventoryProduct.id == product_id))
    return result.scalars().first()

async def get_inventory_products(db: AsyncSession) -> list[InventoryProduct]:
    result = await db.execute(select(InventoryProduct))
    return result.scalars().all()

async def update_inventory_product(db: AsyncSession, product_id: UUID, product_in: InventoryProductCreate) -> InventoryProduct | None:
    await db.execute(update(InventoryProduct).where(InventoryProduct.id == product_id).values(**product_in))
    await db.commit()
    return await get_inventory_product(db, product_id)

async def delete_inventory_product(db: AsyncSession, product_id: UUID) -> None:
    await db.execute(delete(InventoryProduct).where(InventoryProduct.id == product_id))
    await db.commit()
