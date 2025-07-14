from sqlalchemy import Column, String, Boolean, UUID, DateTime, Integer, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM
from app.db.base import Base
import uuid

complaint_priority = ENUM(
    'low',
    'medium',
    'high',
    name='complaint_priority',
    # create_type=False
)

complaint_status = ENUM(
    'open',
    'in_progress',
    'resolved',
    'closed',
    name='complaint_status',
    # create_type=False
)

class Complaint(Base):
    __tablename__ = "complaint"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    customer_product_id = Column(UUID(as_uuid=True), ForeignKey("customer_product.id"), nullable=True)
    submitted_by_user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    assigned_employee_id = Column(UUID(as_uuid=True), ForeignKey("employee.id"), nullable=True)
    category = Column(String, nullable=True)
    priority = Column(complaint_priority, server_default='medium')
    status = Column(complaint_status, server_default='open')
    description = Column(String, nullable=True)
    resolution_notes = Column(String, nullable=True)
    feedback_rating = Column(Integer, nullable=True)
    feedback_comment = Column(String, nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  # ✅ default on INSERT
        onupdate=func.now(),  # ✅ updates automatically on UPDATE
        nullable=False,
    )
    closed_at = Column(DateTime(timezone=True), nullable=True)
    soft_delete_flag = Column(Boolean, nullable=True)