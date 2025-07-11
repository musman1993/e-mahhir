# app/api/v1/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.auth import Token, UserLogin, UserRegister, VerifyOTP
from app.schemas.user import UserOutInDetail
from app.services.auth_service import authenticate_user, register_user, send_otp, verify_otp, decode_token_get_user

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    login_data = UserLogin(email=form_data.username, password=form_data.password)
    return await authenticate_user(db, login_data)

@router.post("/get-current-user"
             , response_model=UserOutInDetail
             )
async def get_current_user_by_token(
    token: str,
    db: AsyncSession = Depends(get_db)
):
    return await decode_token_get_user(db, token)


@router.post("/register")
async def register(
    user_data: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    return await register_user(db, user_data)

@router.post("/send-otp")
async def send_otp_code(
    email: str,
    db: AsyncSession = Depends(get_db)
):
    return await send_otp(db, email)

@router.post("/verify-otp")
async def verify_otp_code(
    otp_data: VerifyOTP,
    db: AsyncSession = Depends(get_db)
):
    return await verify_otp(db, otp_data)