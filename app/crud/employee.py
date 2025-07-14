# app/crud/tenant.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.db.models.employee import Employee
from app.utils.db import get_or_404
from sqlalchemy.orm import selectinload

async def create_employee(db: AsyncSession, employee_data: dict):
    user_id = employee_data.get("user_id")
    from .user import get_user_by_id
    user = await get_or_404(get_user_by_id(db, user_id), entity_name="User")
    
    db_employee = Employee(**employee_data)
    db.add(db_employee)
    await db.commit()
    await db.refresh(db_employee)
    return db_employee

async def get_employee_by_id(db: AsyncSession, employee_id: UUID):
    result = await db.execute(select(Employee).where(Employee.id == employee_id))
    return result.scalars().first()

async def get_all_tenant_employees(db: AsyncSession, tenant_id: str, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(Employee)
        .where(Employee.tenant_id == tenant_id)
        # .options(selectinload(Employee.customer))
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()



async def update_employee(db: AsyncSession, employee_id: UUID, update_data: dict):
    db_employee = await get_employee_by_id(db, employee_id)
    if db_employee:
        for key, value in update_data.items():
            setattr(db_employee, key, value)
        await db.commit()
        await db.refresh(db_employee)
    return db_employee


async def delete_employee(db: AsyncSession, employee_id: UUID):
    db_employee = await get_employee_by_id(db, employee_id)
    if db_employee:
        await db.delete(db_employee)
        await db.commit()
    return db_employee
