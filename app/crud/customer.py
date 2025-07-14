# app/crud/tenant.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.db.models.customer import Customer
from app.utils.db import get_or_404


async def create_customer(db: AsyncSession, customer_data: dict):
    user_id = customer_data.get("user_id")
    from .user import get_user_by_id
    user = await get_or_404(get_user_by_id(db, user_id), entity_name="User")
    
    db_customer = Customer(**customer_data)
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer


async def get_customer_by_id(db: AsyncSession, customer_id: UUID):
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    return result.scalars().first()

async def get_customers(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Customer).offset(skip).limit(limit))
    return result.scalars().all()

async def update_customer(db: AsyncSession, customer_id: UUID, update_data: dict):
    db_customer = await get_customer_by_id(db, customer_id)
    if db_customer:
        for key, value in update_data.items():
            setattr(db_customer, key, value)
        await db.commit()
        await db.refresh(db_customer)
    return db_customer


async def delete_customer(db: AsyncSession, customer_id: UUID):
    db_customer = await get_customer_by_id(db, customer_id)
    if db_customer:
        await db.delete(db_customer)
        await db.commit()
    return db_customer
