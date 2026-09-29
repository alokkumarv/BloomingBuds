# Model.py

import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum


class Base(DeclarativeBase):
    pass


# class UserRole(str,Enum):
#     SUPER_ADMIN = "super_admin"
#     TENANT_ADMIN = "tenant_admin"
#     MANAGER = "manager"
#     STAFF = "staff"
#     CUSTOMER = "customer"


class Tenant(Base):
    __tablename__ = "tenant"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    Name: Mapped[str] = mapped_column(
        String(40),
        nullable=False
    )

    Status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    Eamil: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    Phone: Mapped[str] = mapped_column(
        String(40)
    )

    Address: Mapped[str] = mapped_column(
        String(100)
    )

    Country: Mapped[str] = mapped_column(
        String(40)
    )


class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    Email: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    PasswordHash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    FirstName: Mapped[str] = mapped_column(
        String(40),
        nullable=False
    )

    LastName: Mapped[str] = mapped_column(
        String(40),
        nullable=False
    )

    Phone: Mapped[str] = mapped_column(
        String(40)
    )

    Status: Mapped[str] = mapped_column(
        String(40),
        default="Active",
        nullable=False
    )

    IsEmailVarified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    CreatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    UpdatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    LastLoginAt: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )


class Role(Base):
    __tablename__ = "role"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_role: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        unique=True
    )


class UserTenant(Base):
    __tablename__ = "user_tenant"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        primary_key=True
    )

    tenant_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tenant.id"),
        primary_key=True
    )

    role: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("role.id"),
        primary_key=True
    )