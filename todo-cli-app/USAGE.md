# Todo CLI App - Usage Guide

## Quick Start

### Running the Application

**Option 1: Using UV directly**
```bash
cd todo-cli-app
uv run python src/main.py
```

**Option 2: Using the run script (Linux/macOS)**
```bash
cd todo-cli-app
./run.sh
```

**Option 3: Using Python directly (if UV environment is active)**
```bash
cd todo-cli-app
python src/main.py
```

## Application Features

### 1. Add Task
- Select option `1` from the main menu
- Enter a task title (required, max 200 characters)
- Enter an optional description (max 500 characters) or press Enter to skip
- Task is created with a unique ID and marked as incomplete

**Example:**
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

### 2. View Tasks
- Select option `2` from the main menu
- Displays all tasks in a table format
- Shows: ID, Status (✓/✗), Title, Description

**Example:**
```
Enter choice (1-6): 2

==============================================================
ID    Status    Title                          Description
==============================================================
1     ✗         Buy groceries                  Milk, eggs, bread
2     ✓         Call dentist                   Annual checkup
3     ✗         Submit report
==============================================================
Total tasks: 3
```

### 3. Update Task
- Select option `3` from the main menu
- Enter the task ID you want to update
- Press Enter to keep the current title, or type a new one
- Press Enter to keep the current description, or type a new one

**Example:**
```
Enter choice (1-6): 3

--- Update Task ---

Enter task ID: 1

Current task:
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Incomplete

Enter new title (or press Enter to keep current): Buy groceries and household items
Enter new description (or press Enter to keep current):

✓ Task 1 updated successfully!
  ID: 1
  Title: Buy groceries and household items
  Description: Milk, eggs, bread
  Status: Incomplete
```

### 4. Delete Task
- Select option `4` from the main menu
- Enter the task ID you want to delete
- Confirm deletion by typing `y` (yes) or `n` (no)
- Task is permanently removed (no undo)

**Example:**
```
Enter choice (1-6): 4

--- Delete Task ---

Enter task ID to delete: 3

Task to delete:
  ID: 3
  Title: Submit report
  Description:
  Status: Incomplete

Are you sure you want to delete this task? (y/n): y

✓ Task 3 deleted successfully
```

### 5. Toggle Task Completion
- Select option `5` from the main menu
- Enter the task ID
- Status toggles between complete (✓) and incomplete (✗)

**Example:**
```
Enter choice (1-6): 5

--- Toggle Task Completion ---

Enter task ID: 1

✓ Task 1 marked as complete!
  ID: 1
  Title: Buy groceries and household items
  Description: Milk, eggs, bread
  Status: Complete
```

### 6. Exit
- Select option `6` from the main menu
- Application closes with goodbye message
- ⚠️ All tasks are lost (in-memory storage only)

## Error Handling

### Invalid Task ID
```
Enter task ID: 999

Error: Task ID 999 not found
Please check the ID and try again.
```

### Empty Title
```
Enter task title:

Error: Title cannot be empty
Please try again.
```

### Non-Numeric ID
```
Enter task ID: abc

Error: Invalid ID: must be a positive number
Please try again.
```

### Title Too Long
```
Enter task title: [201+ characters]

Error: Title too long (maximum 200 characters)
Please try again.
```

## Tips

1. **View tasks frequently** - Use option 2 to see all your tasks and their IDs
2. **Use descriptions** - Add context to tasks with optional descriptions
3. **Delete completed tasks** - Keep your list clean by removing finished items
4. **Remember IDs** - Each task has a unique ID used for update/delete/toggle operations
5. **Exit properly** - Use option 6 to exit (though Ctrl+C also works gracefully)

## Keyboard Shortcuts

- **Enter**: Skip optional fields or submit input
- **Ctrl+C**: Exit application immediately (displays goodbye message)

## Limitations (Phase I)

- ❌ No data persistence (all data lost on exit)
- ❌ No file saving or loading
- ❌ No task categories or tags
- ❌ No due dates or reminders
- ❌ No search or filter
- ❌ No undo/redo
- ❌ No color output (plain text only)
- ❌ Single-user only

## Future Phases

**Phase II will add:**
- File-based persistence (JSON or SQLite)
- Task categories and tags
- Due dates and reminders
- Search and filter capabilities
- More advanced features

## Troubleshooting

### Application won't start
- Ensure Python 3.13+ is installed: `python --version`
- Ensure UV is installed: `uv --version`
- Try running from the correct directory: `cd todo-cli-app`

### Symbols not displaying (✓ and ✗)
- Ensure your terminal supports UTF-8 encoding
- On Windows, use Windows Terminal or PowerShell 7+

### UV command not found
- Install UV: https://docs.astral.sh/uv/getting-started/installation/
- Restart your terminal after installation

## Support

For issues or questions:
1. Check this usage guide
2. Review README.md
3. Check specification: `specs/001-todo-cli-phase1/spec.md`
4. Check quickstart guide: `specs/001-todo-cli-phase1/quickstart.md`
