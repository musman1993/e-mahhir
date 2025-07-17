
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

class NotificationTypeEnum(str, Enum):
    complaint_update = "complaint_update"
    new_order = "new_order"
    subscription_expiry = "subscription_expiry"
    other = "other"

class NotificationBase(BaseModel):
    recipient_app_user_id: UUID | None = None
    recipient_app_customer_id: UUID | None = None
    recipient_tenant_employee_id: UUID | None = None
    tenant_id: UUID | None = None
    type: NotificationTypeEnum
    message: str
    is_read: bool = False

class NotificationCreate(NotificationBase):
    pass

class NotificationRead(NotificationBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
