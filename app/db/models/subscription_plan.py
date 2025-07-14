from sqlalchemy import Column, String, Boolean, UUID, DateTime, Numeric, Integer, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    monthly_price = Column(Numeric, nullable=True)
    yearly_price = Column(Numeric, nullable=True)
    max_users = Column(Integer, nullable=True)
    max_inventory_items = Column(Integer, nullable=True)
    max_customer_products = Column(Integer, nullable=True)
    max_notifications_per_month = Column(Integer, nullable=True)
    is_active = Column(Boolean, nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  # ✅ default on INSERT
        onupdate=func.now(),  # ✅ updates automatically on UPDATE
        nullable=False,
    )