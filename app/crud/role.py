# # app/crud/role.py
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select
# from uuid import UUID

# async def create_role(db: AsyncSession, role_data: dict):
#     db_role = Role(**role_data)
#     db.add(db_role)
#     await db.commit()
#     await db.refresh(db_role)
#     return db_role

# async def get_role_by_id(db: AsyncSession, role_id: UUID):
#     result = await db.execute(select(Role).where(Role.id == role_id))
#     return result.scalars().first()

# async def get_all_roles(db: AsyncSession):
#     result = await db.execute(select(Role))
#     return result.scalars().all()


# async def get_roles_by_tenant(db: AsyncSession, tenant_id: UUID, skip: int = 0, limit: int = 100):
#     result = await db.execute(select(Role).where(Role.tenant_id == tenant_id).offset(skip).limit(limit))
#     return result.scalars().all()

# async def update_role(db: AsyncSession, role_id: UUID, update_data: dict):
#     db_role = await get_role_by_id(db, role_id)
#     if db_role:
#         for key, value in update_data.items():
#             setattr(db_role, key, value)
#         await db.commit()
#         await db.refresh(db_role)
#     return db_role

# async def delete_role(db: AsyncSession, role_id: UUID):
#     db_role = await get_role_by_id(db, role_id)
#     if db_role:
#         await db.delete(db_role)
#         await db.commit()
#     return db_role