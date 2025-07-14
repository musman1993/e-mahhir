from sqlalchemy import Column, String, Boolean, UUID, DateTime, Integer, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM
from app.db.base import Base
import uuid

stock_movement_type = ENUM(
    'add',
    'remove',
    'transfer',
    name='stock_movement_type',
    # create_type=False
)

class StockMovement(Base):
    __tablename__ = "stock_movement"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    inventory_item_id = Column(UUID(as_uuid=True), ForeignKey("inventory_item.id"), nullable=True)
    movement_type = Column(stock_movement_type, server_default='add')
    quantity = Column(Integer, nullable=True)
    from_location = Column(String, nullable=True)
    to_location = Column(String, nullable=True)
    approved_by_employee_id = Column(UUID(as_uuid=True), ForeignKey("employee.id"), nullable=True)
    requested_by_employee_id = Column(UUID(as_uuid=True), ForeignKey("employee.id"), nullable=True)
    approved_at = Column(DateTime(timezone=True), nullable=True)
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