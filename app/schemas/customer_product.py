
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from decimal import Decimal

class CustomerProductBase(BaseModel):
    app_customer_id: UUID
    tenant_id: UUID
    inventory_product_id: UUID
    purchase_date: datetime
    price_at_purchase: Decimal | None = None
    quantity: int
    warranty_expires_at: datetime | None = None
    notes: str | None = None

class CustomerProductCreate(CustomerProductBase):
    pass

class CustomerProductRead(CustomerProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
