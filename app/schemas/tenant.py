# app/schemas/tenant.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class TenantBase(BaseModel):
    name: str
    domain: str
    created_by: UUID
    is_active: bool = True

class TenantCreate(TenantBase):
    pass

class TenantUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    is_active: Optional[bool] = None

class TenantOut(TenantBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True