# # app/schemas/__init__.py
# from pydantic import BaseModel, EmailStr, Field, validator
# from typing import Optional, List, Union
# from datetime import datetime, date
# from uuid import UUID
# from enum import Enum

# # --------------------------
# # Common Base Schemas
# # --------------------------
# class BaseSchema(BaseModel):
#     class Config:
#         orm_mode = True
#         arbitrary_types_allowed = True

# class TimestampSchema(BaseSchema):
#     created_at: datetime
#     updated_at: datetime

# class SoftDeleteSchema(TimestampSchema):
#     soft_delete_flag: bool

# # --------------------------
# # Enum Schemas
# # --------------------------
# class TenantSubscriptionStatus(str, Enum):
#     active = "active"
#     expired = "expired"
#     cancelled = "cancelled"
#     trial = "trial"
#     suspended = "suspended"

# class CustomerProductStatus(str, Enum):
#     received = "received"
#     in_repair = "in_repair"
#     ready = "ready"
#     delivered = "delivered"

# class ComplaintPriority(str, Enum):
#     low = "low"
#     medium = "medium"
#     high = "high"

# class ComplaintStatus(str, Enum):
#     open = "open"
#     in_progress = "in_progress"
#     resolved = "resolved"
#     closed = "closed"

# class StockMovementType(str, Enum):
#     add = "add"
#     remove = "remove"
#     transfer = "transfer"

# class NotificationStatus(str, Enum):
#     pending = "pending"
#     sent = "sent"
#     failed = "failed"

# class NotificationChannel(str, Enum):
#     email = "email"
#     sms = "sms"
#     whatsapp = "whatsapp"

# # --------------------------
# # Auth & User Schemas
# # --------------------------
# class Token(BaseSchema):
#     access_token: str
#     token_type: str

# class TokenData(BaseSchema):
#     email: Optional[str] = None
#     tenant_id: Optional[UUID] = None

# class UserBase(BaseSchema):
#     email: EmailStr
#     phone: Optional[str] = None
#     display_name: Optional[str] = None

# class UserCreate(UserBase):
#     password: str

#     @validator('password')
#     def validate_password(cls, v):
#         if len(v) < 8:
#             raise ValueError("Password must be at least 8 characters")
#         return v

# class UserUpdate(UserBase):
#     password: Optional[str] = None
#     is_active: Optional[bool] = None

# class UserInDB(UserBase, SoftDeleteSchema):
#     id: UUID
#     is_active: bool
#     default_tenant_id: Optional[UUID] = None
#     last_login: Optional[datetime] = None

# # --------------------------
# # Tenant & Subscription Schemas
# # --------------------------
# class TenantBase(BaseSchema):
#     name: str
#     domain: Optional[str] = None
#     is_active: bool = True

# class TenantCreate(TenantBase):
#     pass

# class TenantUpdate(TenantBase):
#     pass

# class TenantInDB(TenantBase, SoftDeleteSchema):
#     id: UUID

# class SubscriptionPlanBase(BaseSchema):
#     name: str
#     description: Optional[str] = None
#     monthly_price: Optional[float] = None
#     yearly_price: Optional[float] = None
#     max_users: Optional[int] = None
#     max_inventory_items: Optional[int] = None
#     max_customer_products: Optional[int] = None
#     max_notifications_per_month: Optional[int] = None
#     is_active: bool = True

# class SubscriptionPlanCreate(SubscriptionPlanBase):
#     pass

# class SubscriptionPlanInDB(SubscriptionPlanBase, TimestampSchema):
#     id: UUID

# class TenantSubscriptionBase(BaseSchema):
#     tenant_id: UUID
#     subscription_plan_id: UUID
#     start_date: datetime
#     end_date: Optional[datetime] = None
#     status: TenantSubscriptionStatus = TenantSubscriptionStatus.active

# class TenantSubscriptionCreate(TenantSubscriptionBase):
#     pass

# class TenantSubscriptionInDB(TenantSubscriptionBase, TimestampSchema):
#     id: UUID

# # --------------------------
# # Role & Tenant User Schemas
# # --------------------------
# class RoleBase(BaseSchema):
#     name: str
#     description: Optional[str] = None
#     is_system_role: bool = False

# class RoleCreate(RoleBase):
#     tenant_id: UUID

# class RoleUpdate(RoleBase):
#     pass

# class RoleInDB(RoleBase, SoftDeleteSchema):
#     id: UUID
#     tenant_id: UUID

# class TenantUserBase(BaseSchema):
#     tenant_id: UUID
#     user_id: UUID
#     role_id: UUID
#     is_active: bool = True

# class TenantUserCreate(TenantUserBase):
#     pass

# class TenantUserInDB(TenantUserBase, TimestampSchema):
#     id: UUID

# # --------------------------
# # Employee Schemas
# # --------------------------
# class EmployeeBase(BaseSchema):
#     employee_code: Optional[str] = None
#     department: Optional[str] = None
#     designation: Optional[str] = None
#     location: Optional[str] = None
#     joining_date: Optional[date] = None
#     is_active: bool = True

# class EmployeeCreate(EmployeeBase):
#     tenant_id: UUID
#     user_id: UUID

# class EmployeeUpdate(EmployeeBase):
#     pass

# class EmployeeInDB(EmployeeBase, SoftDeleteSchema):
#     id: UUID
#     tenant_id: UUID
#     user_id: UUID

# # --------------------------
# # Customer Schemas
# # --------------------------
# class CustomerBase(BaseSchema):
#     preferred_language: Optional[str] = None
#     notes: Optional[str] = None

# class CustomerCreate(CustomerBase):
#     user_id: UUID

# class CustomerUpdate(CustomerBase):
#     pass

