from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class InventoryItemBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    category: str
    quantity: int = 0
    unit: str
    location: str
    is_returnable: bool = False

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemUpdate(BaseModel):
    sku: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    location: Optional[str] = None
    is_returnable: Optional[bool] = None
    is_damaged: Optional[bool] = None
    is_disposed: Optional[bool] = None

class InventoryItemOut(InventoryItemBase):
    id: UUID
    tenant_id: UUID
    qr_code: Optional[str] = None
    status: Optional[str] = None
    is_damaged: bool = False
    is_disposed: bool = False
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True