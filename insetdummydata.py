from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from Model import (
    Tenant,
    User,
    Role,
    UserTenant,
)

from database import DATABASE_URL


engine = create_engine(
    DATABASE_URL,
    echo=True
)


def insert_data():

    # =========================================================
    # TENANTS
    # =========================================================

    tenant_data = [
        {
                    "Name": "BloomingBuds",
                    "Status": True,
                    "Eamil": "admin@bloomingbuds.com",
                    "Phone": "7995289130",
                    "Address": "Hyderabad",
                    "Country": "India",
        },
        {
            "Name": "Acme Technologies",
            "Status": True,
            "Eamil": "admin@acmetech.com",
            "Phone": "9876543210",
            "Address": "Hyderabad",
            "Country": "India",
        },
        {
            "Name": "Bluewave Solutions",
            "Status": True,
            "Eamil": "contact@bluewave.com",
            "Phone": "9876543211",
            "Address": "Bangalore",
            "Country": "India",
        },
        {
            "Name": "Greenfield Labs",
            "Status": True,
            "Eamil": "hello@greenfield.com",
            "Phone": "9876543212",
            "Address": "Chennai",
            "Country": "India",
        },
        {
            "Name": "Nova Systems",
            "Status": True,
            "Eamil": "admin@novasystems.com",
            "Phone": "9876543213",
            "Address": "Pune",
            "Country": "India",
        },
        {
            "Name": "Vertex Solutions",
            "Status": True,
            "Eamil": "info@vertexsolutions.com",
            "Phone": "9876543214",
            "Address": "Mumbai",
            "Country": "India",
        },
        {
            "Name": "Sunrise Digital",
            "Status": True,
            "Eamil": "contact@sunrisedigital.com",
            "Phone": "9876543215",
            "Address": "Delhi",
            "Country": "India",
        },
        {
            "Name": "Cloudnine Software",
            "Status": True,
            "Eamil": "support@cloudnine.com",
            "Phone": "9876543216",
            "Address": "Kolkata",
            "Country": "India",
        },
        {
            "Name": "Techbridge India",
            "Status": True,
            "Eamil": "admin@techbridge.com",
            "Phone": "9876543217",
            "Address": "Noida",
            "Country": "India",
        },
        {
            "Name": "Prime Analytics",
            "Status": True,
            "Eamil": "info@primeanalytics.com",
            "Phone": "9876543218",
            "Address": "Ahmedabad",
            "Country": "India",
        },
        {
            "Name": "Orbit Innovations",
            "Status": True,
            "Eamil": "hello@orbitinnovations.com",
            "Phone": "9876543219",
            "Address": "Kochi",
            "Country": "India",
        },
    ]


    # =========================================================
    # USERS
    # =========================================================

    user_data = [
        {
            "Email": "alok@gmail.com",
            "PasswordHash": "super_Admin",
            "FirstName": "Alok",
            "LastName": "Verma",
            "Phone": "7995289130",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "rahul.sharma@example.com",
            "PasswordHash": "hashed_password_001",
            "FirstName": "Rahul",
            "LastName": "Sharma",
            "Phone": "9876500001",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "priya.reddy@example.com",
            "PasswordHash": "hashed_password_002",
            "FirstName": "Priya",
            "LastName": "Reddy",
            "Phone": "9876500002",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "arjun.patel@example.com",
            "PasswordHash": "hashed_password_003",
            "FirstName": "Arjun",
            "LastName": "Patel",
            "Phone": "9876500003",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "sneha.nair@example.com",
            "PasswordHash": "hashed_password_004",
            "FirstName": "Sneha",
            "LastName": "Nair",
            "Phone": "9876500004",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "vikram.singh@example.com",
            "PasswordHash": "hashed_password_005",
            "FirstName": "Vikram",
            "LastName": "Singh",
            "Phone": "9876500005",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "ananya.rao@example.com",
            "PasswordHash": "hashed_password_006",
            "FirstName": "Ananya",
            "LastName": "Rao",
            "Phone": "9876500006",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "karthik.reddy@example.com",
            "PasswordHash": "hashed_password_007",
            "FirstName": "Karthik",
            "LastName": "Reddy",
            "Phone": "9876500007",
            "Status": "Active",
            "IsEmailVarified": True,
        },
        {
            "Email": "meera.iyer@example.com",
            "PasswordHash": "hashed_password_008",
            "FirstName": "Meera",
            "LastName": "Iyer",
            "Phone": "9876500008",
            "Status": "Inactive",
            "IsEmailVarified": True,
        },
        {
            "Email": "rohit.verma@example.com",
            "PasswordHash": "hashed_password_009",
            "FirstName": "Rohit",
            "LastName": "Verma",
            "Phone": "9876500009",
            "Status": "Active",
            "IsEmailVarified": False,
        },
        {
            "Email": "divya.menon@example.com",
            "PasswordHash": "hashed_password_010",
            "FirstName": "Divya",
            "LastName": "Menon",
            "Phone": "9876500010",
            "Status": "Active",
            "IsEmailVarified": True,
        },
    ]


    # =========================================================
    # USER -> TENANT -> ROLE MAPPING
    # =========================================================

    # Role is now stored as a string here.
    # Later we find the corresponding Role row
    # and store its UUID in UserTenant.role.

    user_tenant_data = [
        {
            "user_email": "alok@gmail.com",
            "tenant_email": "admin@bloomingbuds.com",
            "role": "super_admin",
        },

        # Acme Technologies
        {
            "user_email": "rahul.sharma@example.com",
            "tenant_email": "admin@acmetech.com",
            "role": "tenant_admin",
        },
        {
            "user_email": "priya.reddy@example.com",
            "tenant_email": "admin@acmetech.com",
            "role": "manager",
        },
        {
            "user_email": "arjun.patel@example.com",
            "tenant_email": "admin@acmetech.com",
            "role": "staff",
        },

        # Bluewave Solutions
        {
            "user_email": "sneha.nair@example.com",
            "tenant_email": "contact@bluewave.com",
            "role": "tenant_admin",
        },
        {
            "user_email": "vikram.singh@example.com",
            "tenant_email": "contact@bluewave.com",
            "role": "manager",
        },
        {
            "user_email": "ananya.rao@example.com",
            "tenant_email": "contact@bluewave.com",
            "role": "staff",
        },

        # Greenfield Labs
        {
            "user_email": "karthik.reddy@example.com",
            "tenant_email": "hello@greenfield.com",
            "role": "tenant_admin",
        },
        {
            "user_email": "meera.iyer@example.com",
            "tenant_email": "hello@greenfield.com",
            "role": "staff",
        },

        # Nova Systems
        {
            "user_email": "rohit.verma@example.com",
            "tenant_email": "admin@novasystems.com",
            "role": "tenant_admin",
        },
        {
            "user_email": "divya.menon@example.com",
            "tenant_email": "admin@novasystems.com",
            "role": "customer",
        },
    ]


    # =========================================================
    # DATABASE TRANSACTION
    # =========================================================

    with Session(engine) as session:

        try:

            # =====================================================
            # 1. INSERT / GET ROLES
            # =====================================================

            role_names = [
                "super_admin",
                "tenant_admin",
                "manager",
                "staff",
                "customer",
            ]

            roles = {}

            roles_added = 0

            for role_name in role_names:

                existing_role = session.scalar(
                    select(Role).where(
                        Role.user_role == role_name
                    )
                )

                if existing_role:

                    role = existing_role

                else:

                    role = Role(
                        user_role=role_name
                    )

                    session.add(role)

                    roles_added += 1

                roles[role_name] = role


            # =====================================================
            # 2. INSERT / GET TENANTS
            # =====================================================

            tenants = {}

            tenants_added = 0

            for data in tenant_data:

                existing_tenant = session.scalar(
                    select(Tenant).where(
                        Tenant.Eamil == data["Eamil"]
                    )
                )

                if existing_tenant:

                    tenant = existing_tenant

                else:

                    tenant = Tenant(**data)

                    session.add(tenant)

                    tenants_added += 1

                tenants[data["Eamil"]] = tenant


            # =====================================================
            # 3. INSERT / GET USERS
            # =====================================================

            users = {}

            users_added = 0

            for data in user_data:

                existing_user = session.scalar(
                    select(User).where(
                        User.Email == data["Email"]
                    )
                )

                if existing_user:

                    user = existing_user

                else:

                    user = User(**data)

                    session.add(user)

                    users_added += 1

                users[data["Email"]] = user


            # =====================================================
            # FLUSH
            # =====================================================

            # Generate UUIDs for newly-created rows.

            session.flush()


            # =====================================================
            # 4. INSERT USER -> TENANT -> ROLE RELATIONSHIPS
            # =====================================================

            user_tenants_added = 0

            for data in user_tenant_data:

                user = users[data["user_email"]]

                tenant = tenants[data["tenant_email"]]

                role = roles[data["role"]]


                # Check whether this user already belongs
                # to this tenant.

                existing_mapping = session.scalar(
                    select(UserTenant).where(
                        UserTenant.user_id == user.id,
                        UserTenant.tenant_id == tenant.id,
                    )
                )


                if existing_mapping:

                    # Update role if the mapping already exists.

                    existing_mapping.role = role.id

                else:

                    user_tenant = UserTenant(
                        user_id=user.id,
                        tenant_id=tenant.id,
                        role=role.id,
                    )

                    session.add(user_tenant)

                    user_tenants_added += 1


            # =====================================================
            # COMMIT
            # =====================================================

            session.commit()


            # =====================================================
            # SUCCESS
            # =====================================================

            print()
            print("==========================================")
            print("       SEED DATA INSERTED SUCCESSFULLY")
            print("==========================================")
            print(f"Tenants added       : {tenants_added}")
            print(f"Users added         : {users_added}")
            print(f"Roles added         : {roles_added}")
            print(f"User-Tenants added  : {user_tenants_added}")
            print("==========================================")
            print()


        except Exception as e:

            session.rollback()

            print()
            print("==========================================")
            print("             INSERT FAILED")
            print("==========================================")
            print(e)
            print("==========================================")
            print()


if __name__ == "__main__":
    insert_data()