# class CustomerInDB(CustomerBase, SoftDeleteSchema):
#     id: UUID
#     user_id: UUID

# class TenantCustomerBase(BaseSchema):
#     is_blocked: bool = False

# class TenantCustomerCreate(TenantCustomerBase):
#     tenant_id: UUID
#     customer_id: UUID

# class TenantCustomerInDB(TenantCustomerBase):
#     id: UUID
#     tenant_id: UUID
#     customer_id: UUID
#     joined_at: datetime
#     updated_at: datetime

# # --------------------------
# # Customer Product Schemas
# # --------------------------
# class CustomerProductBase(BaseSchema):
#     brand: str
#     model: str
#     serial_number: str
#     qr_code: Optional[str] = None
#     color: Optional[str] = None
#     description: Optional[str] = None
#     received_date: datetime
#     estimated_delivery_date: Optional[datetime] = None
#     status: CustomerProductStatus = CustomerProductStatus.received

# class CustomerProductCreate(CustomerProductBase):
#     customer_id: UUID
#     tenant_id: UUID

# class CustomerProductUpdate(CustomerProductBase):
#     pass

# class CustomerProductInDB(CustomerProductBase, SoftDeleteSchema):
#     id: UUID
#     customer_id: UUID
#     tenant_id: UUID

# # --------------------------
# # Inventory Schemas
# # --------------------------
# class InventoryItemBase(BaseSchema):
#     sku: str
#     name: str
#     description: Optional[str] = None
#     category: Optional[str] = None
#     quantity: int = 0
#     unit: Optional[str] = None
#     location: Optional[str] = None
#     qr_code: Optional[str] = None
#     status: Optional[str] = None
#     is_returnable: bool = False
#     is_damaged: bool = False
#     is_disposed: bool = False

# class InventoryItemCreate(InventoryItemBase):
#     tenant_id: UUID

# class InventoryItemUpdate(InventoryItemBase):
#     pass

# class InventoryItemInDB(InventoryItemBase, SoftDeleteSchema):
#     id: UUID
#     tenant_id: UUID

# # --------------------------
# # Stock Movement Schemas
# # --------------------------
# class StockMovementBase(BaseSchema):
#     movement_type: StockMovementType = StockMovementType.add
#     quantity: int
#     from_location: Optional[str] = None
#     to_location: Optional[str] = None
#     approved_at: Optional[datetime] = None

# class StockMovementCreate(StockMovementBase):
#     tenant_id: UUID
#     inventory_item_id: UUID
#     requested_by_employee_id: UUID
#     approved_by_employee_id: Optional[UUID] = None

# class StockMovementUpdate(StockMovementBase):
#     pass

# class StockMovementInDB(StockMovementBase, SoftDeleteSchema):
#     id: UUID
#     tenant_id: UUID
#     inventory_item_id: UUID
#     requested_by_employee_id: UUID
#     approved_by_employee_id: Optional[UUID] = None

# # --------------------------
# # Complaint Schemas
# # --------------------------
# class ComplaintBase(BaseSchema):
#     category: str
#     priority: ComplaintPriority = ComplaintPriority.medium
#     status: ComplaintStatus = ComplaintStatus.open
#     description: str
#     resolution_notes: Optional[str] = None
#     feedback_rating: Optional[int] = Field(None, ge=1, le=5)
#     feedback_comment: Optional[str] = None
#     closed_at: Optional[datetime] = None

# class ComplaintCreate(ComplaintBase):
#     tenant_id: UUID
#     customer_product_id: UUID
#     submitted_by_user_id: UUID
#     assigned_employee_id: Optional[UUID] = None

# class ComplaintUpdate(ComplaintBase):
#     pass

# class ComplaintInDB(ComplaintBase, SoftDeleteSchema):
#     id: UUID
#     tenant_id: UUID
#     customer_product_id: UUID
#     submitted_by_user_id: UUID
#     assigned_employee_id: Optional[UUID] = None

# class ComplaintAttachmentBase(BaseSchema):
#     file_url: str
#     file_type: str

# class ComplaintAttachmentCreate(ComplaintAttachmentBase):
#     complaint_id: UUID
#     uploaded_by_user_id: UUID

# class ComplaintAttachmentInDB(ComplaintAttachmentBase):
#     id: UUID
#     complaint_id: UUID
#     uploaded_by_user_id: UUID
#     uploaded_at: datetime

# # --------------------------
# # Notification Schemas
# # --------------------------
# class NotificationBase(BaseSchema):
#     channel: NotificationChannel
#     template_name: str
#     payload: str
#     status: NotificationStatus = NotificationStatus.pending
#     error_message: Optional[str] = None
#     sent_at: Optional[datetime] = None

# class NotificationCreate(NotificationBase):
#     tenant_id: UUID
#     user_id: UUID

# class NotificationUpdate(NotificationBase):
#     pass

# class NotificationInDB(NotificationBase):
#     id: UUID
#     tenant_id: UUID
#     user_id: UUID
#     created_at: datetime

# # --------------------------
# # Response Schemas (for relationships)
# # --------------------------
# class UserWithTenants(UserInDB):
#     tenants: List[TenantUserInDB] = []

# class TenantWithUsers(TenantInDB):
#     users: List[TenantUserInDB] = []

# class RoleWithUsers(RoleInDB):
#     users: List[TenantUserInDB] = []

# class CustomerWithProducts(CustomerInDB):
#     products: List[CustomerProductInDB] = []

# class ComplaintWithAttachments(ComplaintInDB):
#     attachments: List[ComplaintAttachmentInDB] = []

# class InventoryItemWithMovements(InventoryItemInDB):
#     movements: List[StockMovementInDB] = []