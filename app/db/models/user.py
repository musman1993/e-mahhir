# app/db/models/user.py
from sqlalchemy import Column, String, Boolean, UUID, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

user_role = ENUM(
    'super-admin',
    'admin',
    'manager',
    'employee',
    'customer',
    name='user_role'
)


class User(Base):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    password_hash = Column(String, nullable=True)
    display_name = Column(String, nullable=True)
    default_tenant_id = Column(
        UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True
    )
    is_active = Column(Boolean, nullable=True)
    last_login = Column(DateTime(timezone=True), nullable=True)
    otp_code = Column(String, nullable=True)
    otp_expiry = Column(DateTime(timezone=True), nullable=True)
    role = Column(user_role, server_default='customer')
    invited_by = Column(UUID(as_uuid=True), nullable=True)
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
    customer = relationship("Customer", back_populates="user", uselist=False)
    
