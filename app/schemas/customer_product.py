from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID
from enum import Enum

class CustomerProductStatus(str, Enum):
    received = "received"
    in_repair = "in_repair"
    ready = "ready"
    delivered = "delivered"

class CustomerProductBase(BaseModel):
    brand: str
    model: str
    serial_number: str
    color: Optional[str] = None
    description: Optional[str] = None

class CustomerProductCreate(CustomerProductBase):
    customer_id: UUID
    received_date: datetime
    estimated_delivery_date: datetime

class CustomerProductUpdate(BaseModel):
    status: Optional[CustomerProductStatus] = None
    estimated_delivery_date: Optional[datetime] = None
    description: Optional[str] = None

class CustomerProductOut(CustomerProductBase):
    id: UUID
    tenant_id: UUID
    customer_id: UUID
    qr_code: Optional[str] = None
    status: CustomerProductStatus
    received_date: datetime
    estimated_delivery_date: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True