"""Task management service for Todo CLI App."""

from models.task import validate_title, validate_description

# Module-level storage
_tasks: list[dict] = []
_next_id: int = 1


def add_task(title: str, description: str = "") -> dict:
    """
    Add a new task.

    Args:
        title: Task title (required)
        description: Task description (optional)

    Returns:
        Created task dictionary

    Raises:
        ValueError: If title validation fails
    """
    global _next_id

    # Validate title
    is_valid, error_msg = validate_title(title)
    if not is_valid:
        raise ValueError(error_msg)

    # Validate description
    is_valid, error_msg = validate_description(description)
    if not is_valid:
        raise ValueError(error_msg)

    # Create task
    task = {
        "id": _next_id,
        "title": title.strip(),
        "description": description.strip(),
        "completed": False
    }

    _tasks.append(task)
    _next_id += 1

    return task


def get_all_tasks() -> list[dict]:
    """
    Get all tasks.

    Returns:
        Copy of tasks list
    """
    return _tasks.copy()


def find_task_by_id(task_id: int) -> dict | None:
    """
    Find a task by ID.

    Args:
        task_id: Task ID to find

    Returns:
        Task dictionary if found, None otherwise
    """
    for task in _tasks:
        if task["id"] == task_id:
            return task
    return None


def toggle_task_completion(task_id: int) -> tuple[bool, str, bool]:
    """
    Toggle task completion status.

    Args:
        task_id: Task ID to toggle

    Returns:
        Tuple of (success: bool, message: str, new_status: bool)
    """
    task = find_task_by_id(task_id)
    if not task:
        return False, f"Error: Task ID {task_id} not found", False

    task["completed"] = not task["completed"]
    status_text = "complete" if task["completed"] else "incomplete"

    return True, f"Task {task_id} marked as {status_text}", task["completed"]


def update_task(task_id: int, new_title: str | None = None,
                new_description: str | None = None) -> tuple[bool, str]:
    """
    Update task title and/or description.

    Args:
        task_id: Task ID to update
        new_title: New title (None to keep current)
        new_description: New description (None to keep current)

    Returns:
        Tuple of (success: bool, message: str)
    """
    task = find_task_by_id(task_id)
    if not task:
        return False, f"Error: Task ID {task_id} not found"

    # Update title if provided
    if new_title is not None:
        is_valid, error_msg = validate_title(new_title)
        if not is_valid:
            return False, error_msg
        task["title"] = new_title.strip()

    # Update description if provided
    if new_description is not None:
        is_valid, error_msg = validate_description(new_description)
        if not is_valid:
            return False, error_msg
        task["description"] = new_description.strip()

    return True, f"Task {task_id} updated successfully"


def delete_task(task_id: int) -> tuple[bool, str]:
    """
    Delete a task.

    Args:
        task_id: Task ID to delete

    Returns:
        Tuple of (success: bool, message: str)
    """
    task = find_task_by_id(task_id)
    if not task:
        return False, f"Error: Task ID {task_id} not found"

    _tasks.remove(task)
    return True, f"Task {task_id} deleted successfully"
