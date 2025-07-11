from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID
from enum import Enum

class NotificationChannel(str, Enum):
    email = "email"
    sms = "sms"
    whatsapp = "whatsapp"

class NotificationStatus(str, Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

class NotificationBase(BaseModel):
    user_id: UUID
    channel: NotificationChannel
    template_name: str

class NotificationCreate(NotificationBase):
    payload: dict

class NotificationOut(NotificationBase):
    id: UUID
    tenant_id: UUID
    payload: dict
    status: NotificationStatus
    error_message: Optional[str] = None
    sent_at: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True