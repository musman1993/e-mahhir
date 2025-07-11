from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from uuid import UUID

class EmployeeBase(BaseModel):
    employee_code: str
    department: str
    designation: str
    location: str
    joining_date: date

class EmployeeCreate(EmployeeBase):
    user_id: UUID
    tenant_id: UUID

class EmployeeUpdate(BaseModel):
    employee_code: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    location: Optional[str] = None
    is_active: Optional[bool] = None

class EmployeeOut(EmployeeBase):
    id: UUID
    tenant_id: UUID
    user_id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True