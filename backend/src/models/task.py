from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from src.models.base import IDMixin, TimestampMixin
from src.models.user import User


class TaskBase(SQLModel):
    """Base task model with common fields."""

    title: str = Field(
        min_length=1,
        max_length=200,
        description="Task title",
        sa_column_kwargs={"comment": "Task title"},
    )
    description: Optional[str] = Field(
        default=None,
        max_length=2000,
        description="Task description",
        sa_column_kwargs={"comment": "Task description (optional)"},
    )
    is_complete: bool = Field(
        default=False,
        description="Completion status",
        sa_column_kwargs={"comment": "Whether task is completed"},
    )


class TaskCreate(TaskBase):
    """Schema for creating a new task."""

    pass


class TaskUpdate(SQLModel):
    """Schema for updating task information."""

    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    is_complete: Optional[bool] = None


class Task(TaskBase, IDMixin, TimestampMixin, table=True):
    """Task model for database storage."""

    user_id: UUID = Field(
        foreign_key="user.id",
        description="Owner of the task",
        sa_column_kwargs={"comment": "User who owns this task"},
    )

    # Relationships
    user: User = Relationship(back_populates="tasks")

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class TaskRead(TaskBase, IDMixin, TimestampMixin):
    """Schema for reading task data."""

    user_id: UUID