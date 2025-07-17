from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.tenant_customer import TenantCustomer
from app.schemas.tenant_customer import TenantCustomerCreate, TenantCustomerRead

async def create_tenant_customer(db: AsyncSession, customer_in: TenantCustomerCreate) -> TenantCustomer:
    db_customer = TenantCustomer(**customer_in)
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer

async def get_tenant_customer(db: AsyncSession, customer_id: UUID) -> TenantCustomer | None:
    result = await db.execute(select(TenantCustomer).where(TenantCustomer.id == customer_id))
    return result.scalars().first()

async def get_tenant_customers(db: AsyncSession) -> list[TenantCustomer]:
    result = await db.execute(select(TenantCustomer))
    return result.scalars().all()

async def update_tenant_customer(db: AsyncSession, customer_id: UUID, customer_in: TenantCustomerCreate) -> TenantCustomer | None:
    await db.execute(update(TenantCustomer).where(TenantCustomer.id == customer_id).values(**customer_in))
    await db.commit()
    return await get_tenant_customer(db, customer_id)

async def delete_tenant_customer(db: AsyncSession, customer_id: UUID) -> None:
    await db.execute(delete(TenantCustomer).where(TenantCustomer.id == customer_id))
    await db.commit()
