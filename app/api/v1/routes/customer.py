# # app/api/v1/routes/tenant.py
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from uuid import UUID
# from app.db.session import get_db
# from app.services.customer_service import (
#     update_customer_service,
#     delete_customer_service
# )
# from app.core.security import get_current_user
# from app.schemas.customer import CustomerUpdate, CustomerRead

# router = APIRouter()

# @router.put("/{customer_id}", response_model=CustomerRead)
# async def update_customer(
#     customer_id: UUID,
#     customer_data: CustomerUpdate,
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await update_customer_service(db, customer_id, customer_data)


# @router.delete("/{customer_id}")
# async def delete_customer(
#     customer_id: UUID,
#     db: AsyncSession = Depends(get_db),
#     # current_user: dict = Depends(get_current_user)
# ):
#     return await delete_customer_service(db, customer_id)
