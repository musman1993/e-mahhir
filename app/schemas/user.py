# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    display_name: str
    role: str
    phone: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    display_name: Optional[str] = None
    phone: Optional[str] = None
    role: str
    password: Optional[str] = None

class UserOut(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime
    role: str

    class Config:
        from_attributes = True
        
class UserOutInDetail(BaseModel):
    id: UUID
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    role: str
    display_name: Optional[str] = None
    default_tenant_id: Optional[UUID] = None
    is_active: Optional[bool] = None
    last_login: Optional[datetime] = None
    otp_code: Optional[str] = None
    otp_expiry: Optional[datetime] = None
    invited_by: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime
    soft_delete_flag: Optional[bool] = None

    class Config:
        from_attributes = True