# app/services/tenant_service.py
from fastapi import HTTPException, status
from uuid import UUID
from app.crud.tenant import create_tenant, get_tenant_by_id, update_tenant, delete_tenant, get_tenants
from app.crud.tenant_customer import get_all_tenant_customers
from app.crud.employee import get_all_tenant_employees
from app.schemas.tenant import TenantCreate, TenantUpdate
from app.db.session import AsyncSession
from app.utils.db import get_or_404

async def create_tenant_service(db: AsyncSession, tenant_data: TenantCreate):
    return await create_tenant(db, tenant_data.model_dump())

async def get_tenant_service(db: AsyncSession, tenant_id: UUID):
    tenant = await get_or_404(get_tenant_by_id(db, tenant_id), entity_name="Tenant")
    return tenant

async def update_tenant_service(db: AsyncSession, tenant_id: UUID, tenant_data: TenantUpdate):
    tenant_data = await get_or_404(get_tenant_by_id(db, tenant_id), entity_name="Tenant")
    update_dict = tenant_data.model_dump(exclude_unset=True)
    return await update_tenant(db, tenant_id, update_dict)

async def delete_tenant_service(db: AsyncSession, tenant_id: UUID):
    tenant = await get_or_404(get_tenant_by_id(db, tenant_id), entity_name="Tenant")
    return await delete_tenant(db, tenant_id)

async def get_tenants_service(db: AsyncSession, skip: int = 0, limit: int = 100):
    return await get_tenants(db, skip=skip, limit=limit)

async def get_tenant_customers(db: AsyncSession, tenant_id: str, skip: int = 0, limit: int = 100):
    return await get_all_tenant_customers(db, tenant_id, skip=skip, limit=limit)

async def get_tenant_employees(db: AsyncSession, tenant_id: str, skip: int = 0, limit: int = 100):
    return await get_all_tenant_employees(db, tenant_id, skip=skip, limit=limit)