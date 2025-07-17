from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.customer_product import CustomerProduct
from app.schemas.customer_product import CustomerProductCreate, CustomerProductRead

async def create_customer_product(db: AsyncSession, product_in: CustomerProductCreate) -> CustomerProduct:
    db_product = CustomerProduct(**product_in)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_customer_product(db: AsyncSession, product_id: UUID) -> CustomerProduct | None:
    result = await db.execute(select(CustomerProduct).where(CustomerProduct.id == product_id))
    return result.scalars().first()

async def get_customer_products(db: AsyncSession) -> list[CustomerProduct]:
    result = await db.execute(select(CustomerProduct))
    return result.scalars().all()

async def update_customer_product(db: AsyncSession, product_id: UUID, product_in: CustomerProductCreate) -> CustomerProduct | None:
    await db.execute(update(CustomerProduct).where(CustomerProduct.id == product_id).values(**product_in))
    await db.commit()
    return await get_customer_product(db, product_id)

async def delete_customer_product(db: AsyncSession, product_id: UUID) -> None:
    await db.execute(delete(CustomerProduct).where(CustomerProduct.id == product_id))
    await db.commit()
