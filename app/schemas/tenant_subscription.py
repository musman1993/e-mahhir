from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

class SubscriptionStatusEnum(str, Enum):
    active = "active"
    expired = "expired"
    cancelled = "cancelled"

class TenantSubscriptionBase(BaseModel):
    app_user_id: UUID
    subscription_plan_id: UUID
    start_date: datetime
    end_date: datetime | None = None
    status: SubscriptionStatusEnum = SubscriptionStatusEnum.ACTIVE
    auto_renew: bool = False
    last_payment_date: datetime | None = None
    next_payment_date: datetime | None = None

class TenantSubscriptionCreate(TenantSubscriptionBase):
    pass

class TenantSubscriptionRead(TenantSubscriptionBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
