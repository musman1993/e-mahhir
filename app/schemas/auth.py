
from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Any


class UserTypeEnum(str, Enum):
    app_user = "app_user"
    app_customer = "app_customer"
    tenant_employee = "tenant_employee"

class AuthLogin(BaseModel):
    email: EmailStr
    password: str
    user_type: UserTypeEnum

class AuthRegister(BaseModel):
    email: EmailStr
    password: str
    user_type: UserTypeEnum
    full_name: str | None = None
    phone_number: str | None = None
    address: str | None = None  # Only for app_customer
    tenant_id: str | None = None # Only for tenant_employee

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    # user: Any | None = None
