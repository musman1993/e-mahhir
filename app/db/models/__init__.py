# models/__init__.py

# Import all model classes from individual files
from .superadmin import SuperAdmin
from .role import Role
from .app_user import AppUser
from .app_customer import AppCustomer
from .tenant import Tenant
from .tenant_employee import TenantEmployee
from .tenant_customer import TenantCustomer
from .inventory_product import InventoryProduct
from .stock_movement import StockMovement
from .complaint import Complaint
from .notification import Notification
from .customer_product import CustomerProduct
from .subscription_plan import SubscriptionPlan
from .tenant_subscription import TenantSubscription

# List all models for easy importing
__all__ = [
    "SuperAdmin",
    "Role",
    "AppUser",
    "AppCustomer",
    "Tenant",
    "TenantEmployee",
    "TenantCustomer",
    "InventoryProduct",
    "StockMovement",
    "Complaint",
    "Notification",
    "CustomerProduct",
    "SubscriptionPlan",
    "TenantSubscription",
]
