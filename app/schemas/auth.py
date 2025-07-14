from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str | None = None
    tenant_id: UUID | None = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    tenant_id: UUID | None = None

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    display_name: str
    phone: str | None = None
    role: str
    tenant_id: UUID | None = None

class VerifyOTP(BaseModel):
    email: EmailStr
    otp: str = Field(..., min_length=6, max_length=6)

class ResetPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordConfirm(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8)