from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.tenant_employee import TenantEmployee
from app.schemas.tenant_employee import TenantEmployeeCreate, TenantEmployeeRead

async def create_tenant_employee(db: AsyncSession, employee_in: TenantEmployeeCreate) -> TenantEmployee:
    db_employee = TenantEmployee(**employee_in)
    db.add(db_employee)
    await db.commit()
    await db.refresh(db_employee)
    return db_employee

async def get_tenant_employee(db: AsyncSession, email: str) -> TenantEmployee | None:
    result = await db.execute(select(TenantEmployee).where(TenantEmployee.email == email))
    return result.scalars().first()


async def get_tenant_employee_by_id(db: AsyncSession, employee_id: UUID) -> TenantEmployee | None:
    result = await db.execute(select(TenantEmployee).where(TenantEmployee.id == employee_id))
    return result.scalars().first()


async def get_tenant_employees(db: AsyncSession) -> list[TenantEmployee]:
    result = await db.execute(select(TenantEmployee))
    return result.scalars().all()

async def update_tenant_employee(db: AsyncSession, employee_id: UUID, employee_in: TenantEmployeeCreate) -> TenantEmployee | None:
    await db.execute(update(TenantEmployee).where(TenantEmployee.id == employee_id).values(**employee_in))
    await db.commit()
    return await get_tenant_employee(db, employee_id)

async def delete_tenant_employee(db: AsyncSession, employee_id: UUID) -> None:
    await db.execute(delete(TenantEmployee).where(TenantEmployee.id == employee_id))
    await db.commit()
