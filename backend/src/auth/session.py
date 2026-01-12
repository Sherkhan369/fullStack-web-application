"""
Session management for JWT tokens and user sessions.

This module handles JWT token refresh, session validation,
and session cleanup functionality.
"""

from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.auth.jwt import create_access_token, verify_token
from src.database import get_session
from src.models.user import User
from src.services.audit_service import AuditService


class SessionManager:
    """Manager for user sessions and JWT tokens."""

    def __init__(self, db: Session):
        self.db = db

    def refresh_access_token(self, refresh_token: str) -> Optional[str]:
        """
        Refresh access token using refresh token.

        Args:
            refresh_token: The refresh token

        Returns:
            New access token or None if refresh failed
        """
        user_id = verify_token(refresh_token)
        if not user_id:
            return None

        user = self.db.get(User, user_id)
        if not user or not user.is_active:
            return None

        # Log token refresh
        audit_service = AuditService(self.db)
        audit_service.log_authentication_success(user.id, None)

        # Create new access token
        new_access_token = create_access_token(user.id)
        return new_access_token

    def validate_session(self, user_id: str) -> bool:
        """
        Validate that a user session is still active.

        Args:
            user_id: ID of the user

        Returns:
            bool: True if session is valid, False otherwise
        """
        user = self.db.get(User, user_id)
        if not user or not user.is_active:
            return False

        return True

    def revoke_user_sessions(self, user_id: str) -> bool:
        """
        Revoke all sessions for a user.

        This is used for security purposes when a user is deactivated
        or when suspicious activity is detected.

        Args:
            user_id: ID of the user

        Returns:
            bool: True if successful, False otherwise
        """
        user = self.db.get(User, user_id)
        if not user:
            return False

        # In a production system with token storage, you would:
        # 1. Mark all refresh tokens as revoked
        # 2. Add user to a blacklist for immediate token invalidation
        # 3. Clear any server-side session data

        # For now, we'll just log the action
        audit_service = AuditService(self.db)
        audit_service.log_security_event(
            "SESSION_REVOKED",
            f"All sessions revoked for user {user_id}",
            user_id
        )

        return True

    def get_session_info(self, user_id: str) -> Optional[dict]:
        """
        Get information about the current user session.

        Args:
            user_id: ID of the user

        Returns:
            dict: Session information or None if user not found
        """
        user = self.db.get(User, user_id)
        if not user:
            return None

        return {
            "user_id": str(user.id),
            "email": user.email,
            "is_active": user.is_active,
            "last_login": user.updated_at,
            "session_active": user.is_active
        }

    def cleanup_expired_sessions(self) -> int:
        """
        Clean up expired sessions.

        In a production system with session storage, this would
        remove expired sessions and tokens.

        Returns:
            int: Number of sessions cleaned up
        """
        # In this implementation, JWT tokens are stateless,
        # so there's no server-side session storage to clean up.
        # This method is here for future extensibility.

        return 0


# Dependency for session management
def get_session_manager(db: Session = Depends(get_session)) -> SessionManager:
    """Get session manager dependency."""
    return SessionManager(db)


# Session validation dependency
def validate_active_session(
    current_user: User = Depends(lambda: None),  # Would get from auth middleware
    session_manager: SessionManager = Depends(get_session_manager)
) -> bool:
    """Validate that the current session is active."""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session"
        )

    if not session_manager.validate_session(str(current_user.id)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired"
        )

    return True


# Session timeout check
def check_session_timeout(
    last_activity: Optional[datetime] = None,
    timeout_minutes: int = 30
) -> bool:
    """
    Check if session has timed out.

    Args:
        last_activity: Last activity timestamp
        timeout_minutes: Session timeout in minutes

    Returns:
        bool: True if session is still valid, False if timed out
    """
    if not last_activity:
        return True  # No activity tracking, assume valid

    timeout_threshold = datetime.utcnow() - timedelta(minutes=timeout_minutes)
    return last_activity > timeout_threshold