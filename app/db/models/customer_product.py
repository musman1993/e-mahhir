from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey, DECIMAL
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
from sqlalchemy.sql import func

class CustomerProduct(Base):
    __tablename__ = "customer_product"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    app_customer_id = Column(UUID(as_uuid=True), ForeignKey("app_customer.id"), nullable=False)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=False)
    inventory_product_id = Column(UUID(as_uuid=True), ForeignKey("inventory_product.id"), nullable=False)
    purchase_date = Column(DateTime(timezone=True), nullable=False)
    price_at_purchase = Column(DECIMAL(10, 2), nullable=True)
    quantity = Column(Integer, nullable=False)
    warranty_expires_at = Column(DateTime(timezone=True), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)