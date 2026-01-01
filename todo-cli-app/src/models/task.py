"""Task validation functions for Todo CLI App."""


def validate_title(title: str) -> tuple[bool, str]:
    """
    Validate task title.

    Args:
        title: Title string to validate

    Returns:
        Tuple of (is_valid: bool, error_message: str)
        If valid, error_message is empty string

    Rules:
        - Cannot be empty after stripping whitespace
        - Maximum 200 characters
    """
    title = title.strip()

    if not title:
        return False, "Title cannot be empty"

    if len(title) > 200:
        return False, "Title too long (maximum 200 characters)"

    return True, ""


def validate_description(description: str) -> tuple[bool, str]:
    """
    Validate task description.

    Args:
        description: Description string to validate

    Returns:
        Tuple of (is_valid: bool, error_message: str)
        If valid, error_message is empty string

    Rules:
        - Can be empty (optional field)
        - Maximum 500 characters
    """
    description = description.strip()

    if len(description) > 500:
        return False, "Description too long (maximum 500 characters)"

    return True, ""


def validate_task_id(id_str: str) -> tuple[bool, int, str]:
    """
    Validate and parse task ID from string input.

    Args:
        id_str: ID string from user input

    Returns:
        Tuple of (is_valid: bool, id_value: int, error_message: str)
        If valid, id_value contains parsed integer
        If invalid, id_value is 0 and error_message explains why

    Rules:
        - Must be numeric string
        - Must be positive integer
    """
    if not id_str.strip():
        return False, 0, "ID cannot be empty"

    if not id_str.isdigit():
        return False, 0, "Invalid ID: must be a positive number"

    id_value = int(id_str)

    if id_value <= 0:
        return False, 0, "Invalid ID: must be positive"

    return True, id_value, ""
