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
