from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from uuid import UUID

class EmployeeBase(BaseModel):
    employee_code: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    location: Optional[str] = None
    joining_date: Optional[date] = None

class EmployeeCreate(BaseModel):
    user_id: Optional[UUID] = None
    tenant_id: Optional[UUID] = None
    employee_code: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    location: Optional[str] = None
    joining_date: Optional[date] = None

class EmployeeUpdate(BaseModel):
    employee_code: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    location: Optional[str] = None
    joining_date: Optional[date] = None
    is_active: Optional[bool] = None
    user_id: Optional[UUID] = None
    tenant_id: Optional[UUID] = None

class EmployeeOut(BaseModel):
    id: Optional[UUID] = None
    employee_code: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    location: Optional[str] = None
    joining_date: Optional[date] = None
    tenant_id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
