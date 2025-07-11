from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID
from enum import Enum

class ComplaintPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class ComplaintStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"

class ComplaintBase(BaseModel):
    customer_product_id: UUID
    category: str
    description: str
    priority: ComplaintPriority = ComplaintPriority.medium

class ComplaintCreate(ComplaintBase):
    pass

class ComplaintUpdate(BaseModel):
    category: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[ComplaintPriority] = None
    status: Optional[ComplaintStatus] = None
    assigned_employee_id: Optional[UUID] = None
    resolution_notes: Optional[str] = None

class ComplaintOut(ComplaintBase):
    id: UUID
    tenant_id: UUID
    status: ComplaintStatus
    submitted_by_user_id: UUID
    assigned_employee_id: Optional[UUID] = None
    resolution_notes: Optional[str] = None
    feedback_rating: Optional[int] = None
    feedback_comment: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    closed_at: Optional[datetime] = None

    class Config:
        from_attributes = True