from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.superadmin import SuperAdmin
from app.schemas.superadmin import SuperAdminCreate, SuperAdminRead, SuperAdminRegister

async def create_superadmin(db: AsyncSession, superadmin_in: SuperAdminCreate) -> SuperAdmin:
    db_superadmin = SuperAdmin(**superadmin_in)
    db.add(db_superadmin)
    await db.commit()
    await db.refresh(db_superadmin)
    return db_superadmin

async def get_superadmin_by_id(db: AsyncSession, superadmin_id: UUID) -> SuperAdmin | None:
    result = await db.execute(select(SuperAdmin).where(SuperAdmin.id == superadmin_id))
    return result.scalars().first()

async def get_superadmin_by_email(db: AsyncSession, email: UUID) -> SuperAdmin | None:
    result = await db.execute(select(SuperAdmin).where(SuperAdmin.email == email))
    return result.scalars().first()


async def get_superadmins(db: AsyncSession) -> list[SuperAdmin]:
    result = await db.execute(select(SuperAdmin))
    return result.scalars().all()

async def update_superadmin(db: AsyncSession, superadmin_id: UUID, superadmin_in: SuperAdminRegister) -> SuperAdmin | None:
    await db.execute(update(SuperAdmin).where(SuperAdmin.id == superadmin_id).values(**superadmin_in))
    await db.commit()
    return await get_superadmin_by_id(db, superadmin_id)

async def delete_superadmin(db: AsyncSession, superadmin_id: UUID) -> None:
    await db.execute(delete(SuperAdmin).where(SuperAdmin.id == superadmin_id))
    await db.commit()
