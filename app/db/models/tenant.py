# app/db/models/tenant.py
from sqlalchemy import Column, String, Boolean, UUID, DateTime, text, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Tenant(Base):
    __tablename__ = "tenant"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=True)
    domain = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=True)
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
    created_by = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        nullable=True
    )