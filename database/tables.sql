DROP TABLE "user";
DROP TABLE "tenant";
DROP TABLE "role";
DROP TABLE "user_tenant";


CREATE TABLE "user" (
    id UUID PRIMARY KEY,
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

CREATE TABLE tenant (
    id UUID PRIMARY KEY,
    "Name" VARCHAR(40) NOT NULL,
    "Status" BOOLEAN NOT NULL DEFAULT TRUE,
    "Email" VARCHAR(100) NOT NULL,
    "Phone" VARCHAR(40),
    "Address" VARCHAR(100),
    "Country" VARCHAR(40)
);

CREATE TABLE role (
    id UUID PRIMARY KEY,
    user_role VARCHAR(200) NOT NULL UNIQUE
);

CREATE TABLE user_tenant (
    user_id UUID NOT NULL,
    tenant_id UUID NOT NULL,
    role UUID NOT NULL,

    PRIMARY KEY (user_id, tenant_id, role),

    FOREIGN KEY (user_id) REFERENCES "user"(id),
    FOREIGN KEY (tenant_id) REFERENCES tenant(id),
    FOREIGN KEY (role) REFERENCES role(id)
);
