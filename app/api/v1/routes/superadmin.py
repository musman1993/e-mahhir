# app/api/v1/routes/superadmin.py
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from typing import List
from app.services.superadmin_service import (
    login_superadmin,
    register_superadmin,
    get_current_superadmin_from_token,
    update_superadmin_service,
    get_all_superadmins,
    delete_superadmin_service,
)

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.schemas.superadmin import SuperAdminRead, SuperAdminLogin, SuperAdminRegister, SuperAdminCreate

router = APIRouter()
bearer_scheme = HTTPBearer()


@router.get(
    "/current",
    response_model=SuperAdminRead,
)
async def get_current_superadmin(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
):
    token = credentials.credentials
    return await get_current_superadmin_from_token(db, token)

@router.get(
    "/all",
    response_model=List[SuperAdminRead],
)
async def get_all_superadmins_accounts(
    # credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
):
    # token = credentials.credentials
    return await get_all_superadmins(db)



@router.post("/register")
async def register(
    user_data: SuperAdminRegister,
    # credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
):
    return await register_superadmin(db, user_data)


@router.post("/login")
async def login(user_data: SuperAdminLogin, db: AsyncSession = Depends(get_db)):
    return await login_superadmin(db, user_data)


@router.put("/{superadmin_id}")
async def update_superadmin(
    superadmin_id: UUID,
    superadmin_data: SuperAdminRegister,
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
):
    return await update_superadmin_service(db, superadmin_id, superadmin_data)


@router.delete("/{superadmin_id}")
async def update_superadmin(
    superadmin_id: UUID,
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
):
    return await delete_superadmin_service(db, superadmin_id)
