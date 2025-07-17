from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class SuperAdminBase(BaseModel):
    email: EmailStr
    name: str | None = None

class SuperAdminCreate(SuperAdminBase):
    password_hash: str | None = None
    pass
class SuperAdminRegister(BaseModel):
    email: EmailStr
    password: str
    name: str | None = None

class SuperAdminLogin(BaseModel):
    email: EmailStr
    password: str

class SuperAdminRead(SuperAdminBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
