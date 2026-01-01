# Quickstart Guide: Todo CLI App (Phase I)

**Feature**: 001-todo-cli-phase1
**Date**: 2026-01-01
**Status**: Complete

## Overview

This quickstart guide provides step-by-step instructions for setting up and running the Todo CLI App (Phase I). The application is a command-line todo list manager with in-memory storage.

**⚠️ IMPORTANT**: This is Phase I - all tasks are stored in memory only and will be lost when the application exits.

## Prerequisites

### Required

- **Python 3.13 or higher**
  - Check version: `python --version` or `python3 --version`
  - Download from: https://www.python.org/downloads/

- **UV Package Manager**
  - Check if installed: `uv --version`
  - Install UV:
    ```bash
    # macOS/Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Windows (PowerShell)
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

### Optional

- Git (for cloning repository)
- Terminal/Command prompt with UTF-8 support (for ✓ and ✗ symbols)

## Installation

### Step 1: Get the Code

**Option A: Clone Repository (if using Git)**
```bash
git clone <repository-url>
cd todo-app
```

**Option B: Download and Extract**
- Download the project zip file
- Extract to a directory
- Navigate to that directory in terminal

### Step 2: Initialize Project with UV

```bash
# Initialize UV project (creates virtual environment and installs dependencies)
uv init --python 3.13

# Verify project structure
ls -la
# Should see: src/, pyproject.toml, .python-version
```

**Note**: UV automatically creates and manages a virtual environment. You don't need to activate it manually.

### Step 3: Verify Installation

```bash
# Check Python version in UV environment
uv run python --version
# Should output: Python 3.13.x

# Verify project structure exists
ls src/
# Should see: main.py, models/, services/, cli/
```

## Running the Application

### Basic Usage

```bash
# Run the application
uv run python src/main.py
```

### First Time Launch

When you first run the app, you'll see:

```
===========================================
    Welcome to Todo CLI App (Phase I)
===========================================

⚠️  IMPORTANT: This application stores tasks
   in memory only. All data will be lost
   when you exit the application.

===========================================

===========================================
           Todo CLI App (Phase I)
===========================================

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Task Completion
6. Exit

Enter choice (1-6):
```

## Usage Examples

### Example 1: Add Your First Task

```
Enter choice (1-6): 1

--- Add New Task ---

Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, bread

✓ Task added successfully!
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Incomplete
```

### Example 2: View All Tasks

```
Enter choice (1-6): 2

==============================================================
  ID    Status    Title                         Description
==============================================================
  1     ✗         Buy groceries                 Milk, eggs
  2     ✗         Call dentist                  Annual checkup
  3     ✓         Submit report
==============================================================
Total tasks: 3
```

### Example 3: Mark Task as Complete

```
Enter choice (1-6): 5

--- Toggle Task Completion ---

Enter task ID: 1

✓ Task 1 marked as complete!
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Complete
```

### Example 4: Update Task

```
Enter choice (1-6): 3

--- Update Task ---

Enter task ID: 2

Current task:
  ID: 2
  Title: Call dentist
  Description: Annual checkup
  Status: Incomplete

Enter new title (or press Enter to keep current): Schedule dentist appointment
Enter new description (or press Enter to keep current): Call tomorrow morning

✓ Task updated successfully!
  ID: 2
  Title: Schedule dentist appointment
  Description: Call tomorrow morning
  Status: Incomplete
```

### Example 5: Delete Task

```
Enter choice (1-6): 4

--- Delete Task ---

Enter task ID to delete: 3

Task to delete:
  ID: 3
  Title: Submit report
  Description:
  Status: Complete

Are you sure you want to delete this task? (y/n): y

✓ Task 3 deleted successfully
```

### Example 6: Exit Application

```
Enter choice (1-6): 6

===========================================
Thank you for using Todo CLI App!

Note: All tasks are stored in memory and
will be lost when the application closes.

Goodbye!
===========================================
```

## Common Tasks

### Add Multiple Tasks Quickly

1. Choose option 1 (Add Task)
2. Enter title and description
3. After confirmation, you're back at main menu
4. Choose option 1 again to add another task
5. Repeat as needed

### Review Your Progress

1. Choose option 2 (View Tasks)
2. Look for ✗ (incomplete) tasks to see what's pending
3. Look for ✓ (complete) tasks to see what you've finished

### Clean Up Completed Tasks

1. Choose option 2 (View Tasks) to see task IDs
2. Choose option 4 (Delete Task)
3. Enter ID of completed task
4. Confirm deletion with 'y'
5. Repeat for other completed tasks

## Keyboard Shortcuts

### During Operation

- **Enter**: Submit input, skip optional fields
- **Ctrl+C**: Exit application immediately (no confirmation)

### Note

Phase I does not include additional keyboard shortcuts. All operations are menu-driven.

## Troubleshooting

### Issue: "python: command not found"

**Solution**: Use `python3` instead of `python`:
```bash
uv run python3 src/main.py
```

### Issue: "uv: command not found"

**Solution**: Install UV package manager:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then restart your terminal.

### Issue: ✓ and ✗ symbols not displaying

**Solution**: Ensure your terminal supports UTF-8 encoding:
```bash
# Check encoding (Linux/macOS)
echo $LANG
# Should include UTF-8

