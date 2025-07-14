CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TYPE tenant_subscription_status AS ENUM (
  'active',
  'expired',
  'cancelled',
  'trial',
  'suspended'
);

CREATE TYPE customer_product_status AS ENUM (
  'received',
  'in_repair',
  'ready',
  'delivered'
);

CREATE TYPE complaint_priority AS ENUM (
  'low',
  'medium',
  'high'
);

CREATE TYPE complaint_status AS ENUM (
  'open',
  'in_progress',
  'resolved',
  'closed'
);

CREATE TYPE stock_movement_type AS ENUM (
  'add',
  'remove',
  'transfer'
);

CREATE TYPE notification_status AS ENUM (
  'pending',
  'sent',
  'failed'
);

CREATE TYPE notification_channel AS ENUM (
  'email',
  'sms',
  'whatsapp'
);

CREATE TABLE "tenant" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "name" text,
  "domain" text,
  "is_active" boolean,
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "subscription_plan" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "name" text,
  "description" text,
  "monthly_price" numeric,
  "yearly_price" numeric,
  "max_users" int,
  "max_inventory_items" int,
  "max_customer_products" int,
  "max_notifications_per_month" int,
  "is_active" boolean,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "tenant_subscription" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "subscription_plan_id" uuid,
  "start_date" timestamp,
  "end_date" timestamp,
  "status" tenant_subscription_status DEFAULT 'active',
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "user" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "email" text,
  "phone" text,
  "password_hash" text,
  "display_name" text,
  "default_tenant_id" uuid,
  "is_active" boolean,
  "last_login" timestamp,
  "otp_code" text,
  "otp_expiry" timestamp,
  "invited_by" uuid,
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "tenant_user" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "user_id" uuid,
  "role_id" uuid,
  "joined_at" timestamp,
  "is_active" boolean,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "role" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "name" text,
  "description" text,
  "is_system_role" boolean,
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "employee" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "user_id" uuid,
  "employee_code" text,
  "department" text,
  "designation" text,
  "location" text,
  "joining_date" date,
  "is_active" boolean,
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "customer" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "user_id" uuid,
  "preferred_language" text,
  "notes" text,
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "tenant_customer" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "customer_id" uuid,
  "is_blocked" boolean,
  "joined_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "customer_product" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "customer_id" uuid,
  "tenant_id" uuid,
  "brand" text,
  "model" text,
  "serial_number" text,
  "qr_code" text,
  "color" text,
  "description" text,
  "received_date" timestamp,
  "estimated_delivery_date" timestamp,
  "status" customer_product_status DEFAULT 'received',
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "inventory_item" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "sku" text,
  "name" text,
  "description" text,
  "category" text,
  "quantity" int,
  "unit" text,
  "location" text,
  "qr_code" text,
  "status" text,
  "is_returnable" boolean,
  "is_damaged" boolean,
  "is_disposed" boolean,
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "stock_movement" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "inventory_item_id" uuid,
  "movement_type" stock_movement_type DEFAULT 'add',
  "quantity" int,
  "from_location" text,
  "to_location" text,
  "approved_by_employee_id" uuid,
  "requested_by_employee_id" uuid,
  "approved_at" timestamp,
  "created_at" timestamp,
  "updated_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "complaint" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "customer_product_id" uuid,
  "submitted_by_user_id" uuid,
  "assigned_employee_id" uuid,
  "category" text,
  "priority" complaint_priority DEFAULT 'medium',
  "status" complaint_status DEFAULT 'open',
  "description" text,
  "resolution_notes" text,
  "feedback_rating" int,
  "feedback_comment" text,
  "created_at" timestamp,
  "updated_at" timestamp,
  "closed_at" timestamp,
  "soft_delete_flag" boolean
);

CREATE TABLE "complaint_attachment" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "complaint_id" uuid,
  "file_url" text,
  "file_type" text,
  "uploaded_by_user_id" uuid,
  "uploaded_at" timestamp
);

CREATE TABLE "notification" (
  "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  "tenant_id" uuid,
  "user_id" uuid,
  "channel" notification_channel,
  "template_name" text,
  "payload" text,
  "status" notification_status DEFAULT 'pending',
  "error_message" text,
  "sent_at" timestamp,
  "created_at" timestamp
);

ALTER TABLE "tenant_subscription" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");
ALTER TABLE "tenant_subscription" ADD FOREIGN KEY ("subscription_plan_id") REFERENCES "subscription_plan" ("id");

ALTER TABLE "user" ADD FOREIGN KEY ("default_tenant_id") REFERENCES "tenant" ("id");

ALTER TABLE "tenant_user" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");
ALTER TABLE "tenant_user" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");
ALTER TABLE "tenant_user" ADD FOREIGN KEY ("role_id") REFERENCES "role" ("id");

ALTER TABLE "role" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");

ALTER TABLE "employee" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");
ALTER TABLE "employee" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "customer" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "tenant_customer" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");
ALTER TABLE "tenant_customer" ADD FOREIGN KEY ("customer_id") REFERENCES "customer" ("id");

ALTER TABLE "customer_product" ADD FOREIGN KEY ("customer_id") REFERENCES "customer" ("id");
ALTER TABLE "customer_product" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");

ALTER TABLE "inventory_item" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");

ALTER TABLE "stock_movement" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");
ALTER TABLE "stock_movement" ADD FOREIGN KEY ("inventory_item_id") REFERENCES "inventory_item" ("id");
ALTER TABLE "stock_movement" ADD FOREIGN KEY ("approved_by_employee_id") REFERENCES "employee" ("id");
ALTER TABLE "stock_movement" ADD FOREIGN KEY ("requested_by_employee_id") REFERENCES "employee" ("id");

ALTER TABLE "complaint" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");
ALTER TABLE "complaint" ADD FOREIGN KEY ("customer_product_id") REFERENCES "customer_product" ("id");
ALTER TABLE "complaint" ADD FOREIGN KEY ("submitted_by_user_id") REFERENCES "user" ("id");
ALTER TABLE "complaint" ADD FOREIGN KEY ("assigned_employee_id") REFERENCES "employee" ("id");

ALTER TABLE "complaint_attachment" ADD FOREIGN KEY ("complaint_id") REFERENCES "complaint" ("id");
ALTER TABLE "complaint_attachment" ADD FOREIGN KEY ("uploaded_by_user_id") REFERENCES "user" ("id");

ALTER TABLE "notification" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenant" ("id");
ALTER TABLE "notification" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");
