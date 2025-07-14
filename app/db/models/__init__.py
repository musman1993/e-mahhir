# models/__init__.py

# Import all model classes from individual files
from .complaint_attachment import ComplaintAttachment
from .complaint import Complaint
from .customer_product import CustomerProduct
from .customer import Customer
from .employee import Employee
from .inventory_item import InventoryItem
from .notification import Notification
from .stock_movement import StockMovement
from .subscription_plan import SubscriptionPlan
from .tenant_customer import TenantCustomer
from .tenant_subscription import TenantSubscription
from .tenant import Tenant
from .user import User

# List all models for easy importing
__all__ = [
    "ComplaintAttachment",
    "Complaint",
    "CustomerProduct",
    "Customer",
    "Employee",
    "InventoryItem",
    "Notification",
    "StockMovement",
    "SubscriptionPlan",
    "TenantCustomer",
    "TenantSubscription",
    "Tenant",
    "User",
]
