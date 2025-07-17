from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from decimal import Decimal

class InventoryProductBase(BaseModel):
    tenant_id: UUID
    product_name: str
    description: str | None = None
    sku: str | None = None
    unit_price: Decimal
    current_stock: int = 0
    reorder_level: int | None = None
    supplier_info: str | None = None
    image_url: str | None = None

class InventoryProductCreate(InventoryProductBase):
    pass

class InventoryProductRead(InventoryProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
