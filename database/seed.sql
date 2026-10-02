-- ============================================================
-- SEED DATA
-- Tables:
--   user
--   tenant
--   role
--   user_tenant
-- ============================================================


-- ============================================================
-- 1. ROLES
-- ============================================================

INSERT INTO role (id, user_role)
VALUES
    ('10000000-0000-0000-0000-000000000001', 'Admin'),
    ('10000000-0000-0000-0000-000000000002', 'Manager'),
    ('10000000-0000-0000-0000-000000000003', 'User'),
    ('10000000-0000-0000-0000-000000000004', 'Support'),
    ('10000000-0000-0000-0000-000000000005', 'Viewer')
ON CONFLICT (id) DO NOTHING;


-- ============================================================
-- 2. TENANTS
-- ============================================================

INSERT INTO tenant
    (id, "Name", "Status", "Eamil", "Phone", "Address", "Country")
VALUES
    (
        '20000000-0000-0000-0000-000000000001',
        'Microsoft',
        TRUE,
        'contact@microsoft.com',
        '+1-425-882-8080',
        'One Microsoft Way',
        'United States'
    ),
    (
        '20000000-0000-0000-0000-000000000002',
        'Amazon',
        TRUE,
        'contact@amazon.com',
        '+1-206-266-1000',
        '410 Terry Ave N',
        'United States'
    ),
    (
        '20000000-0000-0000-0000-000000000003',
        'Google',
        TRUE,
        'contact@google.com',
        '+1-650-253-0000',
        '1600 Amphitheatre Parkway',
        'United States'
    ),
    (
        '20000000-0000-0000-0000-000000000004',
        'Acme Corporation',
        TRUE,
        'admin@acme.example',
        '+1-212-555-0100',
        '123 Business Avenue',
        'United States'
    ),
    (
        '20000000-0000-0000-0000-000000000005',
        'TechNova Solutions',
        TRUE,
        'admin@technova.example',
        '+91-40-5555-0100',
        'HITEC City',
        'India'
    )
ON CONFLICT (id) DO NOTHING;


-- ============================================================
-- 3. USERS
-- ============================================================

INSERT INTO "user"
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
    (
        '30000000-0000-0000-0000-000000000001',
        'john.smith@example.com',
        'hashed_password_1',
        'John',
        'Smith',
        '+1-202-555-0101',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000002',
        'sarah.johnson@example.com',
        'hashed_password_2',
        'Sarah',
        'Johnson',
        '+1-202-555-0102',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000003',
        'michael.brown@example.com',
        'hashed_password_3',
        'Michael',
        'Brown',
        '+1-202-555-0103',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000004',
        'emily.davis@example.com',
        'hashed_password_4',
        'Emily',
        'Davis',
        '+1-202-555-0104',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000005',
        'david.wilson@example.com',
        'hashed_password_5',
        'David',
        'Wilson',
        '+1-202-555-0105',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000006',
        'olivia.martin@example.com',
        'hashed_password_6',
        'Olivia',
        'Martin',
        '+1-202-555-0106',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000007',
        'daniel.anderson@example.com',
        'hashed_password_7',
        'Daniel',
        'Anderson',
        '+1-202-555-0107',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000008',
        'emma.thompson@example.com',
        'hashed_password_8',
        'Emma',
        'Thompson',
        '+1-202-555-0108',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000009',
        'alex.wright@example.com',
        'hashed_password_9',
        'Alex',
        'Wright',
        '+1-202-555-0109',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    ),
    (
        '30000000-0000-0000-0000-000000000010',
        'sophia.taylor@example.com',
        'hashed_password_10',
        'Sophia',
        'Taylor',
        '+1-202-555-0110',
        'Active',
        TRUE,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    )
ON CONFLICT (id) DO NOTHING;


-- ============================================================
-- 4. USER / TENANT / ROLE MAPPING
-- ============================================================

INSERT INTO user_tenant
    (user_id, tenant_id, role)
VALUES

    -- Microsoft
    (
        '30000000-0000-0000-0000-000000000001',
        '20000000-0000-0000-0000-000000000001',
        '10000000-0000-0000-0000-000000000001'
    ),
    (
        '30000000-0000-0000-0000-000000000002',
        '20000000-0000-0000-0000-000000000001',
        '10000000-0000-0000-0000-000000000002'
    ),
    (
        '30000000-0000-0000-0000-000000000003',
        '20000000-0000-0000-0000-000000000001',
        '10000000-0000-0000-0000-000000000003'
    ),

    -- Amazon
    (
        '30000000-0000-0000-0000-000000000005',
        '20000000-0000-0000-0000-000000000002',
        '10000000-0000-0000-0000-000000000001'
    ),
    (
        '30000000-0000-0000-0000-000000000006',
        '20000000-0000-0000-0000-000000000002',
        '10000000-0000-0000-0000-000000000002'
    ),
    (
        '30000000-0000-0000-0000-000000000007',
        '20000000-0000-0000-0000-000000000002',
        '10000000-0000-0000-0000-000000000003'
    ),

    -- Google
    (
        '30000000-0000-0000-0000-000000000004',
        '20000000-0000-0000-0000-000000000003',
        '10000000-0000-0000-0000-000000000001'
    ),
    (
        '30000000-0000-0000-0000-000000000009',
        '20000000-0000-0000-0000-000000000003',
        '10000000-0000-0000-0000-000000000003'
    ),

    -- Acme Corporation
    (
        '30000000-0000-0000-0000-000000000008',
        '20000000-0000-0000-0000-000000000004',
        '10000000-0000-0000-0000-000000000001'
    ),
    (
        '30000000-0000-0000-0000-000000000010',
        '20000000-0000-0000-0000-000000000004',
        '10000000-0000-0000-0000-000000000002'
    ),

    -- TechNova Solutions
    (
        '30000000-0000-0000-0000-000000000001',
        '20000000-0000-0000-0000-000000000005',
        '10000000-0000-0000-0000-000000000002'
    ),
    (
        '30000000-0000-0000-0000-000000000003',
        '20000000-0000-0000-0000-000000000005',
        '10000000-0000-0000-0000-000000000003'
    ),
    (
        '30000000-0000-0000-0000-000000000009',
        '20000000-0000-0000-0000-000000000005',
        '10000000-0000-0000-0000-000000000004'
    )

ON CONFLICT DO NOTHING;


-- ============================================================
-- VERIFY SEED DATA
-- ============================================================

SELECT * FROM role;

SELECT * FROM tenant;

SELECT * FROM "user";

SELECT * FROM user_tenant;
