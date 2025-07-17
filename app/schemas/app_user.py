from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class AppUserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    phone_number: str | None = None
    is_active: bool = True

class AppUserCreate(AppUserBase):
    password_hash: str
    pass

class AppUserRead(AppUserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
