from sqlalchemy import Column, String, UUID, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid
from sqlalchemy.dialects.postgresql import ENUM

notification_status = ENUM(
    'pending',
    'sent',
    'failed',
    name='notification_status',
    # create_type=False
)

notification_channel = ENUM(
    'email',
    'sms',
    'whatsapp',
    name='notification_channel',
    # create_type=False
)

class Notification(Base):
    __tablename__ = "notification"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    channel = Column(notification_channel, nullable=True)
    template_name = Column(String, nullable=True)
    payload = Column(String, nullable=True)
    status = Column(notification_status, server_default='pending')
    error_message = Column(String, nullable=True)
    sent_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())