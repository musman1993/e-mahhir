from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.tenant import Tenant
from app.schemas.tenant import TenantCreate, TenantRead

async def create_tenant(db: AsyncSession, tenant_in: TenantCreate) -> Tenant:
    db_tenant = Tenant(**tenant_in)
    db.add(db_tenant)
    await db.commit()
    await db.refresh(db_tenant)
    return db_tenant

async def get_tenant(db: AsyncSession, tenant_id: UUID) -> Tenant | None:
    result = await db.execute(select(Tenant).where(Tenant.id == tenant_id))
    return result.scalars().first()

async def get_tenants(db: AsyncSession) -> list[Tenant]:
    result = await db.execute(select(Tenant))
    return result.scalars().all()

async def update_tenant(db: AsyncSession, tenant_id: UUID, tenant_in: TenantCreate) -> Tenant | None:
    await db.execute(update(Tenant).where(Tenant.id == tenant_id).values(**tenant_in))
    await db.commit()
    return await get_tenant(db, tenant_id)

async def delete_tenant(db: AsyncSession, tenant_id: UUID) -> None:
    await db.execute(delete(Tenant).where(Tenant.id == tenant_id))
    await db.commit()
