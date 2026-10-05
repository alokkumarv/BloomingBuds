-- DROP TABLE "user_profile";
-- DROP TABLE "tenant";
-- DROP TABLE "role";
-- DROP TABLE "user_tenant";


CREATE EXTENSION if not exists pgcrypto;


CREATE TYPE roles as ENUM (
    'super_admin'
    'tenant_admin'
    'tenant_manager'
    'tenant_staff'
    'customer'
); 


CREATE TABLE user_profile (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
    "Email" VARCHAR(100) NOT NULL UNIQUE,
    "Password" VARCHAR(255) NOT NULL,
    "FirstName" VARCHAR(40) NOT NULL,
    "LastName" VARCHAR(40) NOT NULL,
    "Phone" VARCHAR(40),
    "Status" VARCHAR(40) NOT NULL DEFAULT 'Active',
    "IsEmailVarified" BOOLEAN NOT NULL DEFAULT FALSE,
    "CreatedAt" TIMESTAMP NOT NULL,
    "UpdatedAt" TIMESTAMP NOT NULL,
    "LastLoginAt" TIMESTAMP
);

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE tenant (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    "Name" VARCHAR(40) NOT NULL,
    "Status" BOOLEAN NOT NULL DEFAULT TRUE,
    "Email" VARCHAR(100) NOT NULL,
    "Phone" VARCHAR(40),
    "Address" VARCHAR(100),
    "Country" VARCHAR(40)
);

CREATE TABLE role (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_role roles NOT NULL UNIQUE
);

CREATE TABLE user_tenant (
    user_id UUID NOT NULL,
    tenant_id UUID NOT NULL,
    role UUID NOT NULL,

    PRIMARY KEY (user_id, tenant_id, role),

    FOREIGN KEY (user_id) REFERENCES user_profile(id) ON DELETE CASCADE,
    FOREIGN KEY (tenant_id) REFERENCES tenant(id) ON DELETE CASCADE,
    FOREIGN KEY (role) REFERENCES role(id)
);
