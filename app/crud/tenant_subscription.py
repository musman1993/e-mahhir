from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.tenant_subscription import TenantSubscription
from app.schemas.tenant_subscription import TenantSubscriptionCreate, TenantSubscriptionRead

async def create_tenant_subscription(db: AsyncSession, subscription_in: TenantSubscriptionCreate) -> TenantSubscription:
    db_subscription = TenantSubscription(**subscription_in)
    db.add(db_subscription)
    await db.commit()
    await db.refresh(db_subscription)
    return db_subscription

async def get_tenant_subscription(db: AsyncSession, subscription_id: UUID) -> TenantSubscription | None:
    result = await db.execute(select(TenantSubscription).where(TenantSubscription.id == subscription_id))
    return result.scalars().first()

async def get_tenant_subscriptions(db: AsyncSession) -> list[TenantSubscription]:
    result = await db.execute(select(TenantSubscription))
    return result.scalars().all()

async def update_tenant_subscription(db: AsyncSession, subscription_id: UUID, subscription_in: TenantSubscriptionCreate) -> TenantSubscription | None:
    await db.execute(update(TenantSubscription).where(TenantSubscription.id == subscription_id).values(**subscription_in))
    await db.commit()
    return await get_tenant_subscription(db, subscription_id)

async def delete_tenant_subscription(db: AsyncSession, subscription_id: UUID) -> None:
    await db.execute(delete(TenantSubscription).where(TenantSubscription.id == subscription_id))
    await db.commit()
