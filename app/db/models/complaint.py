from sqlalchemy import (
    Column,
    String,
    DateTime,
    Text,
    ForeignKey,
    Enum as SQLEnum,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
from sqlalchemy.sql import func
import enum


class ComplaintStatusEnum(enum.Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"

class ComplaintPriorityEnum(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Complaint(Base):
    __tablename__ = "complaint"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=False)
    app_customer_id = Column(
        UUID(as_uuid=True), ForeignKey("app_customer.id"), nullable=False
    )
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(SQLEnum(ComplaintStatusEnum), nullable=False, server_default="open")
    priority = Column(SQLEnum(ComplaintPriorityEnum), nullable=True)
    assigned_to_employee_id = Column(
        UUID(as_uuid=True), ForeignKey("tenant_employee.id"), nullable=True
    )
    resolution_notes = Column(Text, nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    closed_at = Column(DateTime(timezone=True), nullable=True)
    soft_delete_flag = Column(Boolean, nullable=True)
