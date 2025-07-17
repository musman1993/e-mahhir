from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
from sqlalchemy.sql import func
import enum

class SubscriptionStatusEnum(enum.Enum):
    active = "active"
    expired = "expired"
    cancelled = "cancelled"

class TenantSubscription(Base):
    __tablename__ = "tenant_subscription"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    app_user_id = Column(UUID(as_uuid=True), ForeignKey("app_user.id"), nullable=False)
    subscription_plan_id = Column(UUID(as_uuid=True), ForeignKey("subscription_plan.id"), nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(SQLEnum(SubscriptionStatusEnum), nullable=False, server_default="active")
    auto_renew = Column(Boolean, nullable=False, server_default="false")
    last_payment_date = Column(DateTime(timezone=True), nullable=True)
    next_payment_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)