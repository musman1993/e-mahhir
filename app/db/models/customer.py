from sqlalchemy import Column, String, Boolean, UUID, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    preferred_language = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  # ✅ default on INSERT
        onupdate=func.now(),  # ✅ updates automatically on UPDATE
        nullable=False,
    )
    soft_delete_flag = Column(Boolean, nullable=True)
    
    user = relationship("User", back_populates="customer")

    tenant_customers = relationship("TenantCustomer", back_populates="customer")