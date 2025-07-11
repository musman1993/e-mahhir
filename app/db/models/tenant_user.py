from sqlalchemy import Column, UUID, DateTime, Boolean, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class TenantUser(Base):
    __tablename__ = "tenant_user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("role.id"), nullable=True)
    joined_at = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Boolean, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())