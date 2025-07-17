from sqlalchemy import Column, String, Boolean, DateTime, Text, Integer, DECIMAL
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.db.base import Base
import uuid
from sqlalchemy.sql import func

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plan"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plan_name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    monthly_price = Column(DECIMAL(10, 2), nullable=False)
    annual_price = Column(DECIMAL(10, 2), nullable=True)
    features = Column(JSONB, nullable=True)
    max_employees = Column(Integer, nullable=True)
    max_products = Column(Integer, nullable=True)
    is_active = Column(Boolean, nullable=False, server_default="true")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)