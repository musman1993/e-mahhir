# app/services/customer_service.py
from uuid import UUID
from app.crud.customer import get_customer_by_id, update_customer, delete_customer
from app.schemas.customer import CustomerUpdate
from app.db.session import AsyncSession
from app.utils.db import get_or_404

async def update_customer_service(
    db: AsyncSession,
    customer_id: UUID,
    customer_data: CustomerUpdate
):
    update_dict = customer_data.model_dump(exclude_unset=True)
    return await update_customer(db, customer_id, update_dict)


async def delete_customer_service(db: AsyncSession, customer_id: UUID):
    customer = await get_or_404(get_customer_by_id(db, customer_id), entity_name="Customer")
    return await delete_customer(db, customer_id)
