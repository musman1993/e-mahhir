# app/services/auth_service.py
from fastapi import HTTPException, status
from app.core.security import (
    create_access_token,
    verify_password,
    generate_otp,
    decode_access_token,
)
from app.crud.user import get_user_by_email, create_user, set_user_otp, get_user_by_id
from app.crud.tenant import get_tenant_by_id
from app.schemas.auth import UserLogin, UserRegister, VerifyOTP
from app.db.session import AsyncSession
from app.core.config import settings
from app.core.email_utils import send_email
from datetime import datetime, timezone, timedelta
from app.utils.db import get_or_404

async def authenticate_user(db: AsyncSession, login_data: UserLogin):
    user = await get_user_by_email(db, login_data.email)
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            {"sub": str(user.id)}, access_token_expires
        ),
        "token_type": "bearer",
    }

async def decode_token_get_user(db: AsyncSession, token: str):
    payload = decode_access_token(token)
    user_id = payload["sub"]
    return await get_user_by_id(db, user_id)

async def register_user(db: AsyncSession, user_data: UserRegister):
    # Normalize role for comparison
    role = user_data.role

    # Check rules based on role
    if role in ["manager", "employee"]:
        if user_data.tenant_id is None:
            raise HTTPException(
                status_code=400,
                detail=f"tenant_id is required for role '{role}'."
            )
        # Check if tenant exists
        tenant = await get_tenant_by_id(db, user_data.tenant_id)
        if tenant is None:
            raise HTTPException(
                status_code=404,
                detail="Tenant not found."
            )

    elif role == "super-admin":
        # Ignore tenant_id for these roles
        user_data.tenant_id = None

    # Check if email already exists
    existing_user = await get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create user
    user_dict = user_data.model_dump()
    user = await create_user(db, user_dict)
    return user

async def send_otp(db: AsyncSession, email: str):
    user = await get_or_404(get_user_by_email(db), entity_name="User")

    otp = generate_otp()
    await set_user_otp(db, user.id, otp)
    # Compose OTP email
    subject = "Your OTP Code for E-Mahhir"
    body = f"Hello {user.display_name},\n\nYour OTP code is: {otp}\n\nIt is valid for 10 minutes."

    await send_email(
        subject=subject,
        recipient_email=email,
        body=body,
    )

    return {"message": "OTP sent successfully"}

async def verify_otp(db: AsyncSession, otp_data: VerifyOTP):
    user = await get_or_404(get_user_by_email(db), entity_name="User")

    if user.otp_code != otp_data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    utc_now = datetime.now(timezone.utc)
    if user.otp_expiry < utc_now:
        raise HTTPException(status_code=400, detail="OTP expired")

    return {"message": "OTP verified successfully"}
