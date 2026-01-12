from datetime import datetime
from typing import Optional, Dict, Any

from sqlalchemy import JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, SQLModel

from src.models.base import IDMixin, TimestampMixin


class AuditLogBase(SQLModel):
    """Base audit log model with common fields."""

    action: str = Field(description="Type of action performed")
    resource_type: str = Field(description="Type of resource accessed")
    ip_address: Optional[str] = Field(default=None, description="IP address of the request")
    endpoint: Optional[str] = Field(default=None, description="API endpoint accessed")
    success: bool = Field(default=True, description="Whether the action was successful")
    details: Optional[Dict[str, Any]] = Field(
        default=None,
        sa_type=JSON,
        nullable=True
    )


class AuditLog(AuditLogBase, IDMixin, TimestampMixin, table=True):
    """Audit log model for tracking security events."""

    user_id: Optional[str] = Field(
        default=None,
        description="ID of the user performing the action",
        sa_column_kwargs={"comment": "User ID for the audit event"}
    )
    resource_id: Optional[str] = Field(
        default=None,
        description="ID of the resource accessed",
        sa_column_kwargs={"comment": "Resource ID for the audit event"}
    )

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class AuditLogCreate(AuditLogBase):
    """Schema for creating audit logs."""

    user_id: Optional[str] = None
    resource_id: Optional[str] = None


class AuditLogRead(AuditLogBase, IDMixin, TimestampMixin):
    """Schema for reading audit logs."""

    user_id: Optional[str] = None
    resource_id: Optional[str] = None