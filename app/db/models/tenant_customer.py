from sqlalchemy import Column, UUID, DateTime, Boolean, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid
from sqlalchemy.orm import relationship

class TenantCustomer(Base):
    __tablename__ = "tenant_customer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id"), nullable=True)
    customer = relationship("Customer", back_populates="tenant_customers")
    is_blocked = Column(Boolean, default=False)
    joined_at = Column(DateTime(timezone=True), nullable=True)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  # ✅ default on INSERT
        onupdate=func.now(),  # ✅ updates automatically on UPDATE
        nullable=False,
    )