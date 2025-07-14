from sqlalchemy import Column, String, Boolean, UUID, DateTime, Integer, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class InventoryItem(Base):
    __tablename__ = "inventory_item"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    sku = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)
    quantity = Column(Integer, nullable=True)
    unit = Column(String, nullable=True)
    location = Column(String, nullable=True)
    qr_code = Column(String, nullable=True)
    status = Column(String, nullable=True)
    is_returnable = Column(Boolean, nullable=True)
    is_damaged = Column(Boolean, nullable=True)
    is_disposed = Column(Boolean, nullable=True)
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