# CLI Interface Contract: Todo CLI App (Phase I)

**Feature**: 001-todo-cli-phase1
**Date**: 2026-01-01
**Status**: Complete

## Purpose

Define the command-line interface contract for the Todo CLI application. This document specifies menu options, user prompts, expected inputs, outputs, and error messages.

## Main Menu

**Display**: The main menu is displayed when the application starts and after each operation completes.

**Format**:
```
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

**Input**: Single character ('1', '2', '3', '4', '5', or '6')

**Behavior**:
- Invalid input: Display error "Invalid choice. Please enter a number between 1 and 6." and re-prompt
- Valid input: Execute corresponding operation and return to menu (except Exit)

---

## Operation 1: Add Task

**Menu Option**: "1. Add Task"

**User Flow**:
1. User selects option 1
2. System prompts for title
3. User enters title
4. System validates title
5. System prompts for description (optional)
6. User enters description or presses Enter to skip
7. System creates task and displays confirmation
8. Return to main menu

**Prompts and Inputs**:

```
--- Add New Task ---

Enter task title: [user input]
Enter task description (optional, press Enter to skip): [user input]
```

**Success Output**:
```
✓ Task added successfully!
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Incomplete
```

**Error Cases**:

1. **Empty Title**:
   ```
   Error: Title cannot be empty
   Please try again.
   ```

2. **Title Too Long** (> 200 chars):
   ```
   Error: Title too long (maximum 200 characters)
   Please try again.
   ```

3. **Description Too Long** (> 500 chars):
   ```
   Error: Description too long (maximum 500 characters)
   Please try again.
   ```

---

## Operation 2: View Tasks

**Menu Option**: "2. View Tasks"

**User Flow**:
1. User selects option 2
2. System displays all tasks in table format
3. Return to main menu

**Output (Tasks Exist)**:
```
==============================================================
  ID    Status    Title                         Description
==============================================================
  1     ✗         Buy groceries                 Milk, eggs
  2     ✓         Call dentist                  Annual checkup
  3     ✗         Submit report
==============================================================
Total tasks: 3
```

**Output (No Tasks)**:
```
==============================================================
                    No tasks found!
         Add your first task using option 1.
==============================================================
```

**Column Specifications**:
- ID: Left-aligned, 5 characters wide
- Status: Left-aligned, 8 characters wide (✓ for complete, ✗ for incomplete)
- Title: Left-aligned, 30 characters wide (truncated if longer)
- Description: Left-aligned, 20 characters (truncated if longer, empty if not provided)

**Symbols**:
- Complete: ✓ (U+2713 CHECK MARK)
- Incomplete: ✗ (U+2717 BALLOT X)

---

## Operation 3: Update Task

**Menu Option**: "3. Update Task"

**User Flow**:
1. User selects option 3
2. System prompts for task ID
3. User enters task ID
4. System validates ID and checks if task exists
5. System displays current task details
6. System prompts for new title (or Enter to keep current)
7. User enters new title or presses Enter
8. System prompts for new description (or Enter to keep current)
9. User enters new description or presses Enter
10. System updates task and displays confirmation
11. Return to main menu

**Prompts and Inputs**:

```
--- Update Task ---

Enter task ID: [user input]

Current task:
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Incomplete

Enter new title (or press Enter to keep current): [user input]
Enter new description (or press Enter to keep current): [user input]
```

**Success Output**:
```
✓ Task updated successfully!
  ID: 1
  Title: Buy milk and eggs
  Description: Just milk and eggs now
  Status: Incomplete
```

**Error Cases**:

1. **Invalid ID Format**:
   ```
   Error: Invalid ID: must be a positive number
   Please try again.
   ```

2. **Task Not Found**:
   ```
   Error: Task ID 99 not found
   Please check the ID and try again.
   ```

3. **Empty New Title** (if provided):
   ```
   Error: Title cannot be empty
   Keeping previous title.
   ```

4. **New Title Too Long**:
   ```
   Error: Title too long (maximum 200 characters)
   Keeping previous title.
   ```

---

## Operation 4: Delete Task

**Menu Option**: "4. Delete Task"

**User Flow**:
1. User selects option 4
2. System prompts for task ID
3. User enters task ID
4. System validates ID and checks if task exists
5. System displays task details and asks for confirmation
6. User confirms (y/n)
7. System deletes task and displays confirmation
8. Return to main menu

**Prompts and Inputs**:

```
--- Delete Task ---

Enter task ID to delete: [user input]

Task to delete:
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Incomplete

Are you sure you want to delete this task? (y/n): [user input]
```

**Success Output** (confirmed):
```
✓ Task 1 deleted successfully
```

**Cancelled Output** (not confirmed):
```
Deletion cancelled. Task not deleted.
```

**Error Cases**:

1. **Invalid ID Format**:
   ```
   Error: Invalid ID: must be a positive number
   Please try again.
   ```

2. **Task Not Found**:
   ```
   Error: Task ID 99 not found
   Please check the ID and try again.
   ```

---

## Operation 5: Toggle Task Completion

**Menu Option**: "5. Toggle Task Completion"

**User Flow**:
1. User selects option 5
2. System prompts for task ID
3. User enters task ID
4. System validates ID and checks if task exists
5. System toggles completion status
6. System displays confirmation with new status
7. Return to main menu

**Prompts and Inputs**:

```
--- Toggle Task Completion ---

