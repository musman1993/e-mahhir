from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class TenantUserBase(BaseModel):
    tenant_id: UUID
    user_id: UUID
    role_id: UUID
    is_active: bool = True

class TenantUserCreate(TenantUserBase):
    pass

class TenantUserUpdate(BaseModel):
    role_id: Optional[UUID] = None
    is_active: Optional[bool] = None

class TenantUserOut(TenantUserBase):
    id: UUID
    joined_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True