# app/api/v1/routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.db.session import get_db
from app.schemas.user import UserOut, UserUpdate, UserOutInDetail
from app.services.user_service import get_user, update_user_service, get_all_users, get_all_tenant_admins
from app.core.security import get_current_user
from typing import List

router = APIRouter()

@router.get("/", response_model=List[UserOut])
async def read_all_users(
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    users = await get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No user found")
    return users

@router.get("/admins", response_model=List[UserOut])
async def read_all_tenant_admins(
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    users = await get_all_tenant_admins(db)
    if not users:
        raise HTTPException(status_code=404, detail="No user found")
    return users


@router.get("/{user_id}", response_model=UserOutInDetail)
async def read_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await get_user(db, user_id)

@router.put("/{user_id}", response_model=UserOutInDetail)
async def update_user(
    user_id: UUID,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await update_user_service(db, user_id, user_data)