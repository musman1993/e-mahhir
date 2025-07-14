# app/crud/tenant_customer.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.db.models.tenant_customer import TenantCustomer
from app.db.models.customer import Customer
from sqlalchemy.orm import selectinload


async def create_tenant_customer(db: AsyncSession, tenant_customer_data: dict):
    db_tenant = TenantCustomer(**tenant_customer_data)
    db.add(db_tenant)
    await db.commit()
    await db.refresh(db_tenant)
    return db_tenant


async def get_tenant_customer_by_id(db: AsyncSession, tenant_customer_id: UUID):
    result = await db.execute(
        select(TenantCustomer)
        .options(selectinload(TenantCustomer.customer))
        .where(TenantCustomer.id == tenant_customer_id)
    )
    return result.scalars().first()


async def get_all_tenant_customers(db: AsyncSession, tenant_id: str, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(TenantCustomer)
        .options(
            selectinload(TenantCustomer.customer).selectinload(Customer.user)
        )
        .where(TenantCustomer.tenant_id == tenant_id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


async def update_tenant(db: AsyncSession, tenant_customer_id: UUID, update_data: dict):
    db_tenant = await get_tenant_customer_by_id(db, tenant_customer_id)
    if db_tenant:
        for key, value in update_data.items():
            setattr(db_tenant, key, value)
        await db.commit()
        await db.refresh(db_tenant)
    return db_tenant

async def delete_tenant_customer(db: AsyncSession, tenant_customer_id: UUID):
    db_tenant = await get_tenant_customer_by_id(db, tenant_customer_id)
    if db_tenant:
        await db.delete(db_tenant)
        await db.commit()
    return db_tenant
