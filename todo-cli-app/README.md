# Todo CLI App (Phase I)

A Python 3.13+ command-line todo list application with in-memory storage.

## Phase I Constraints

⚠️ **IMPORTANT**: This is Phase I implementation with the following constraints:
- **In-memory storage only** - All tasks are lost when the application exits
- **No file persistence** - No database or file storage
- **Single-user, single-session** - Designed for one user per session
- **CLI-only interface** - Command-line interface only

## Features

- ✅ Add tasks with title and optional description
- ✅ View all tasks with IDs and completion status
- ✅ Update task title and description
- ✅ Delete tasks
- ✅ Toggle task completion status (✓/✗)

## Requirements

- Python 3.13 or higher
- UV package manager

## Installation

```bash
# Install UV if not already installed
# macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Navigate to project directory
cd todo-cli-app

# Run the application
uv run python src/main.py
```

## Usage

When you run the application, you'll see a menu with 6 options:

1. **Add Task** - Create a new task
2. **View Tasks** - Display all tasks
3. **Update Task** - Edit task details
4. **Delete Task** - Remove a task
5. **Toggle Task Completion** - Mark task as complete/incomplete
6. **Exit** - Close the application

### Example Workflow

```
1. Add a task: "Buy groceries"
2. Add another task: "Call dentist" with description "Schedule annual checkup"
3. View all tasks to see your list
4. Mark task ID 1 as complete
5. View tasks again to see the ✓ status
6. Exit the application
```

## Data Loss Warning

All tasks are stored in memory only. When you exit the application, **all data will be lost**. This is intentional Phase I behavior.

## Documentation

For detailed information, see:
- **Specification**: `specs/001-todo-cli-phase1/spec.md`
- **Implementation Plan**: `specs/001-todo-cli-phase1/plan.md`
- **Quick Start Guide**: `specs/001-todo-cli-phase1/quickstart.md`

## Constitution

This project follows the Todo App Constitution (Phase I) located at `.specify/memory/constitution.md`.

## License

Phase I - Internal Development Only
