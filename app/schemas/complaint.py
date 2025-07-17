
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

class ComplaintStatusEnum(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"

class ComplaintPriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class ComplaintBase(BaseModel):
    tenant_id: UUID
    app_customer_id: UUID
    title: str
    description: str | None = None
    status: ComplaintStatusEnum = ComplaintStatusEnum.OPEN
    priority: ComplaintPriorityEnum | None = None
    assigned_to_employee_id: UUID | None = None
    resolution_notes: str | None = None
    closed_at: datetime | None = None

class ComplaintCreate(ComplaintBase):
    pass

class ComplaintRead(ComplaintBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    soft_delete_flag: bool | None = None

    class Config:
        orm_mode = True
