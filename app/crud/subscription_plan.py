from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.subscription_plan import SubscriptionPlan
from app.schemas.subscription_plan import SubscriptionPlanCreate, SubscriptionPlanRead

async def create_subscription_plan(db: AsyncSession, plan_in: SubscriptionPlanCreate) -> SubscriptionPlan:
    db_plan = SubscriptionPlan(**plan_in)
    db.add(db_plan)
    await db.commit()
    await db.refresh(db_plan)
    return db_plan

async def get_subscription_plan(db: AsyncSession, plan_id: UUID) -> SubscriptionPlan | None:
    result = await db.execute(select(SubscriptionPlan).where(SubscriptionPlan.id == plan_id))
    return result.scalars().first()

async def get_subscription_plans(db: AsyncSession) -> list[SubscriptionPlan]:
    result = await db.execute(select(SubscriptionPlan))
    return result.scalars().all()

async def update_subscription_plan(db: AsyncSession, plan_id: UUID, plan_in: SubscriptionPlanCreate) -> SubscriptionPlan | None:
    await db.execute(update(SubscriptionPlan).where(SubscriptionPlan.id == plan_id).values(**plan_in))
    await db.commit()
    return await get_subscription_plan(db, plan_id)

async def delete_subscription_plan(db: AsyncSession, plan_id: UUID) -> None:
    await db.execute(delete(SubscriptionPlan).where(SubscriptionPlan.id == plan_id))
    await db.commit()
