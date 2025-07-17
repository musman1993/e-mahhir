from typing import List
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import (
    decode_access_token,
    get_password_hash,
    verify_password,
    create_access_token,
)
from app.db.models.superadmin import SuperAdmin
from uuid import UUID
from app.schemas.auth import AuthResponse
from app.schemas.superadmin import SuperAdminCreate, SuperAdminLogin, SuperAdminRegister
from app.crud.superadmin import create_superadmin, get_superadmin_by_email, get_superadmin_by_id, get_superadmins, update_superadmin, delete_superadmin


async def register_superadmin(db: AsyncSession, data: SuperAdminRegister):
    hashed_password = get_password_hash(data.password)
    existing_user = await get_superadmin_by_email(db, data.email)
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Email already registered as superadmin"
        )
    user_in = data.dict()
    user_in["password_hash"] = hashed_password
    user_in.pop("password")
    user = await create_superadmin(db, user_in)
    user_dict = user.__dict__.copy()
    user_dict.pop("password_hash", None)
    return user_dict

async def login_superadmin(db: AsyncSession, data: SuperAdminLogin):
    user = None
    user = await get_superadmin_by_email(db, data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong Password"
        )

    access_token = create_access_token(
        {"sub": str(user.id)}
    )
    return AuthResponse(access_token=access_token)

async def update_superadmin_service(db: AsyncSession, superadmin_id: UUID, superadmin_in: SuperAdminRegister) -> SuperAdmin | None:
    return await update_superadmin(db, superadmin_id, superadmin_in)

async def get_all_superadmins(db: AsyncSession) -> List[SuperAdmin] | None:
    return await get_superadmins(db)

async def delete_superadmin_service(db: AsyncSession, superadmin_id: UUID) -> None:
    await delete_superadmin(db, superadmin_id)


async def get_current_superadmin_from_token(db: AsyncSession, token: str):
    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )
        user = await get_superadmin_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
