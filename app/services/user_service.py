# app/services/user_service.py
from fastapi import HTTPException, status
from uuid import UUID
from app.crud.user import get_user_by_id, update_user, get_all_users_, get_all_tenant_admins_
from app.schemas.user import UserUpdate
from app.db.session import AsyncSession

async def get_all_tenant_admins(db: AsyncSession):
    users = await get_all_tenant_admins_(db)
    if not users:
        raise HTTPException(status_code=404, detail="No user found")
    return users


async def get_all_users(db: AsyncSession):
    users = await get_all_users_(db)
    if not users:
        raise HTTPException(status_code=404, detail="No user found")
    return users


async def get_user(db: AsyncSession, user_id: UUID):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def update_user_service(db: AsyncSession, user_id: UUID, update_data: UserUpdate):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_dict = update_data.model_dump(exclude_unset=True)
    return await update_user(db, user_id, update_dict)