# # app/db/base.py
# from sqlalchemy.orm import DeclarativeBase

# class Base(DeclarativeBase):
#     pass

# app/db/base.py
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncEngine

class Base(DeclarativeBase):
    @classmethod
    async def create_enum_types(cls, engine: AsyncEngine):
        """Create all ENUM types explicitly before table creation"""
        from app.db.models.user import user_status_enum
        from app.db.models.tenant_subscription import tenant_subscription_status
        from app.db.models.customer_product import customer_product_status
        from app.db.models.complaint import complaint_priority, complaint_status
        from app.db.models.stock_movement import stock_movement_type
        from app.db.models.notification import notification_status, notification_channel
        
        async with engine.begin() as conn:
            await conn.run_sync(user_status_enum.create)
            await conn.run_sync(tenant_subscription_status.create)
            await conn.run_sync(customer_product_status.create)
            await conn.run_sync(complaint_priority.create)
            await conn.run_sync(complaint_status.create)
            await conn.run_sync(stock_movement_type.create)
            await conn.run_sync(notification_status.create)
            await conn.run_sync(notification_channel.create)