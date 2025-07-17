from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from uuid import UUID
from app.db.models.complaint import Complaint
from app.schemas.complaint import ComplaintCreate, ComplaintRead

async def create_complaint(db: AsyncSession, complaint_in: ComplaintCreate) -> Complaint:
    db_complaint = Complaint(**complaint_in)
    db.add(db_complaint)
    await db.commit()
    await db.refresh(db_complaint)
    return db_complaint

async def get_complaint(db: AsyncSession, complaint_id: UUID) -> Complaint | None:
    result = await db.execute(select(Complaint).where(Complaint.id == complaint_id))
    return result.scalars().first()

async def get_complaints(db: AsyncSession) -> list[Complaint]:
    result = await db.execute(select(Complaint))
    return result.scalars().all()

async def update_complaint(db: AsyncSession, complaint_id: UUID, complaint_in: ComplaintCreate) -> Complaint | None:
    await db.execute(update(Complaint).where(Complaint.id == complaint_id).values(**complaint_in))
    await db.commit()
    return await get_complaint(db, complaint_id)

async def delete_complaint(db: AsyncSession, complaint_id: UUID) -> None:
    await db.execute(delete(Complaint).where(Complaint.id == complaint_id))
    await db.commit()
