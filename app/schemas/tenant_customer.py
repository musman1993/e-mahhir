# app/schemas/tenant_customer.py

from typing import Optional
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from .user import UserOutInDetail

# Base schema shared by all
class TenantCustomerBase(BaseModel):
    tenant_id: Optional[UUID] = None
    customer_id: Optional[UUID] = None
    is_blocked: Optional[bool] = None
    joined_at: Optional[datetime] = None


# For creation (POST)
class TenantCustomerCreate(TenantCustomerBase):
    pass


# For partial updates (PATCH)
class TenantCustomerUpdate(BaseModel):
    tenant_id: Optional[UUID] = None
    customer_id: Optional[UUID] = None
    is_blocked: Optional[bool] = None
    joined_at: Optional[datetime] = None

class TenantCustomerRead(BaseModel):
    id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    preferred_language: Optional[str] = None
    notes: Optional[str] = None
    soft_delete_flag: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    user: Optional[UserOutInDetail] = None

    class Config:
        orm_mode = True
