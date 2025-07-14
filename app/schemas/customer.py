# app/schemas/customer.py

from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class CustomerBase(BaseModel):
    user_id: Optional[UUID] = None
    preferred_language: Optional[str] = None
    notes: Optional[str] = None
    soft_delete_flag: Optional[bool] = None

class CustomerCreate(CustomerBase):
    # all fields optional via inheritance
    pass

class CustomerUpdate(BaseModel):
    user_id: Optional[UUID] = None
    preferred_language: Optional[str] = None
    notes: Optional[str] = None
    soft_delete_flag: Optional[bool] = None

class CustomerRead(CustomerBase):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