# Windows: Use Windows Terminal or PowerShell 7+ for better Unicode support
```

### Issue: Application exits immediately

**Possible Causes**:
1. Syntax error in code → Check error message
2. Ctrl+C pressed accidentally → Relaunch application
3. Python version too old → Upgrade to Python 3.13+

**Debug**:
```bash
# Run with verbose output
uv run python -v src/main.py
```

### Issue: "Task ID not found" error

**Solution**: View all tasks first to see correct IDs:
1. Choose option 2 (View Tasks)
2. Note the ID in the leftmost column
3. Use that exact ID for update/delete/toggle operations

### Issue: Cannot enter multi-word titles

**Not an Issue**: Multi-word titles work normally. Just type the full title with spaces when prompted.

**Example**:
```
Enter task title: Buy groceries and household items
# This works perfectly fine
```

## Best Practices

### 1. Use Descriptive Titles

**Good**:
- "Buy groceries - Walmart"
- "Call dentist for annual checkup"
- "Submit Q4 financial report"

**Bad**:
- "Task 1"
- "TODO"
- "Important"

### 2. Leverage Descriptions

Use descriptions for:
- Additional context
- Subtasks or steps
- Deadlines or time constraints
- Reference information

**Example**:
- **Title**: "Prepare presentation"
- **Description**: "Include Q4 metrics, team goals, and budget projections. Due Friday 3pm."

### 3. Review Tasks Regularly

- Use "View Tasks" (option 2) frequently
- Mark tasks complete as you finish them
- Delete obsolete tasks to keep list clean

### 4. Be Aware of Data Loss

**Remember**:
- Tasks are stored in memory only
- Closing the app deletes all tasks
- No undo for deletions
- No auto-save feature

**Workarounds**:
- Keep app running while working
- Manually note critical tasks elsewhere
- Wait for Phase II for persistence

### 5. Validate Input Before Submitting

- Titles must be non-empty (< 200 chars)
- Descriptions are optional (< 500 chars)
- Task IDs must be valid positive numbers
- Check task list before delete operations

## Limitations (Phase I)

### What's NOT Included

- ❌ File persistence (tasks lost on exit)
- ❌ Task categories or tags
- ❌ Due dates or reminders
- ❌ Task priorities
- ❌ Search or filter
- ❌ Undo/redo
- ❌ Multi-user support
- ❌ Web or GUI interface

### What IS Included

- ✅ Add tasks with title and description
- ✅ View all tasks
- ✅ Update task details
- ✅ Delete tasks
- ✅ Toggle completion status
- ✅ In-memory storage
- ✅ Interactive CLI menu
- ✅ Error handling and validation

## Next Steps

### After Phase I

**Phase II** (planned):
- File-based persistence (JSON or SQLite)
- Task categories and tags
- Due dates and reminders
- Search and filter capabilities

### Providing Feedback

If you encounter issues or have suggestions:
1. Note the error message (if any)
2. Describe what you were trying to do
3. Describe what happened vs. what you expected
4. Report via project issue tracker (if available)

## Quick Reference Card

```
MENU OPTIONS
1 - Add Task          Add new task with title/description
2 - View Tasks        Display all tasks in table format
3 - Update Task       Modify task title or description by ID
4 - Delete Task       Remove task by ID (with confirmation)
5 - Toggle Complete   Mark task complete or incomplete by ID
6 - Exit              Close application (data lost)

SHORTCUTS
Ctrl+C                Exit immediately
Enter                 Skip optional field, submit input

SYMBOLS
✓                     Task is complete
✗                     Task is incomplete

LIMITS
Title                 200 characters maximum, required
Description           500 characters maximum, optional
Tasks                 100+ supported (memory permitting)
```

## Support

### Documentation

- **Specification**: `specs/001-todo-cli-phase1/spec.md`
- **Architecture Plan**: `specs/001-todo-cli-phase1/plan.md`
- **Data Model**: `specs/001-todo-cli-phase1/data-model.md`
- **CLI Contract**: `specs/001-todo-cli-phase1/contracts/cli-interface.md`

### Getting Help

1. Read this quickstart guide thoroughly
2. Check troubleshooting section above
3. Review error messages carefully
4. Consult specification documents
5. Check project issue tracker or forum

---

**Quickstart Status**: ✅ COMPLETE
**Setup Time**: ~5 minutes
**Learning Curve**: Minimal (menu-driven interface)
**Ready to Use**: Yes - follow installation steps above
