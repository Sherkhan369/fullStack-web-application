# Data Model: Todo CLI App (Phase I)

**Feature**: 001-todo-cli-phase1
**Date**: 2026-01-01
**Status**: Complete

## Purpose

Define the data structures and validation rules for the Todo CLI application. This document specifies the Task entity and its attributes, constraints, and relationships (though Phase I has only one entity).

## Entities

### Task

The Task entity represents a single todo item in the user's list.

**Description**: A task contains a title, optional description, completion status, and a unique identifier. Tasks are stored in memory for the duration of the application session.

**Storage**: In-memory list of dictionaries (no persistence in Phase I)

**Attributes**:

| Attribute | Type | Required | Default | Constraints | Description |
|-----------|------|----------|---------|-------------|-------------|
| `id` | `int` | Yes (auto) | Auto-generated | Positive integer, unique, auto-increment | Unique identifier for the task, assigned automatically when task is created |
| `title` | `str` | Yes | None | Non-empty, max 200 chars | Task title or summary, cannot be empty or whitespace-only |
| `description` | `str` | No | Empty string `""` | Max 500 chars | Optional additional details about the task |
| `completed` | `bool` | Yes (auto) | `False` | Boolean | Completion status: `True` if done, `False` if pending |

**Validation Rules**:

1. **ID Validation**:
   - Must be positive integer (> 0)
   - Generated automatically by task_manager
   - Never reused after task deletion
   - Sequential (1, 2, 3, ...)

2. **Title Validation**:
   - MUST NOT be empty string
   - MUST NOT be whitespace-only (e.g., "   ")
   - MUST be stripped of leading/trailing whitespace before storage
   - Maximum length: 200 characters
   - Error message: "Title cannot be empty"

3. **Description Validation**:
   - CAN be empty string (optional field)
   - Stripped of leading/trailing whitespace before storage
   - Maximum length: 500 characters
   - If not provided, defaults to empty string `""`

4. **Completed Validation**:
   - MUST be boolean (`True` or `False`)
   - Defaults to `False` on task creation
   - Can be toggled between `True` and `False`

**Example Task (Dictionary)**:

```python
task = {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, and vegetables",
    "completed": False
}
```

**Example Tasks (Various States)**:

```python
# Task with description
task1 = {
    "id": 1,
    "title": "Call dentist",
    "description": "Schedule annual checkup for next month",
    "completed": False
}

# Task without description
task2 = {
    "id": 2,
    "title": "Submit report",
    "description": "",
    "completed": True
}

# Completed task
task3 = {
    "id": 3,
    "title": "Review pull request #42",
    "description": "Check code quality and test coverage",
    "completed": True
}
```

## State Transitions

Tasks have a simple two-state lifecycle:

```
[Created]
    ↓
[Incomplete] (completed = False)
    ↕ (toggle)
[Complete] (completed = True)
    ↓
[Deleted] (removed from list)
```

**Transition Rules**:

1. **Creation**: Task starts as incomplete (`completed = False`)
2. **Toggle**: Can switch between incomplete ↔ complete any number of times
3. **Deletion**: Permanent removal from list (no undo in Phase I)

## Data Storage

**Storage Type**: In-memory Python list

**Storage Location**: Module-level variable in `src/services/task_manager.py`

**Structure**:
```python
_tasks: list[dict] = []  # List of task dictionaries
_next_id: int = 1         # Counter for auto-incrementing IDs
```

**Persistence**: None (Phase I constraint - data lost when app exits)

**Capacity**: Limited only by available memory (target: 100+ tasks without performance issues)

## Validation Functions

**Location**: `src/models/task.py`

### validate_title

```python
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
```

### validate_description

```python
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
```

### validate_task_id

```python
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
```

## Error Messages

Standard error messages for validation failures:

| Validation | Error Message |
|------------|--------------|
| Empty title | "Title cannot be empty" |
| Title too long | "Title too long (maximum 200 characters)" |
| Description too long | "Description too long (maximum 500 characters)" |
| Non-numeric ID | "Invalid ID: must be a positive number" |
| ID not positive | "Invalid ID: must be positive" |
| Task not found | "Error: Task ID {id} not found" |

## Relationships

**Phase I**: No relationships between entities (only one entity exists)

**Future Phases**: May add relationships such as:
- Categories (many tasks to one category)
- Tags (many-to-many between tasks and tags)
- Subtasks (parent-child task relationships)

## Data Integrity Rules

1. **ID Uniqueness**: Each task MUST have a unique ID within the session
2. **ID Immutability**: Task IDs MUST NOT change after creation
3. **ID Continuity**: IDs MUST NOT be reused after task deletion
4. **Title Requirement**: Every task MUST have a non-empty title
5. **Boolean Integrity**: `completed` field MUST always be boolean (never null or undefined)

## Testing Considerations

**Valid Test Cases**:
```python
# Valid task with description
{"id": 1, "title": "Test task", "description": "Test desc", "completed": False}

# Valid task without description
{"id": 2, "title": "Another task", "description": "", "completed": False}

# Valid completed task
{"id": 3, "title": "Done task", "description": "", "completed": True}

# Valid task with max length title (200 chars)
{"id": 4, "title": "x" * 200, "description": "", "completed": False}
```

**Invalid Test Cases** (should trigger validation errors):
```python
# Empty title
{"id": 1, "title": "", "description": "desc", "completed": False}

# Whitespace-only title
{"id": 2, "title": "   ", "description": "desc", "completed": False}

# Title too long
{"id": 3, "title": "x" * 201, "description": "", "completed": False}

# Description too long
{"id": 4, "title": "Task", "description": "x" * 501, "completed": False}
```

**Edge Cases**:
```python
# Title with special characters
{"id": 1, "title": "Buy milk @ store #1", "description": "", "completed": False}

# Title with Unicode
{"id": 2, "title": "学習する - Study", "description": "", "completed": False}

# Title with newlines (should be stripped)
{"id": 3, "title": "Task\nwith\nnewlines", "description": "", "completed": False}

# Very long description (just under limit)
{"id": 4, "title": "Task", "description": "x" * 500, "completed": False}
```

## Implementation Notes

1. **No ORM**: Phase I uses plain dictionaries, no SQLAlchemy or ORM
2. **No Database**: No SQLite, PostgreSQL, or any database in Phase I
3. **Manual Validation**: Validation functions called explicitly in service layer
4. **Type Hints**: Use type hints for clarity (e.g., `list[dict]`, `tuple[bool, str]`)
5. **Immutability**: Task dictionaries are mutable, but IDs should never be changed

## Migration Strategy (Future Phases)

**Phase II+**: If adding persistence:
- Export current dict structure to JSON easily
- Migrate to dataclasses or Pydantic models
- Add SQLite or file-based storage
- Maintain same validation rules

**Backwards Compatibility**: Dict-based structure makes future migrations easier

---

**Data Model Status**: ✅ COMPLETE
**Validation Rules**: ✅ DEFINED
**Constitution Compliance**: ✅ VERIFIED (in-memory, no external deps)
**Ready for**: Contract definitions and implementation
