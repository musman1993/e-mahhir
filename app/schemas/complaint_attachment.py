from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ComplaintAttachmentBase(BaseModel):
    complaint_id: UUID
    file_url: str
    file_type: str

class ComplaintAttachmentCreate(ComplaintAttachmentBase):
    pass

class ComplaintAttachmentOut(ComplaintAttachmentBase):
    id: UUID
    uploaded_by_user_id: UUID
    uploaded_at: datetime

    class Config:
        from_attributes = True