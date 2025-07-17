# app/api/v1/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

# from app.schemas.auth import Token, UserLogin, UserRegister, VerifyOTP
from app.schemas.auth import AuthRegister, AuthLogin, AuthResponse

# from app.schemas.user import UserOutInDetail
from app.services.auth_service import (
    login_user,
    register_user,
    get_current_user_from_token,
    # send_otp,
    # verify_otp,
    # decode_token_get_user,
)
from typing import Any
from fastapi import Header, Query

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Union
from app.schemas.app_user import AppUserRead
from app.schemas.app_customer import AppCustomerRead
from app.schemas.tenant_employee import TenantEmployeeRead

router = APIRouter()
bearer_scheme = HTTPBearer()

# @router.post("/login", response_model=Token)
# async def login_for_access_token(
#     form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
# ):
#     login_data = UserLogin(email=form_data.username, password=form_data.password)
#     return await login_user(db, login_data)


@router.get(
    "/get-current-user",
    response_model=Union[AppUserRead, AppCustomerRead, TenantEmployeeRead],
)
async def get_current_user_by_token(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
):
    token = credentials.credentials
    return await get_current_user_from_token(db, token)


@router.post("/register")
async def register(user_data: AuthRegister, db: AsyncSession = Depends(get_db)):
    return await register_user(db, user_data)


@router.post("/login")
async def login(user_data: AuthLogin, db: AsyncSession = Depends(get_db)):
    return await login_user(db, user_data)


# @router.post("/send-otp")
# async def send_otp_code(email: str, db: AsyncSession = Depends(get_db)):
#     return await send_otp(db, email)


# @router.post("/verify-otp")
# async def verify_otp_code(otp_data: VerifyOTP, db: AsyncSession = Depends(get_db)):
#     return await verify_otp(db, otp_data)
