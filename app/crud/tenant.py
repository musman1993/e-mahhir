# app/crud/tenant.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.db.models.tenant import Tenant
from .user import get_user_by_id


async def create_tenant(db: AsyncSession, tenant_data: dict):
    created_by_id = tenant_data.get("created_by")
    if not created_by_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing 'created_by' in tenant data.",
        )

    user = await get_user_by_id(db, created_by_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with given ID not found.",
        )

    if getattr(user, "role", None) != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin users can create tenants.",
        )

    # Check no tenant already created by this user
    existing_tenant = await get_tenant_created_by(db, created_by_id)
    if existing_tenant:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This user already have one tenant.",
        )

    db_tenant = Tenant(**tenant_data)
    db.add(db_tenant)
    await db.commit()
    await db.refresh(db_tenant)
    return db_tenant


async def get_tenant_by_id(db: AsyncSession, tenant_id: UUID):
    result = await db.execute(select(Tenant).where(Tenant.id == tenant_id))
    return result.scalars().first()


async def get_tenant_created_by(db: AsyncSession, user_id: UUID):
    result = await db.execute(select(Tenant).where(Tenant.created_by == user_id))
    return result.scalars().first()


async def get_tenants(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Tenant).offset(skip).limit(limit))
    return result.scalars().all()


async def update_tenant(db: AsyncSession, tenant_id: UUID, update_data: dict):
    db_tenant = await get_tenant_by_id(db, tenant_id)
    if db_tenant:
        for key, value in update_data.items():
            setattr(db_tenant, key, value)
        await db.commit()
        await db.refresh(db_tenant)
    return db_tenant


async def delete_tenant(db: AsyncSession, tenant_id: UUID):
    db_tenant = await get_tenant_by_id(db, tenant_id)
    if db_tenant:
        await db.delete(db_tenant)
        await db.commit()
    return db_tenant
