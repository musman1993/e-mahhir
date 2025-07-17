from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class RoleBase(BaseModel):
    role_name: str
    description: str | None = None

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
