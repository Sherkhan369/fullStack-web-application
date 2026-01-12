from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class TimestampMixin(SQLModel):
    """Mixin class providing created_at and updated_at timestamp fields."""

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"comment": "Creation timestamp"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"comment": "Last update timestamp"},
    )

    def __setattr__(self, name, value):
        """Automatically update updated_at when any field is modified."""
        # Skip updating updated_at for internal SQLAlchemy attributes
        if name != "updated_at" and not name.startswith('_'):
            super().__setattr__("updated_at", datetime.utcnow())
        super().__setattr__(name, value)


class IDMixin(SQLModel):
    """Mixin class providing UUID primary key field."""

    id: Optional[UUID] = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs={"comment": "Unique identifier"},
    )