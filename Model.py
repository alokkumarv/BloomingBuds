from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import UUID,String,ForeignKey,DateTime,Boolean
import uuid
from enum import Enum
from sqlalchemy import Enum as SQLEnum
from datetime import datetime
class Base(DeclarativeBase):
    pass


class UserRole(Enum):
    SUPER_ADMIN = "super_admin"
    TENANT_ADMIN = "tenant_admin"
    MANAGER = "manager"
    STAFF = "staff"
    CUSTOMER = "customer"


class Tenant(Base):
    __tablename__="tenant"
    id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    Name : Mapped[str] = mapped_column(String(20))
    Status : Mapped[bool] = mapped_column(Boolean,default=True)
    Eamil : Mapped[str] = mapped_column(String(20))
    Phone : Mapped[str] = mapped_column(String(20))
    Address : Mapped[str] = mapped_column(String(20))
    Country : Mapped[str] = mapped_column(String(20))

class User(Base):
    __tablename__='user'
    id :Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    Email : Mapped[str] = mapped_column(String(20))
    PasswordHash: Mapped[str] = mapped_column(String(20))
    FirstName: Mapped[str] = mapped_column(String(20))
    LastName: Mapped[str] = mapped_column(String(20))
    Phone: Mapped[str] = mapped_column(String(20))
    Status: Mapped[str] = mapped_column(String(20))
    IsEmailVarified: Mapped[str] = mapped_column(String(20))
    CreatedAt: Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)
    UpdatedAt: Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)
    LastLoginAt: Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)


class Role(Base):
    __tablename__ = "role"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    Name:  Mapped[UserRole] = mapped_column(SQLEnum(name="user_role"),nullable=False)



class UserTenant(Base):
    __tablename__ = "user_tenant"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id"),
        primary_key=True
    )

    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenant.id"),
        primary_key=True
    )

    role: Mapped[Role] = mapped_column(
        SQLEnum(UserRole),name="user_role",
        nullable=False
    )