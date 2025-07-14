from sqlalchemy import Column, UUID, DateTime, Boolean, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class TenantCustomer(Base):
    __tablename__ = "tenant_customer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id"), nullable=True)
    is_blocked = Column(Boolean, nullable=True)
    joined_at = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())