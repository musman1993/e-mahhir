# app/api/v1/routes/tenant.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List
from app.db.session import get_db
from app.schemas.tenant import TenantCreate, TenantOut, TenantUpdate
from app.schemas.tenant_customer import TenantCustomerRead
from app.schemas.employee import EmployeeOut
from app.services.tenant_service import (
    create_tenant_service,
    get_tenant_service,
    update_tenant_service,
    delete_tenant_service,
    get_tenants_service,
    get_tenant_customers,
    get_tenant_employees
)
from app.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=TenantOut)
async def create_tenant(
    tenant_data: TenantCreate,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await create_tenant_service(db, tenant_data)


@router.get("/", response_model=List[TenantOut])
async def read_all_tenants(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await get_tenants_service(db, skip=skip, limit=limit)


@router.get("/{tenant_id}", response_model=TenantOut)
async def read_tenant(
    tenant_id: UUID,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await get_tenant_service(db, tenant_id)


@router.put("/{tenant_id}", response_model=TenantOut)
async def update_tenant(
    tenant_id: UUID,
    tenant_data: TenantUpdate,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await update_tenant_service(db, tenant_id, tenant_data)


@router.delete("/{tenant_id}")
async def delete_tenant(
    tenant_id: UUID,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await delete_tenant_service(db, tenant_id)

@router.get("/{tenant_id}/customers", response_model=List[TenantCustomerRead])
async def read_tenant_customers(
    tenant_id: UUID,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await get_tenant_customers(db, tenant_id)

@router.get("/{tenant_id}/employees", response_model=List[EmployeeOut])
async def read_tenant_employees(
    tenant_id: UUID,
    db: AsyncSession = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    return await get_tenant_employees(db, tenant_id)

