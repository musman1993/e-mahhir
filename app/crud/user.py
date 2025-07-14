# app/crud/user.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from uuid import UUID
from app.db.models.user import User
from app.core.security import get_password_hash
from datetime import datetime, timedelta
from app.core.config import settings
from .tenant_customer import create_tenant_customer
from loguru import logger
from .customer import create_customer
from .employee import create_employee


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user_data: dict):
    hashed_password = get_password_hash(user_data["password"])

    db_user = User(
        email=user_data["email"],
        role=user_data["role"],
        password_hash=hashed_password,
        display_name=user_data["display_name"],
        phone=user_data.get("phone"),
        is_active=True,
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    role = user_data.get("role")
    tenant_id = user_data.get("tenant_id")

    if role == "customer":
        customer_data = await create_customer(db, {"user_id": db_user.id})
        logger.info("customer created.", customer_data)
        if tenant_id:
            from .tenant import get_tenant_by_id

            tenant = await get_tenant_by_id(db, tenant_id)
            if tenant:
                tenant_customer = await create_tenant_customer(
                    db, {"tenant_id": tenant_id, "customer_id": customer_data.id}
                )
                logger.info("tenant customer created.")

    if role in ["manager", "employee"]:
        employee_data = await create_employee(
            db, {"tenant_id": tenant_id, "user_id": db_user.id}
        )
        logger.info("employee created.", employee_data)

    return db_user


async def update_user(db: AsyncSession, user_id: UUID, update_data: dict):
    if "password" in update_data:
        update_data["password_hash"] = get_password_hash(update_data.pop("password"))

    stmt = update(User).where(User.id == user_id).values(**update_data)
    await db.execute(stmt)
    await db.commit()
    return await get_user_by_id(db, user_id)


async def get_all_tenant_admins_(db: AsyncSession):
    stmt = select(User).where(User.role == "admin")
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_all_users_(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


async def get_user_by_id(db: AsyncSession, user_id: UUID):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


async def set_user_otp(db: AsyncSession, user_id: UUID, otp_code: str):
    otp_expiry = datetime.utcnow() + timedelta(minutes=settings.OTP_EXPIRE_MINUTES)
    stmt = (
        update(User)
        .where(User.id == user_id)
        .values(otp_code=otp_code, otp_expiry=otp_expiry)
    )
    await db.execute(stmt)
    await db.commit()
