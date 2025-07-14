from sqlalchemy import Column, String, Boolean, UUID, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM
from app.db.base import Base
import uuid

customer_product_status = ENUM(
    'received',
    'in_repair',
    'ready',
    'delivered',
    name='customer_product_status',
    # create_type=False
)

class CustomerProduct(Base):
    __tablename__ = "customer_product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id"), nullable=True)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)
    serial_number = Column(String, nullable=True)
    qr_code = Column(String, nullable=True)
    color = Column(String, nullable=True)
    description = Column(String, nullable=True)
    received_date = Column(DateTime(timezone=True), nullable=True)
    estimated_delivery_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(customer_product_status, server_default='received')
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