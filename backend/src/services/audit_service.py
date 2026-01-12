"""
Audit service for logging security events and access patterns.

This module provides comprehensive audit logging for security monitoring,
compliance, and troubleshooting purposes.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from src.models.audit import AuditLog


class AuditService:
    """Service for managing audit logs."""

    def __init__(self, db: Session):
        self.db = db

    def log_authentication_success(self, user_id: str, ip_address: Optional[str] = None):
        """Log successful authentication."""
        audit_log = AuditLog(
            user_id=user_id,
            action="AUTH_SUCCESS",
            resource_type="AUTHENTICATION",
            ip_address=ip_address,
            timestamp=datetime.utcnow(),
            success=True,
            details={"message": "User authenticated successfully"}
        )
        self.db.add(audit_log)
        self.db.commit()

    def log_authentication_failure(self, ip_address: Optional[str], reason: str, endpoint: str):
        """Log failed authentication attempt."""
        audit_log = AuditLog(
            action="AUTH_FAILURE",
            resource_type="AUTHENTICATION",
            ip_address=ip_address,
            endpoint=endpoint,
            timestamp=datetime.utcnow(),
            success=False,
            details={"reason": reason}
        )
        self.db.add(audit_log)
        self.db.commit()

    def log_access_denied(self, user_id: Optional[str], ip_address: Optional[str], reason: str, endpoint: str):
        """Log access denied event."""
        audit_log = AuditLog(
            user_id=user_id,
            action="ACCESS_DENIED",
            resource_type="RESOURCE",
            ip_address=ip_address,
            endpoint=endpoint,
            timestamp=datetime.utcnow(),
            success=False,
            details={"reason": reason}
        )
        self.db.add(audit_log)
        self.db.commit()

    def log_api_access(self, user_id: str, ip_address: Optional[str], method: str, endpoint: str, timestamp: Optional[datetime] = None):
        """Log API access."""
        audit_log = AuditLog(
            user_id=user_id,
            action=f"API_{method.upper()}",
            resource_type="API",
            ip_address=ip_address,
            endpoint=endpoint,
            timestamp=timestamp or datetime.utcnow(),
            success=True
        )
        self.db.add(audit_log)
        self.db.commit()

    def log_data_access(self, user_id: str, resource_type: str, resource_id: Optional[str], action: str, ip_address: Optional[str] = None):
        """Log data access."""
        audit_log = AuditLog(
            user_id=user_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            ip_address=ip_address,
            timestamp=datetime.utcnow(),
            success=True
        )
        self.db.add(audit_log)
        self.db.commit()

    def log_security_event(self, event_type: str, description: str, user_id: Optional[str] = None, ip_address: Optional[str] = None):
        """Log security-related events."""
        audit_log = AuditLog(
            user_id=user_id,
            action="SECURITY_EVENT",
            resource_type="SECURITY",
            ip_address=ip_address,
            timestamp=datetime.utcnow(),
            success=False,
            details={"event_type": event_type, "description": description}
        )
        self.db.add(audit_log)
        self.db.commit()

    def get_user_audit_trail(self, user_id: str, limit: int = 100):
        """Get audit trail for a specific user."""
        return self.db.query(AuditLog).filter(
            AuditLog.user_id == user_id
        ).order_by(AuditLog.timestamp.desc()).limit(limit).all()

    def get_failed_attempts(self, ip_address: Optional[str] = None, user_id: Optional[str] = None, hours: int = 24):
        """Get failed authentication attempts."""
        from datetime import timedelta

        cutoff_time = datetime.utcnow() - timedelta(hours=hours)

        query = self.db.query(AuditLog).filter(
            AuditLog.action.in_(['AUTH_FAILURE', 'ACCESS_DENIED']),
            AuditLog.timestamp >= cutoff_time
        )

        if ip_address:
            query = query.filter(AuditLog.ip_address == ip_address)

        if user_id:
            query = query.filter(AuditLog.user_id == user_id)

        return query.order_by(AuditLog.timestamp.desc()).all()

    def get_recent_activity(self, user_id: str, hours: int = 24):
        """Get recent activity for a user."""
        from datetime import timedelta

        cutoff_time = datetime.utcnow() - timedelta(hours=hours)

        return self.db.query(AuditLog).filter(
            AuditLog.user_id == user_id,
            AuditLog.timestamp >= cutoff_time
        ).order_by(AuditLog.timestamp.desc()).all()

    def cleanup_old_logs(self, days: int = 90):
        """Clean up audit logs older than specified days."""
        from datetime import timedelta

        cutoff_time = datetime.utcnow() - timedelta(days=days)

        deleted_count = self.db.query(AuditLog).filter(
            AuditLog.timestamp < cutoff_time
        ).delete()

        self.db.commit()
        return deleted_count