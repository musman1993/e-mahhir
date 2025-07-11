-- Create 3 subscription plans
INSERT INTO "subscription_plan" 
    ("name", "description", "monthly_price", "yearly_price", 
     "max_users", "max_inventory_items", "max_customer_products",
     "max_notifications_per_month", "is_active", "created_at", "updated_at")
VALUES
    ('Basic Plan', 'Basic subscription', 50, 500, 10, 100, 50, 1000, true, NOW(), NOW()),
    ('Pro Plan', 'Professional subscription', 200, 2000, 50, 1000, 500, 10000, true, NOW(), NOW()),
    ('Enterprise Plan', 'Enterprise subscription', 500, 5000, 200, 5000, 2000, 50000, true, NOW(), NOW());

-- Create 3 tenants
INSERT INTO "tenant" 
    ("name", "domain", "is_active", "created_at", "updated_at")
VALUES
    ('Tenant One', 'tenant1.example.com', true, NOW(), NOW()),
    ('Tenant Two', 'tenant2.example.com', true, NOW(), NOW()),
    ('Tenant Three', 'tenant3.example.com', true, NOW(), NOW());

-- Get tenant IDs
WITH tenants AS (
    SELECT id, name FROM tenant
)
SELECT * FROM tenants;

-- For clarity, let’s generate and use fixed UUIDs for foreign keys.

-- Create 3 users (one admin per tenant)
INSERT INTO "user" 
    (id, email, phone, password_hash, display_name, is_active, created_at, updated_at)
VALUES
    ('00000000-0000-0000-0000-000000000001', 'admin1@tenant1.com', '1234567890', 'hashedpwd1', 'Tenant One Admin', true, NOW(), NOW()),
    ('00000000-0000-0000-0000-000000000002', 'admin2@tenant2.com', '2234567890', 'hashedpwd2', 'Tenant Two Admin', true, NOW(), NOW()),
    ('00000000-0000-0000-0000-000000000003', 'admin3@tenant3.com', '3234567890', 'hashedpwd3', 'Tenant Three Admin', true, NOW(), NOW());

-- Create roles
INSERT INTO "role"
    (id, tenant_id, name, description, is_system_role, created_at, updated_at)
VALUES
    ('10000000-0000-0000-0000-000000000001', (SELECT id FROM tenant WHERE name = 'Tenant One'), 'Admin', 'Tenant One Admin role', true, NOW(), NOW()),
    ('10000000-0000-0000-0000-000000000002', (SELECT id FROM tenant WHERE name = 'Tenant Two'), 'Admin', 'Tenant Two Admin role', true, NOW(), NOW()),
    ('10000000-0000-0000-0000-000000000003', (SELECT id FROM tenant WHERE name = 'Tenant Three'), 'Admin', 'Tenant Three Admin role', true, NOW(), NOW());

-- Assign users to tenants
INSERT INTO "tenant_user"
    (tenant_id, user_id, role_id, joined_at, is_active, created_at, updated_at)
VALUES
    ((SELECT id FROM tenant WHERE name = 'Tenant One'), '00000000-0000-0000-0000-000000000001', '10000000-0000-0000-0000-000000000001', NOW(), true, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Two'), '00000000-0000-0000-0000-000000000002', '10000000-0000-0000-0000-000000000002', NOW(), true, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Three'), '00000000-0000-0000-0000-000000000003', '10000000-0000-0000-0000-000000000003', NOW(), true, NOW(), NOW());

-- Create 1 employee per tenant
INSERT INTO "employee"
    (tenant_id, user_id, employee_code, department, designation, location, joining_date, is_active, created_at, updated_at)
VALUES
    ((SELECT id FROM tenant WHERE name = 'Tenant One'), '00000000-0000-0000-0000-000000000001', 'EMP001', 'Sales', 'Manager', 'City A', '2024-01-10', true, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Two'), '00000000-0000-0000-0000-000000000002', 'EMP002', 'Support', 'Executive', 'City B', '2024-02-15', true, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Three'), '00000000-0000-0000-0000-000000000003', 'EMP003', 'IT', 'Engineer', 'City C', '2024-03-20', true, NOW(), NOW());

-- Create 1 customer per tenant
INSERT INTO "customer"
    (id, user_id, preferred_language, notes, created_at, updated_at)
VALUES
    ('c1aaaaaa-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', 'en', 'Important customer for Tenant One', NOW(), NOW()),
    ('c1aaaaaa-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000002', 'fr', 'VIP customer for Tenant Two', NOW(), NOW()),
    ('c1aaaaaa-0000-0000-0000-000000000003', '00000000-0000-0000-0000-000000000003', 'es', 'Regular customer for Tenant Three', NOW(), NOW());

-- Map customers to tenants
INSERT INTO "tenant_customer"
    (tenant_id, customer_id, is_blocked, joined_at, updated_at)
