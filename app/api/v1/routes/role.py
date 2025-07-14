# # app/api/v1/routes/role.py
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from uuid import UUID
# from typing import List
# from app.db.session import get_db
# from app.schemas.role import RoleBase, RoleOut, RoleUpdate
# from app.services.role_service import (
#     create_role_service,
#     get_role_service,
#     update_role_service,
#     delete_role_service,
#     get_roles_by_tenant_service,
#     get_all_roles_service
# )
# from app.core.security import get_current_user

# router = APIRouter()

# @router.post("/", response_model=RoleOut)
# async def create_role(
#     role_data: RoleBase,
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await create_role_service(db, role_data)

# @router.get("/tenant/{tenant_id}", response_model=List[RoleOut])
# async def read_roles_by_tenant(
#     tenant_id: UUID,
#     skip: int = 0,
#     limit: int = 100,
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await get_roles_by_tenant_service(db, tenant_id, skip=skip, limit=limit)

# @router.get("/{role_id}", response_model=RoleOut)
# async def read_role(
#     role_id: UUID,
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await get_role_service(db, role_id)

# @router.get("/", response_model=List[RoleOut])
# async def read_all_roles(
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await get_all_roles_service(db)


# @router.put("/{role_id}", response_model=RoleOut)
# async def update_role(
#     role_id: UUID,
#     role_data: RoleUpdate,
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await update_role_service(db, role_id, role_data)

# @router.delete("/{role_id}")
# async def delete_role(
#     role_id: UUID,
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await delete_role_service(db, role_id)