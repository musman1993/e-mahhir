from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.app_customer import AppCustomer
from app.schemas.app_customer import AppCustomerCreate, AppCustomerRead

async def create_app_customer(db: AsyncSession, customer_in: AppCustomerCreate) -> AppCustomer:
    db_customer = AppCustomer(**customer_in)
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer

async def get_app_customer(db: AsyncSession, email: str) -> AppCustomer | None:
    result = await db.execute(select(AppCustomer).where(AppCustomer.email == email))
    return result.scalars().first()

async def get_app_customer_by_id(db: AsyncSession, customer_id: UUID) -> AppCustomer | None:
    result = await db.execute(select(AppCustomer).where(AppCustomer.id == customer_id))
    return result.scalars().first()



async def get_app_customers(db: AsyncSession) -> list[AppCustomer]:
    result = await db.execute(select(AppCustomer))
    return result.scalars().all()

async def update_app_customer(db: AsyncSession, customer_id: UUID, customer_in: AppCustomerCreate) -> AppCustomer | None:
    await db.execute(update(AppCustomer).where(AppCustomer.id == customer_id).values(**customer_in))
    await db.commit()
    return await get_app_customer(db, customer_id)

async def delete_app_customer(db: AsyncSession, customer_id: UUID) -> None:
    await db.execute(delete(AppCustomer).where(AppCustomer.id == customer_id))
    await db.commit()
