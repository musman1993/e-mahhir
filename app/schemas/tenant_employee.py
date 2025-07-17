from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TenantEmployeeBase(BaseModel):
    tenant_id: UUID
    role_id: UUID
    email: str
    full_name: str | None = None
    phone_number: str | None = None
    hire_date: datetime | None = None
    is_active: bool = True

class TenantEmployeeCreate(TenantEmployeeBase):
    password_hash: str
    pass

class TenantEmployeeRead(TenantEmployeeBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
