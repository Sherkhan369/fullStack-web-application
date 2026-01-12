from datetime import datetime, timezone
from typing import Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from src.auth.jwt import verify_token
from src.auth.user_validation import setup_user_session, validate_user_access
from src.database import get_session
from src.models.user import User
from src.services.audit_service import AuditService

security = HTTPBearer()


def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_session),
) -> User:
    """Get current authenticated user with session setup."""
    token = credentials.credentials
    user_id = verify_token(token)

    if not user_id:
        # Audit failed authentication attempt
        audit_service = AuditService(db)
        audit_service.log_authentication_failure(
            request.client.host if request.client else None,
            "Invalid token",
            request.url.path
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.get(User, user_id)
    if not user:
        # Audit failed authentication attempt
        audit_service = AuditService(db)
        audit_service.log_authentication_failure(
            request.client.host if request.client else None,
            "User not found",
            request.url.path
        )

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    if not user.is_active:
        # Audit blocked access attempt
        audit_service = AuditService(db)
        audit_service.log_access_denied(
            user.id,
            request.client.host if request.client else None,
            "Inactive user",
            request.url.path
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )

    # Setup user session for RLS
    setup_user_session(db, user)

    # Audit successful authentication
    audit_service = AuditService(db)
    audit_service.log_authentication_success(user.id, request.client.host if request.client else None)

    return user


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Get current active user."""
    return current_user


def require_permission(
    resource_type: str,
    action: str = "read",
    resource_id_param: Optional[str] = None
):
    """
    Dependency to require specific permissions for resource access.

    Args:
        resource_type: Type of resource being accessed
        action: Action being performed (read, write, delete)
        resource_id_param: Parameter name containing resource ID (optional)

    Returns:
        Dependency function
    """
    def permission_checker(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_session),
    ):
        # Check basic permissions
        if not validate_user_access(db, current_user, resource_type):
            audit_service = AuditService(db)
            audit_service.log_access_denied(
                current_user.id,
                None,  # Would get from request if available
                f"No permission for {action} on {resource_type}",
                None
            )

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )

        # For specific resource access, validate ownership
        if resource_id_param:
            resource_id = getattr(current_user, resource_id_param, None)
            if resource_id and not validate_user_access(db, current_user, resource_type, resource_id):
                audit_service = AuditService(db)
                audit_service.log_access_denied(
                    current_user.id,
                    None,
                    f"Access denied to {resource_type} {resource_id}",
                    None
                )

                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Access denied to this resource"
                )

        return current_user

    return permission_checker


def validate_task_ownership(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session),
):
    """Validate that current user owns the specified task."""
    from src.auth.user_validation import validate_task_ownership

    task = validate_task_ownership(db, current_user, task_id)
    if not task:
        audit_service = AuditService(db)
        audit_service.log_access_denied(
            current_user.id,
            None,
            f"Task {task_id} not found or access denied",
            None
        )

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )

    return task


def audit_request(
    request: Request,
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_session),
):
    """
    Dependency to audit all requests for security monitoring.

    This should be used in routes that handle sensitive operations.
    """
    if current_user:
        # Log successful request
        audit_service = AuditService(db)
        audit_service.log_api_access(
            current_user.id,
            request.client.host if request.client else None,
            request.method,
            request.url.path,
            datetime.now(timezone.utc)
        )
    else:
        # Log anonymous request (shouldn't happen with auth required routes)
        pass

    return True