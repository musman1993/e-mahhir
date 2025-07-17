from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from typing import Any

class SubscriptionPlanBase(BaseModel):
    plan_name: str
    description: str | None = None
    monthly_price: Decimal
    annual_price: Decimal | None = None
    features: Any | None = None
    max_employees: int | None = None
    max_products: int | None = None
    is_active: bool = True

class SubscriptionPlanCreate(SubscriptionPlanBase):
    pass

class SubscriptionPlanRead(SubscriptionPlanBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
