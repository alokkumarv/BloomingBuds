
# Model.py

import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
from models.models import Base

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

    Password: Mapped[str] = mapped_column(
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
