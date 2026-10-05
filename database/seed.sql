-- =========================================================
-- SEED DATA
-- =========================================================

-- ---------------------------------------------------------
-- Roles
-- ---------------------------------------------------------

INSERT INTO role (id, user_role)
VALUES
    (gen_random_uuid(), 'super_admin'),
    (gen_random_uuid(), 'tenant_admin'),
    (gen_random_uuid(), 'tenant_manager'),
    (gen_random_uuid(), 'tenant_staff'),
    (gen_random_uuid(), 'customer');


-- ---------------------------------------------------------
-- Tenants
-- ---------------------------------------------------------

INSERT INTO tenant
    (id, "Name", "Status", "Email", "Phone", "Address", "Country")
VALUES
    (gen_random_uuid(), 'Acme Corporation', TRUE,
     'admin@acme.com', '+91-9876543210',
     'Hitech City, Hyderabad', 'India'),

    (gen_random_uuid(), 'Globex Solutions', TRUE,
     'admin@globex.com', '+91-9876543211',
     'Banjara Hills, Hyderabad', 'India'),

    (gen_random_uuid(), 'TechNova Systems', TRUE,
     'admin@technova.com', '+91-9876543212',
     'Madhapur, Hyderabad', 'India'),

    (gen_random_uuid(), 'BlueSky Retail', TRUE,
     'admin@bluesky.com', '+91-9876543213',
     'Kukatpally, Hyderabad', 'India'),

    (gen_random_uuid(), 'GreenField Services', TRUE,
     'admin@greenfield.com', '+91-9876543214',
     'Gachibowli, Hyderabad', 'India');


-- ---------------------------------------------------------
-- Users
-- Passwords below are intentionally simple seed passwords.
-- DO NOT use these passwords in production.
-- ---------------------------------------------------------

INSERT INTO user_profile
    (
        id,
        "Email",
        "Password",
        "FirstName",
        "LastName",
        "Phone",
        "Status",
        "IsEmailVarified",
        "CreatedAt",
        "UpdatedAt",
        "LastLoginAt"
    )
VALUES

-- Super Admin
(
    gen_random_uuid(),
    'superadmin@example.com',
    crypt('SuperAdmin@123', gen_salt('bf')),
    'John',
    'Admin',
    '+91-9000000001',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

-- Tenant Admins
(
    gen_random_uuid(),
    'alice@acme.com',
    crypt('Password@123', gen_salt('bf')),
    'Alice',
    'Johnson',
    '+91-9000000002',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'bob@globex.com',
    crypt('Password@123', gen_salt('bf')),
    'Bob',
    'Williams',
    '+91-9000000003',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'charlie@technova.com',
    crypt('Password@123', gen_salt('bf')),
    'Charlie',
    'Brown',
    '+91-9000000004',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

-- Tenant Managers
(
    gen_random_uuid(),
    'david@acme.com',
    crypt('Password@123', gen_salt('bf')),
    'David',
    'Miller',
    '+91-9000000005',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'emma@globex.com',
    crypt('Password@123', gen_salt('bf')),
    'Emma',
    'Davis',
    '+91-9000000006',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'frank@technova.com',
    crypt('Password@123', gen_salt('bf')),
    'Frank',
    'Wilson',
    '+91-9000000007',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

-- Staff
(
    gen_random_uuid(),
    'grace@acme.com',
    crypt('Password@123', gen_salt('bf')),
    'Grace',
    'Taylor',
    '+91-9000000008',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'henry@acme.com',
    crypt('Password@123', gen_salt('bf')),
    'Henry',
    'Anderson',
    '+91-9000000009',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'isabella@globex.com',
    crypt('Password@123', gen_salt('bf')),
    'Isabella',
    'Thomas',
    '+91-9000000010',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'jack@technova.com',
    crypt('Password@123', gen_salt('bf')),
    'Jack',
    'Moore',
    '+91-9000000011',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

-- Customers
(
    gen_random_uuid(),
    'customer1@gmail.com',
    crypt('Customer@123', gen_salt('bf')),
    'Michael',
    'Martin',
    '+91-9000000012',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'customer2@gmail.com',
    crypt('Customer@123', gen_salt('bf')),
    'Sophia',
    'Jackson',
    '+91-9000000013',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'customer3@gmail.com',
    crypt('Customer@123', gen_salt('bf')),
    'William',
    'White',
    '+91-9000000014',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'customer4@gmail.com',
    crypt('Customer@123', gen_salt('bf')),
    'Olivia',
    'Harris',
    '+91-9000000015',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
),

(
    gen_random_uuid(),
    'customer5@gmail.com',
    crypt('Customer@123', gen_salt('bf')),
    'James',
    'Clark',
    '+91-9000000016',
    'Active',
    TRUE,
    NOW(),
    NOW(),
    NOW()
);


-- =========================================================
-- USER / TENANT / ROLE MAPPING
-- =========================================================

-- Super Admin
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT
    u.id,
    t.id,
    r.id
FROM user_profile u
CROSS JOIN tenant t
JOIN role r ON r.user_role = 'super_admin'
WHERE u."Email" = 'superadmin@example.com';


-- Acme Admin
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Acme Corporation'
JOIN role r ON r.user_role = 'tenant_admin'
WHERE u."Email" = 'alice@acme.com';


-- Globex Admin
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Globex Solutions'
JOIN role r ON r.user_role = 'tenant_admin'
WHERE u."Email" = 'bob@globex.com';


-- TechNova Admin
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'TechNova Systems'
JOIN role r ON r.user_role = 'tenant_admin'
WHERE u."Email" = 'charlie@technova.com';


-- Acme Manager
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Acme Corporation'
JOIN role r ON r.user_role = 'tenant_manager'
WHERE u."Email" = 'david@acme.com';


-- Globex Manager
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Globex Solutions'
JOIN role r ON r.user_role = 'tenant_manager'
WHERE u."Email" = 'emma@globex.com';


-- TechNova Manager
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'TechNova Systems'
JOIN role r ON r.user_role = 'tenant_manager'
WHERE u."Email" = 'frank@technova.com';


-- Acme Staff
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Acme Corporation'
JOIN role r ON r.user_role = 'tenant_staff'
WHERE u."Email" IN (
    'grace@acme.com',
    'henry@acme.com'
);


-- Globex Staff
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Globex Solutions'
JOIN role r ON r.user_role = 'tenant_staff'
WHERE u."Email" = 'isabella@globex.com';


-- TechNova Staff
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'TechNova Systems'
JOIN role r ON r.user_role = 'tenant_staff'
WHERE u."Email" = 'jack@technova.com';


-- Customers
INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Acme Corporation'
JOIN role r ON r.user_role = 'customer'
WHERE u."Email" IN (
    'customer1@gmail.com',
    'customer2@gmail.com'
);


INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'Globex Solutions'
JOIN role r ON r.user_role = 'customer'
WHERE u."Email" = 'customer3@gmail.com';


INSERT INTO user_tenant (user_id, tenant_id, role)
SELECT u.id, t.id, r.id
FROM user_profile u
JOIN tenant t ON t."Name" = 'TechNova Systems'
JOIN role r ON r.user_role = 'customer'
WHERE u."Email" IN (
    'customer4@gmail.com',
    'customer5@gmail.com'
);
