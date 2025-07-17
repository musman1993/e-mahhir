from sqlalchemy import Column, String, Boolean, DateTime, Text, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
from sqlalchemy.sql import func
import enum

class NotificationTypeEnum(enum.Enum):
    complaint_update = "complaint_update"
    new_order = "new_order"
    subscription_expiry = "subscription_expiry"
    other = "other"

class Notification(Base):
    __tablename__ = "notification"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    recipient_app_user_id = Column(UUID(as_uuid=True), ForeignKey("app_user.id"), nullable=True)
    recipient_app_customer_id = Column(UUID(as_uuid=True), ForeignKey("app_customer.id"), nullable=True)
    recipient_tenant_employee_id = Column(UUID(as_uuid=True), ForeignKey("tenant_employee.id"), nullable=True)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    type = Column(SQLEnum(NotificationTypeEnum), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, nullable=False, server_default="false")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)