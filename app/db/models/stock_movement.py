import enum
from sqlalchemy import Column, Enum as SQLEnum, Integer, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class MovementTypeEnum(enum.Enum):
    in_ = "in"
    out = "out"
    adjustment = "adjustment"

class StockMovement(Base):
    __tablename__ = "stock_movement"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    inventory_product_id = Column(UUID(as_uuid=True), ForeignKey("inventory_product.id"), nullable=False)
    # Use SQLEnum wrapper
    movement_type = Column(
        SQLEnum(MovementTypeEnum, name="movementtypeenum"),
        nullable=False
    )
    quantity = Column(Integer, nullable=False)
    movement_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    reason = Column(Text, nullable=True)
    performed_by_employee_id = Column(UUID(as_uuid=True), ForeignKey("tenant_employee.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
