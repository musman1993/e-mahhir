# app/services/user_service.py
from fastapi import HTTPException, status
from uuid import UUID
from app.crud.user import get_user_by_id, update_user, get_all_users_, get_all_tenant_admins_
from app.schemas.user import UserUpdate
from app.db.session import AsyncSession
from app.utils.db import get_or_404

async def get_all_tenant_admins(db: AsyncSession):
    users = await get_or_404(get_all_tenant_admins_(db), entity_name="Tenant Admins")
    return users

async def get_all_users(db: AsyncSession):
    users = await get_or_404(get_all_users_(db), entity_name="Users")
    return users


async def get_user(db: AsyncSession, user_id: UUID):
    user = await get_or_404(get_user_by_id(db, user_id), entity_name="User")
    return user

async def update_user_service(db: AsyncSession, user_id: UUID, update_data: UserUpdate):
    user = await get_or_404(get_user_by_id(db, user_id), entity_name="User")
    
    update_dict = update_data.model_dump(exclude_unset=True)
    return await update_user(db, user_id, update_dict)