# app/services/role_service.py
from fastapi import HTTPException, status
from uuid import UUID
from app.crud.role import (
    create_role,
    get_role_by_id,
    update_role,
    delete_role,
    get_roles_by_tenant,
    get_all_roles,
)
from app.schemas.role import RoleCreate, RoleUpdate
from app.db.session import AsyncSession


async def create_role_service(db: AsyncSession, role_data: RoleCreate):
    return await create_role(db, role_data.model_dump())


async def get_role_service(db: AsyncSession, role_id: UUID):
    role = await get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


async def get_all_roles_service(db: AsyncSession):
    role = await get_all_roles(db)
    if not role:
        raise HTTPException(status_code=404, detail="No role found")
    return role


async def update_role_service(db: AsyncSession, role_id: UUID, role_data: RoleUpdate):
    role = await get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    update_dict = role_data.model_dump(exclude_unset=True)
    return await update_role(db, role_id, update_dict)


async def delete_role_service(db: AsyncSession, role_id: UUID):
    role = await get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return await delete_role(db, role_id)


async def get_roles_by_tenant_service(
    db: AsyncSession, tenant_id: UUID, skip: int = 0, limit: int = 100
):
    return await get_roles_by_tenant(db, tenant_id, skip=skip, limit=limit)
