from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID
from enum import Enum

class StockMovementType(str, Enum):
    add = "add"
    remove = "remove"
    transfer = "transfer"

class StockMovementBase(BaseModel):
    inventory_item_id: UUID
    movement_type: StockMovementType
    quantity: int
    to_location: str

class StockMovementCreate(StockMovementBase):
    from_location: Optional[str] = None

class StockMovementUpdate(BaseModel):
    approved_by_employee_id: Optional[UUID] = None
    approved_at: Optional[datetime] = None

class StockMovementOut(StockMovementBase):
    id: UUID
    tenant_id: UUID
    from_location: Optional[str] = None
    approved_by_employee_id: Optional[UUID] = None
    requested_by_employee_id: UUID
    approved_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True