Enter task ID: [user input]
```

**Success Output** (marked as complete):
```
✓ Task 1 marked as complete!
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, bread
  Status: Complete
```

**Success Output** (marked as incomplete):
```
✓ Task 2 marked as incomplete
  ID: 2
  Title: Call dentist
  Description: Annual checkup
  Status: Incomplete
```

**Error Cases**:

1. **Invalid ID Format**:
   ```
   Error: Invalid ID: must be a positive number
   Please try again.
   ```

2. **Task Not Found**:
   ```
   Error: Task ID 99 not found
   Please check the ID and try again.
   ```

---

## Operation 6: Exit

**Menu Option**: "6. Exit"

**User Flow**:
1. User selects option 6
2. System displays exit message
3. Application terminates

**Output**:
```
===========================================
Thank you for using Todo CLI App!

Note: All tasks are stored in memory and
will be lost when the application closes.

Goodbye!
===========================================
```

---

## Startup Message

**Display**: Shown once when application starts (before main menu)

```
===========================================
    Welcome to Todo CLI App (Phase I)
===========================================

⚠️  IMPORTANT: This application stores tasks
   in memory only. All data will be lost
   when you exit the application.

===========================================
```

---

## Input Handling Rules

### General Rules

1. **Whitespace**: Strip leading/trailing whitespace from all text inputs
2. **Case Sensitivity**: Menu choices are case-sensitive (must be digits 1-6)
3. **Empty Input**: Pressing Enter without text is allowed for optional fields
4. **Invalid Input**: Display error message and re-prompt (don't crash)
5. **Ctrl+C**: Allow user to exit gracefully with Ctrl+C (KeyboardInterrupt)

### Task ID Input

**Valid**:
- "1", "2", "3", ... (positive integers as strings)

**Invalid**:
- "" (empty)
- "abc" (non-numeric)
- "1.5" (decimal)
- "-1" (negative)
- "0" (zero)

### Title Input

**Valid**:
- Any non-empty string after stripping whitespace
- Maximum 200 characters
- Special characters allowed
- Unicode characters allowed

**Invalid**:
- "" (empty string)
- "   " (whitespace only)
- Strings > 200 characters

### Description Input

**Valid**:
- Any string (including empty)
- Maximum 500 characters
- Special characters allowed
- Unicode characters allowed

**Invalid**:
- Strings > 500 characters

### Yes/No Confirmation

**Valid**:
- "y", "Y" (yes)
- "n", "N" (no)

**Invalid**:
- Any other input → treat as "no" (safe default)

---

## Error Message Standards

### Format

All error messages follow this format:
```
Error: [clear description of what went wrong]
[Optional: suggestion for how to fix]
```

### Examples

```
Error: Title cannot be empty
Please try again.

Error: Task ID 5 not found
Please check the ID and try again.

Error: Invalid choice. Please enter a number between 1 and 6.

Error: Title too long (maximum 200 characters)
Please use a shorter title.
```

### Tone

- Clear and specific (not vague)
- Friendly and non-technical
- Actionable (tell user what to do)
- No blame or judgment

---

## Success Message Standards

### Format

Success messages follow this format:
```
✓ [Action completed]
  [Optional: details about what changed]
```

### Examples

```
✓ Task added successfully!
  ID: 1

✓ Task 3 marked as complete!

✓ Task updated successfully!
```

---

## Keyboard Shortcuts

**Phase I**: No keyboard shortcuts (menu-driven only)

**Future Phases**: May add shortcuts like:
- Ctrl+A: Add task
- Ctrl+L: List tasks
- Ctrl+Q: Quit

---

## Screen Clearing

**Phase I**: Do not clear screen between operations (let output scroll)

**Rationale**: Allows users to review previous operations and messages

**Future Phases**: May add screen clearing option

---

## Color Support

**Phase I**: No color output (plain text only)

**Symbols Only**: Use ✓ and ✗ for visual distinction

**Future Phases**: May add color support if external library allowed

---

## Testing Checklist

To validate CLI interface implementation:

- [ ] Main menu displays correctly with all 6 options
- [ ] Invalid menu choice shows error and re-prompts
- [ ] Add task prompts for title and description
- [ ] Add task validates title (not empty, < 200 chars)
- [ ] Add task validates description (< 500 chars)
- [ ] View tasks shows table with all tasks
- [ ] View tasks shows "no tasks" message when list empty
- [ ] Update task prompts for ID and new values
- [ ] Update task validates ID exists
- [ ] Update task keeps current values if Enter pressed
- [ ] Delete task shows confirmation prompt
- [ ] Delete task only deletes on "y" confirmation
- [ ] Toggle completion changes status correctly
- [ ] Toggle completion shows new status in output
- [ ] Exit displays goodbye message
- [ ] Error messages are clear and helpful
- [ ] All operations return to main menu (except exit)
- [ ] Startup message warns about in-memory storage
- [ ] ✓ and ✗ symbols display correctly

---

**Contract Status**: ✅ COMPLETE
**Operations Defined**: 6 (Add, View, Update, Delete, Toggle, Exit)
**Error Handling**: ✅ COMPREHENSIVE
**User Experience**: ✅ CLEAR PROMPTS AND FEEDBACK
**Ready for**: Implementation
