from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import (
    decode_access_token,
    get_password_hash,
    verify_password,
    create_access_token,
)
from app.schemas.auth import (
    AuthRegister,
    AuthLogin,
    AuthResponse,
    UserTypeEnum,
)
from app.crud.app_user import create_app_user, get_app_user_by_id, get_app_user
from app.crud.app_customer import create_app_customer, get_app_customer_by_id, get_app_customer
from app.crud.tenant_employee import create_tenant_employee, get_tenant_employee_by_id, get_tenant_employee
from app.crud.tenant_customer import create_tenant_customer
from app.crud.tenant import get_tenant

async def register_user(db: AsyncSession, data: AuthRegister):
    hashed_password = get_password_hash(data.password)
    if data.user_type == UserTypeEnum.app_user:
        existing_user = await get_app_user(db, data.email)
        if existing_user:
            raise HTTPException(
                status_code=400, detail="Email already registered as app_user"
            )
        user_in = data.dict()
        user_in["password_hash"] = hashed_password
        user_in.pop("password")
        user_in.pop("tenant_id")
        user_in.pop("user_type")
        user_in.pop("address")
        user = await create_app_user(db, user_in)
        user_dict = user.__dict__.copy()
        user_dict.pop("password_hash", None)
        return user_dict

    elif data.user_type == UserTypeEnum.app_customer:
        existing_customer = await get_app_customer(db, data.email)
        if existing_customer:
            raise HTTPException(
                status_code=400, detail="Email already registered as app_customer"
            )
        customer_in = data.dict()
        customer_in["password_hash"] = hashed_password
        customer_in.pop("password")
        customer_in.pop("tenant_id")
        customer_in.pop("user_type")
        customer = await create_app_customer(db, customer_in)
        tenant_id = getattr(data, "tenant_id", None)
        if tenant_id:
            tenant = await get_tenant(db, tenant_id)
            if not tenant:
                raise HTTPException(status_code=404, detail="Tenant not found")
            customer_in["tenant_id"] = tenant_id
            tenant_customer = await create_tenant_customer(db, customer_in)
            print(f"Tenant Customer created: {tenant_customer}")
        customer_dict = customer.__dict__.copy()
        customer_dict.pop("password_hash", None)
        return customer_dict

    elif data.user_type == UserTypeEnum.tenant_employee:
        existing_employee = await get_tenant_employee(db, data.email)
        if existing_employee:
            raise HTTPException(
                status_code=400, detail="Email already registered as tenant_employee"
            )
        if not data.tenant_id:
            raise HTTPException(
                status_code=400, detail="tenant_id is required for tenant_employee"
            )
        tenant = await get_tenant(db, data.tenant_id)
        if not tenant:
            raise HTTPException(status_code=404, detail="Tenant not found")
        employee_in = data.dict()
        employee_in["password_hash"] = hashed_password
        employee_in.pop("password")
        employee_in.pop("user_type")
        employee_in.pop("address")
        employee = await create_tenant_employee(db, employee_in)
        employee_dict = employee.__dict__.copy()
        employee_dict.pop("password_hash", None)
        return employee_dict

    else:
        raise HTTPException(status_code=400, detail="Invalid user_type")


async def login_user(db: AsyncSession, data: AuthLogin):
    user = None
    if data.user_type == UserTypeEnum.app_user:
        user = await get_app_user(db, data.email)
    elif data.user_type == UserTypeEnum.app_customer:
        user = await get_app_customer(db, data.email)
    elif data.user_type == UserTypeEnum.tenant_employee:
        user = await get_tenant_employee(db, data.email)
    else:
        raise HTTPException(status_code=400, detail="Invalid user_type")

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong Password"
        )

    access_token = create_access_token(
        {"sub": str(user.id), "user_type": data.user_type}
    )
    return AuthResponse(access_token=access_token)


async def get_current_user_from_token(db: AsyncSession, token: str):
    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        user_type = payload.get("user_type")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )
        # Convert user_type to enum if needed
        if user_type == UserTypeEnum.app_user:
            user = await get_app_user_by_id(db, user_id)
        elif user_type == UserTypeEnum.app_customer:
            user = await get_app_customer_by_id(db, user_id)
        elif user_type == UserTypeEnum.tenant_employee:
            user = await get_tenant_employee_by_id(db, user_id)
        else:
            raise HTTPException(status_code=400, detail="Invalid user_type")
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

