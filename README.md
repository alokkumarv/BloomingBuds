# User, Tenant & Role Mapping

This document describes the current relationship between users, tenants, and roles based on the seed data.

## User → Tenant → Role

| # | User | Email | Tenant | Role |
|---|---|---|---|---|
| 1 | Rahul Sharma | rahul.sharma@example.com | Acme Technologies | `tenant_admin` |
| 2 | Priya Reddy | priya.reddy@example.com | Acme Technologies | `manager` |
| 3 | Arjun Patel | arjun.patel@example.com | Acme Technologies | `staff` |
| 4 | Sneha Nair | sneha.nair@example.com | Bluewave Solutions | `tenant_admin` |
| 5 | Vikram Singh | vikram.singh@example.com | Bluewave Solutions | `manager` |
| 6 | Ananya Rao | ananya.rao@example.com | Bluewave Solutions | `staff` |
| 7 | Karthik Reddy | karthik.reddy@example.com | Greenfield Labs | `tenant_admin` |
| 8 | Meera Iyer | meera.iyer@example.com | Greenfield Labs | `staff` |
| 9 | Rohit Verma | rohit.verma@example.com | Nova Systems | `tenant_admin` |
| 10 | Divya Menon | divya.menon@example.com | Nova Systems | `customer` |

## Grouped by Tenant

### Acme Technologies

| User | Role |
|---|---|
| Rahul Sharma | `tenant_admin` |
| Priya Reddy | `manager` |
| Arjun Patel | `staff` |

### Bluewave Solutions

| User | Role |
|---|---|
| Sneha Nair | `tenant_admin` |
| Vikram Singh | `manager` |
| Ananya Rao | `staff` |

### Greenfield Labs

| User | Role |
|---|---|
| Karthik Reddy | `tenant_admin` |
| Meera Iyer | `staff` |

### Nova Systems

| User | Role |
|---|---|
| Rohit Verma | `tenant_admin` |
| Divya Menon | `customer` |

## Role Summary

| Role | Number of Users |
|---|---:|
| `super_admin` | 0 |
| `tenant_admin` | 4 |
| `manager` | 2 |
| `staff` | 3 |
| `customer` | 1 |
| **Total** | **10** |

## Database Relationship

```text
USER
  │
  │ user_id
  ▼
USER_TENANT
  │
  ├── tenant_id ──────► TENANT
  │
  └── role ───────────► ROLE





<!-- Only tenant admin can create a new user under his org and super admin can create a new user without any tenant -->