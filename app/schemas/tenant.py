from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TenantBase(BaseModel):
    app_user_id: UUID
    tenant_name: str
    business_type: str | None = None
    address: str | None = None
    phone_number: str | None = None
    email: str | None = None
    website: str | None = None
    is_active: bool = True
    setup_completed: bool = False

class TenantCreate(TenantBase):
    pass

class TenantRead(TenantBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
