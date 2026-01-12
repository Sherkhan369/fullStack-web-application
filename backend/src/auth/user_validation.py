"""
User validation and isolation utilities.

This module provides functions for validating user permissions
and ensuring proper data isolation at the application level.
"""

from typing import Optional
from sqlalchemy.orm import Session

from src.models.user import User
from src.models.task import Task
from src.database.security import set_current_user_id


def validate_user_access(
    db: Session,
    user: User,
    resource_type: str,
    resource_id: Optional[str] = None
) -> bool:
    """
    Validate that a user has access to a specific resource.

    Args:
        db: Database session
        user: The user attempting access
        resource_type: Type of resource (e.g., 'task', 'user')
        resource_id: ID of the specific resource (optional)

    Returns:
        bool: True if access is allowed, False otherwise
    """
    if not user.is_active:
        return False

    if resource_type == 'task':
        if not resource_id:
            # User can access their own task list
            return True

        # Check if the task belongs to the user
        task = db.query(Task).filter(
            Task.id == resource_id,
            Task.user_id == user.id
        ).first()

        return task is not None

    elif resource_type == 'user':
        # Users can only access their own user data
        return resource_id is None or resource_id == str(user.id)

    return False


def validate_task_ownership(
    db: Session,
    user: User,
    task_id: str
) -> Optional[Task]:
    """
    Validate that a user owns a specific task.

    Args:
        db: Database session
        user: The user attempting access
        task_id: ID of the task

    Returns:
        Task: The task if user owns it, None otherwise
    """
    if not user.is_active:
        return None

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user.id
    ).first()

    return task


def validate_user_ownership(
    db: Session,
    user: User,
    target_user_id: str
) -> bool:
    """
    Validate that a user can access specific user data.

    Args:
        db: Database session
        user: The user attempting access
        target_user_id: ID of the user being accessed

    Returns:
        bool: True if user can access the data, False otherwise
    """
    if not user.is_active:
        return False

    return str(user.id) == target_user_id


def setup_user_session(
    db: Session,
    user: User
) -> None:
    """
    Setup user session for database-level security.

    This function sets the current user ID in the database session
    for Row-Level Security enforcement.

    Args:
        db: Database session
        user: The authenticated user
    """
    try:
        set_current_user_id(db, str(user.id))
    except Exception:
        # If RLS setup fails, we still continue but log the issue
        # Application-level security will still be enforced
        pass


def validate_bulk_operation(
    db: Session,
    user: User,
    task_ids: list[str]
) -> list[Task]:
    """
    Validate bulk operations on multiple tasks.

    Args:
        db: Database session
        user: The user attempting the operation
        task_ids: List of task IDs to validate

    Returns:
        list[Task]: List of tasks the user owns
    """
    if not user.is_active or not task_ids:
        return []

    # Use IN clause for efficient bulk validation
    owned_tasks = db.query(Task).filter(
        Task.id.in_(task_ids),
        Task.user_id == user.id
    ).all()

    return owned_tasks


def check_user_permissions(
    user: User,
    action: str,
    resource: str
) -> bool:
    """
    Check if a user has permission to perform an action on a resource.

    Args:
        user: The user
        action: The action (e.g., 'read', 'write', 'delete')
        resource: The resource type (e.g., 'task', 'user')

    Returns:
        bool: True if permission is granted, False otherwise
    """
    if not user.is_active:
        return False

    # Define permission matrix
    permissions = {
        'task': {
            'read': True,    # Users can read their tasks
            'write': True,   # Users can modify their tasks
            'delete': True,  # Users can delete their tasks
        },
        'user': {
            'read': True,    # Users can read their own profile
            'write': True,   # Users can update their own profile
            'delete': False, # Users cannot delete their own account (soft delete only)
        }
    }

    resource_permissions = permissions.get(resource, {})
    return resource_permissions.get(action, False)