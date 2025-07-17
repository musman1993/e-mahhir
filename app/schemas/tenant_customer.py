
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TenantCustomerBase(BaseModel):
    tenant_id: UUID
    app_customer_id: UUID
    customer_since: datetime | None = None
    last_interaction: datetime | None = None
    notes: str | None = None

class TenantCustomerCreate(TenantCustomerBase):
    pass

class TenantCustomerRead(TenantCustomerBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
