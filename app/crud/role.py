from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.role import Role
from app.schemas.role import RoleCreate, RoleRead

async def create_role(db: AsyncSession, role_in: RoleCreate) -> Role:
    db_role = Role(**role_in)
    db.add(db_role)
    await db.commit()
    await db.refresh(db_role)
    return db_role

async def get_role(db: AsyncSession, role_id: UUID) -> Role | None:
    result = await db.execute(select(Role).where(Role.id == role_id))
    return result.scalars().first()

async def get_roles(db: AsyncSession) -> list[Role]:
    result = await db.execute(select(Role))
    return result.scalars().all()

async def update_role(db: AsyncSession, role_id: UUID, role_in: RoleCreate) -> Role | None:
    await db.execute(update(Role).where(Role.id == role_id).values(**role_in))
    await db.commit()
    return await get_role(db, role_id)

async def delete_role(db: AsyncSession, role_id: UUID) -> None:
    await db.execute(delete(Role).where(Role.id == role_id))
    await db.commit()
