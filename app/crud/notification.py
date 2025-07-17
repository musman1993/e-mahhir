from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationRead

async def create_notification(db: AsyncSession, notification_in: NotificationCreate) -> Notification:
    db_notification = Notification(**notification_in)
    db.add(db_notification)
    await db.commit()
    await db.refresh(db_notification)
    return db_notification

async def get_notification(db: AsyncSession, notification_id: UUID) -> Notification | None:
    result = await db.execute(select(Notification).where(Notification.id == notification_id))
    return result.scalars().first()

async def get_notifications(db: AsyncSession) -> list[Notification]:
    result = await db.execute(select(Notification))
    return result.scalars().all()

async def update_notification(db: AsyncSession, notification_id: UUID, notification_in: NotificationCreate) -> Notification | None:
    await db.execute(update(Notification).where(Notification.id == notification_id).values(**notification_in))
    await db.commit()
    return await get_notification(db, notification_id)

async def delete_notification(db: AsyncSession, notification_id: UUID) -> None:
    await db.execute(delete(Notification).where(Notification.id == notification_id))
    await db.commit()
