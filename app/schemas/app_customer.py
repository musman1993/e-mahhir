from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class AppCustomerBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    phone_number: str | None = None
    address: str | None = None
    is_active: bool = True

class AppCustomerCreate(AppCustomerBase):
    password_hash: str
    pass

class AppCustomerRead(AppCustomerBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
