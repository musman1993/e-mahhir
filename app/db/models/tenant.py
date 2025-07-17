from sqlalchemy import Column, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
from sqlalchemy.sql import func

class Tenant(Base):
    __tablename__ = "tenant"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    app_user_id = Column(UUID(as_uuid=True), ForeignKey("app_user.id"), nullable=False)
    tenant_name = Column(String(255), nullable=False)
    business_type = Column(String(100), nullable=True)
    address = Column(Text, nullable=True)
    phone_number = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    is_active = Column(Boolean, nullable=False, server_default="true")
    setup_completed = Column(Boolean, nullable=False, server_default="false")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)