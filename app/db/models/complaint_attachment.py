from sqlalchemy import Column, String, UUID, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class ComplaintAttachment(Base):
    __tablename__ = "complaint_attachment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    complaint_id = Column(UUID(as_uuid=True), ForeignKey("complaint.id"), nullable=True)
    file_url = Column(String, nullable=True)
    file_type = Column(String, nullable=True)
    uploaded_by_user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True)
    uploaded_at = Column(DateTime(timezone=True), nullable=True)