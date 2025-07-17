from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.app_user import AppUser
from app.schemas.app_user import AppUserCreate, AppUserRead

async def create_app_user(db: AsyncSession, user_in: AppUserCreate) -> AppUser:
    db_user = AppUser(**user_in)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_app_user(db: AsyncSession, email: str) -> AppUser | None:
    result = await db.execute(select(AppUser).where(AppUser.email == email))
    return result.scalars().first()

async def get_app_user_by_id(db: AsyncSession, user_id: UUID) -> AppUser | None:
    result = await db.execute(select(AppUser).where(AppUser.id == user_id))
    return result.scalars().first()

async def get_app_users(db: AsyncSession) -> list[AppUser]:
    result = await db.execute(select(AppUser))
    return result.scalars().all()

async def update_app_user(db: AsyncSession, user_id: UUID, user_in: AppUserCreate) -> AppUser | None:
    await db.execute(update(AppUser).where(AppUser.id == user_id).values(**user_in))
    await db.commit()
    return await get_app_user(db, user_id)

async def delete_app_user(db: AsyncSession, user_id: UUID) -> None:
    await db.execute(delete(AppUser).where(AppUser.id == user_id))
    await db.commit()