VALUES
    ((SELECT id FROM tenant WHERE name = 'Tenant One'), 'c1aaaaaa-0000-0000-0000-000000000001', false, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Two'), 'c1aaaaaa-0000-0000-0000-000000000002', false, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Three'), 'c1aaaaaa-0000-0000-0000-000000000003', false, NOW(), NOW());

-- Create a customer product for each tenant
INSERT INTO "customer_product"
    (customer_id, tenant_id, brand, model, serial_number, qr_code, color, description, received_date, estimated_delivery_date, created_at, updated_at)
VALUES
    ('c1aaaaaa-0000-0000-0000-000000000001', (SELECT id FROM tenant WHERE name = 'Tenant One'), 'BrandX', 'ModelA', 'SN-001', 'QR001', 'Red', 'Product for Tenant One', NOW(), NOW() + INTERVAL '10 days', NOW(), NOW()),
    ('c1aaaaaa-0000-0000-0000-000000000002', (SELECT id FROM tenant WHERE name = 'Tenant Two'), 'BrandY', 'ModelB', 'SN-002', 'QR002', 'Blue', 'Product for Tenant Two', NOW(), NOW() + INTERVAL '15 days', NOW(), NOW()),
    ('c1aaaaaa-0000-0000-0000-000000000003', (SELECT id FROM tenant WHERE name = 'Tenant Three'), 'BrandZ', 'ModelC', 'SN-003', 'QR003', 'Green', 'Product for Tenant Three', NOW(), NOW() + INTERVAL '20 days', NOW(), NOW());

-- Create inventory items for each tenant
INSERT INTO "inventory_item"
    (tenant_id, sku, name, description, category, quantity, unit, location, qr_code, status, is_returnable, is_damaged, is_disposed, created_at, updated_at)
VALUES
    ((SELECT id FROM tenant WHERE name = 'Tenant One'), 'SKU-001', 'Part A', 'Part for repairs', 'Electronics', 50, 'pcs', 'Warehouse A', 'QRINV001', 'Available', true, false, false, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Two'), 'SKU-002', 'Part B', 'Part for repairs', 'Mechanical', 30, 'pcs', 'Warehouse B', 'QRINV002', 'Available', true, false, false, NOW(), NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Three'), 'SKU-003', 'Part C', 'Part for repairs', 'Electrical', 20, 'pcs', 'Warehouse C', 'QRINV003', 'Available', true, false, false, NOW(), NOW());

-- Create a complaint for each tenant
INSERT INTO "complaint"
    (tenant_id, customer_product_id, submitted_by_user_id, assigned_employee_id, category, description, created_at, updated_at)
VALUES
    (
        (SELECT id FROM tenant WHERE name = 'Tenant One'),
        (SELECT id FROM customer_product WHERE tenant_id = (SELECT id FROM tenant WHERE name = 'Tenant One')),
        '00000000-0000-0000-0000-000000000001',
        (SELECT id FROM employee WHERE tenant_id = (SELECT id FROM tenant WHERE name = 'Tenant One')),
        'Service',
        'Complaint about product from Tenant One',
        NOW(), NOW()
    ),
    (
        (SELECT id FROM tenant WHERE name = 'Tenant Two'),
        (SELECT id FROM customer_product WHERE tenant_id = (SELECT id FROM tenant WHERE name = 'Tenant Two')),
        '00000000-0000-0000-0000-000000000002',
        (SELECT id FROM employee WHERE tenant_id = (SELECT id FROM tenant WHERE name = 'Tenant Two')),
        'Warranty',
        'Complaint about product from Tenant Two',
        NOW(), NOW()
    ),
    (
        (SELECT id FROM tenant WHERE name = 'Tenant Three'),
        (SELECT id FROM customer_product WHERE tenant_id = (SELECT id FROM tenant WHERE name = 'Tenant Three')),
        '00000000-0000-0000-0000-000000000003',
        (SELECT id FROM employee WHERE tenant_id = (SELECT id FROM tenant WHERE name = 'Tenant Three')),
        'Repair',
        'Complaint about product from Tenant Three',
        NOW(), NOW()
    );

-- Create a notification for each tenant
INSERT INTO "notification"
    (tenant_id, user_id, channel, template_name, payload, created_at)
VALUES
    ((SELECT id FROM tenant WHERE name = 'Tenant One'), '00000000-0000-0000-0000-000000000001', 'email', 'Welcome Template', '{"message":"Welcome to Tenant One"}', NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Two'), '00000000-0000-0000-0000-000000000002', 'sms', 'Alert Template', '{"message":"Alert for Tenant Two"}', NOW()),
    ((SELECT id FROM tenant WHERE name = 'Tenant Three'), '00000000-0000-0000-0000-000000000003', 'whatsapp', 'Notification Template', '{"message":"Hello from Tenant Three"}', NOW());
