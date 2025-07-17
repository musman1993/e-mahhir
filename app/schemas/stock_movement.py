
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

class MovementTypeEnum(str, Enum):
    in_ = "in"
    out = "out"
    adjustment = "adjustment"

class StockMovementBase(BaseModel):
    inventory_product_id: UUID
    movement_type: MovementTypeEnum
    quantity: int
    movement_date: datetime | None = None
    reason: str | None = None
    performed_by_employee_id: UUID | None = None

class StockMovementCreate(StockMovementBase):
    pass

class StockMovementRead(StockMovementBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
