from asyncio import Task
from datetime import datetime
from typing import Optional

from pydantic import EmailStr, validator
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel

from src.models.base import IDMixin, TimestampMixin


class UserBase(SQLModel):
    """Base user model with common fields."""

    email: EmailStr = Field(
        index=True,
        unique=True,
        description="User's email address for login",
        sa_column_kwargs={"comment": "User email address"},
    )
    is_active: bool = Field(
        default=True,
        description="Account status",
        sa_column_kwargs={"comment": "Whether account is active"},
    )


class UserCreate(UserBase):
    """Schema for creating a new user."""

    password: str = Field(
        min_length=8,
        description="User password (minimum 8 characters)",
        sa_column_kwargs={"comment": "Hashed password"},
    )

    @validator("password")
    def password_strength(cls, v):
        """Validate password strength."""
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v


class UserUpdate(SQLModel):
    """Schema for updating user information."""

    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=8)


class User(UserBase, IDMixin, TimestampMixin, table=True):
    """User model for database storage."""

    password_hash: str = Field(
        description="Securely hashed password",
        sa_column_kwargs={"comment": "Hashed password using bcrypt"},
    )

    # Relationships
    tasks: list["Task"] = Relationship(back_populates="user")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class UserRead(UserBase, IDMixin, TimestampMixin):
    """Schema for reading user data (excludes password)."""

    pass


class UserLogin(SQLModel):
    """Schema for user login."""

    email: EmailStr
    password: str