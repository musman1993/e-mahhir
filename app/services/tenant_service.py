# app/services/tenant_service.py
from fastapi import HTTPException, status
from uuid import UUID
from app.crud.tenant import create_tenant, get_tenant_by_id, update_tenant, delete_tenant, get_tenants
from app.schemas.tenant import TenantCreate, TenantUpdate
from app.db.session import AsyncSession

async def create_tenant_service(db: AsyncSession, tenant_data: TenantCreate):
    return await create_tenant(db, tenant_data.model_dump())

async def get_tenant_service(db: AsyncSession, tenant_id: UUID):
    tenant = await get_tenant_by_id(db, tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

async def update_tenant_service(db: AsyncSession, tenant_id: UUID, tenant_data: TenantUpdate):
    tenant = await get_tenant_by_id(db, tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    
    update_dict = tenant_data.model_dump(exclude_unset=True)
    return await update_tenant(db, tenant_id, update_dict)

async def delete_tenant_service(db: AsyncSession, tenant_id: UUID):
    tenant = await get_tenant_by_id(db, tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return await delete_tenant(db, tenant_id)

async def get_tenants_service(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await get_tenants(db, skip=skip, limit=limit)