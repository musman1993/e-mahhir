from sqlalchemy import Column, UUID, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM
from app.db.base import Base
import uuid

tenant_subscription_status = ENUM(
    'active',
    'expired',
    'cancelled',
    'trial',
    'suspended',
    name='tenant_subscription_status',
    # create_type=False
)

class TenantSubscription(Base):
    __tablename__ = "tenant_subscription"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    subscription_plan_id = Column(UUID(as_uuid=True), ForeignKey("subscription_plan.id"), nullable=True)
    start_date = Column(DateTime(timezone=True), nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(tenant_subscription_status, server_default='active')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())