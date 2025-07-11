from sqlalchemy import Column, String, Boolean, UUID, DateTime, Date, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Employee(Base):
    __tablename__ = "employee"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenant.id"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    employee_code = Column(String, nullable=True)
    department = Column(String, nullable=True)
    designation = Column(String, nullable=True)
    location = Column(String, nullable=True)
    joining_date = Column(Date, nullable=True)
    is_active = Column(Boolean, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    soft_delete_flag = Column(Boolean, nullable=True)