# Research & Technical Decisions: Todo CLI App (Phase I)

**Feature**: 001-todo-cli-phase1
**Date**: 2026-01-01
**Status**: Complete

## Purpose

Document research findings and technical decisions for Phase I Todo CLI implementation. All decisions align with constitution constraints: Python 3.13+, UV package manager, in-memory storage, CLI-only, no external dependencies.

## Research Areas

### 1. UV Project Initialization

**Question**: What are best practices for initializing a Python 3.13+ project with UV?

**Research Findings**:
- UV is a modern Python package and project manager (Rust-based, fast)
- `uv init` creates project structure with pyproject.toml
- `uv add` manages dependencies
- `uv run` executes Python scripts with proper environment
- Supports Python 3.13+ out of the box

**Decision**: Use `uv init` to bootstrap project structure

**Rationale**:
- Modern, fast package management
- Built-in virtual environment handling
- No manual venv creation needed
- Aligns with constitution requirement

**Implementation**:
```bash
uv init --python 3.13
uv run python src/main.py
```

**Alternatives Considered**:
- pip + venv: Traditional but slower, requires manual venv setup
- poetry: Alternative modern tool but UV specified in constitution

**Status**: ✅ Approved

---

### 2. In-Memory Data Structure

**Question**: Should tasks be stored as list of dictionaries or list of custom objects?

**Research Findings**:
- List of dicts: Simple, flexible, no class overhead
- List of dataclasses: More structure, type safety, but adds complexity
- List of Pydantic models: Excellent validation but external dependency

**Decision**: Use list of dictionaries

**Rationale**:
- Simplest approach for Phase I
- No external dependencies (constitution constraint)
- Easy to serialize if persistence added later
- Sufficient validation possible with manual checks
- Python dict operations are fast (O(1) lookup)

**Data Structure**:
```python
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "completed": False
    },
    # ... more tasks
]
```

**Alternatives Considered**:
- Dataclasses: Better type safety but more boilerplate
- Pydantic: Best validation but violates "standard library only" constraint
- Named tuples: Immutable, harder to update

**Status**: ✅ Approved

---

### 3. CLI Menu Pattern

**Question**: What's the best pattern for interactive CLI menus in Python (standard library only)?

**Research Findings**:
- Simple loop with `input()` and numbered choices
- No external library needed (argparse for args, not menus)
- Clear prompt design critical for usability (FR-012)

**Decision**: Use while loop with `input()` and numbered menu options

**Rationale**:
- Standard library only (no external deps)
- User-friendly for non-technical users
- Easy to test manually
- Meets "clear CLI prompts" requirement

**Pattern**:
```python
while True:
    print("\n=== Todo CLI ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Completion")
    print("6. Exit")

    choice = input("\nEnter choice (1-6): ").strip()

    if choice == "1":
        # add task
    elif choice == "6":
        break
```

**Alternatives Considered**:
- argparse: For command-line args, not interactive menus
- click library: External dependency, violates Phase I constraints
- curses: Overly complex, platform issues

**Status**: ✅ Approved

---

### 4. ID Generation Strategy

**Question**: How to implement auto-incrementing IDs without a database?

**Research Findings**:
- Module-level counter variable
- Track next available ID
- Increment on each task creation
- Never reuse IDs (even after deletion)

**Decision**: Module-level counter variable in task_manager.py

**Rationale**:
- Simple to implement
- Thread-safe for single-user application
- IDs never reused (FR-013 requirement)
- Survives for session duration (in-memory)

**Implementation**:
```python
# In task_manager.py
_next_id = 1
_tasks = []

def add_task(title: str, description: str = "") -> dict:
    global _next_id
    task = {
        "id": _next_id,
        "title": title,
        "description": description,
        "completed": False
    }
    _tasks.append(task)
    _next_id += 1
    return task
```

**Alternatives Considered**:
- UUID: Too long, hard for users to reference
- max(ids) + 1: Works but requires iterating all tasks
- Random integers: Risk of collisions

**Status**: ✅ Approved

---

### 5. Input Validation

**Question**: How to validate user input (empty titles, non-numeric IDs) using standard library?

**Research Findings**:
- String methods: `.strip()`, `.isdigit()`, `len()`
- Simple validation functions for each input type
- Return early with error messages

**Decision**: Use built-in string methods for validation

**Rationale**:
- No external libraries needed
- Clear error messages (FR-010 requirement)
- Simple validation functions in models layer

**Pattern**:
```python
def validate_title(title: str) -> tuple[bool, str]:
    """Returns (is_valid, error_message)"""
    title = title.strip()
    if not title:
        return False, "Title cannot be empty"
    if len(title) > 200:
        return False, "Title too long (max 200 characters)"
    return True, ""

def validate_task_id(id_str: str) -> tuple[bool, int, str]:
    """Returns (is_valid, id_value, error_message)"""
    if not id_str.isdigit():
        return False, 0, "Invalid ID: must be a number"
    return True, int(id_str), ""
```

**Alternatives Considered**:
- Regex: Overkill for simple validation
- Pydantic validators: External dependency
- No validation: Poor UX, violates requirements

**Status**: ✅ Approved

---

### 6. Error Handling

**Question**: How should CLI errors be displayed to users?

**Research Findings**:
- Print error messages to stdout (not stderr for simple CLI)
- Use clear, friendly language
- Provide actionable feedback
- Don't crash on invalid input

**Decision**: Print error messages with clear formatting, return to main menu

**Rationale**:
- Meets FR-010 (error messages for invalid operations)
- User-friendly experience
- Application never crashes
- Simple to implement

**Pattern**:
```python
def delete_task(task_id: int) -> tuple[bool, str]:
    """Returns (success, message)"""
    task = find_task_by_id(task_id)
    if not task:
        return False, f"Error: Task ID {task_id} not found"

    _tasks.remove(task)
    return True, f"Task {task_id} deleted successfully"

# In CLI
success, message = delete_task(task_id)
print(message)
if not success:
    print("Please try again.")
```

**Alternatives Considered**:
- Exceptions: Overkill for expected validation errors
- Stderr output: Confusing for simple CLI app
- Silent failures: Poor UX

**Status**: ✅ Approved

---

### 7. Display Formatting

**Question**: How to format task list display for readability?

**Research Findings**:
- Simple table-like format using string formatting
- Status symbols: ✓ (complete) and ✗ (incomplete)
- Truncate long titles/descriptions if needed

**Decision**: Manual string formatting with fixed-width columns

**Rationale**:
- No external library needed (rich, tabulate would violate constraints)
- Easy to read
- Works in all terminals that support UTF-8

**Pattern**:
```python
def display_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("\nNo tasks found. Add your first task!")
        return

    print("\n" + "="*60)
    print(f"{'ID':<5} {'Status':<8} {'Title':<30} {'Description'}")
    print("="*60)

    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        title = task["title"][:30]
        desc = task["description"][:20] if task["description"] else ""
        print(f"{task['id']:<5} {status:<8} {title:<30} {desc}")

    print("="*60)
```

**Alternatives Considered**:
- Rich library: Beautiful but external dependency
- tabulate: External dependency
- JSON output: Not user-friendly for CLI

**Status**: ✅ Approved

---

### 8. Project Structure

**Question**: How should source code be organized?

**Research Findings**:
- Standard Python project structure: `src/` for source code
- Separation of concerns: models, services, CLI
- Test directory (optional for Phase I)

**Decision**: Three-layer architecture in `src/` directory

**Rationale**:
- Clean separation of concerns
- Follows Python best practices
- Easy to extend in future phases
- Aligns with clean code principle from constitution

**Structure**:
```
src/
├── __init__.py
├── models/
│   ├── __init__.py
│   └── task.py          # Task validation functions
├── services/
│   ├── __init__.py
│   └── task_manager.py  # CRUD operations
├── cli/
│   ├── __init__.py
│   ├── menu.py          # Main menu loop
│   └── display.py       # Display formatting
└── main.py              # Entry point
```

**Alternatives Considered**:
- Flat structure: Poor organization, hard to maintain
- Single file: Violates clean code principles
- Package per feature: Overkill for small app

**Status**: ✅ Approved

---

## Summary of Technical Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Language** | Python 3.13+ | Constitution requirement |
| **Package Manager** | UV | Constitution requirement, modern and fast |
| **Storage** | In-memory list of dicts | Phase I constraint, simple |
| **CLI Framework** | Native `input()` loops | Standard library only |
| **Validation** | String methods | Standard library only |
| **ID Generation** | Module counter variable | Simple, no database needed |
| **Display** | Manual string formatting | Standard library only |
| **Testing** | Manual CLI testing | Phase I - automated tests optional |
| **Architecture** | Three-layer (Models, Services, CLI) | Clean code principles |

## Key Decisions Summary

1. ✅ **UV for project init**: Fast, modern, constitution-mandated
2. ✅ **List of dicts**: Simplest data structure for Phase I
3. ✅ **Interactive menu**: Numbered options with `input()`
4. ✅ **Counter-based IDs**: Module variable, auto-increment
5. ✅ **String method validation**: Built-in, no external deps
6. ✅ **Print error messages**: Clear, user-friendly feedback
7. ✅ **Manual formatting**: UTF-8 symbols, fixed-width columns
8. ✅ **Three-layer architecture**: Models, Services, CLI separation

## Dependencies

**External**: None (standard library only per Phase I constraints)

**System Requirements**:
- Python 3.13+
- UV package manager

## Next Steps

Phase 0 research complete. Proceed to Phase 1:
1. Create data-model.md with detailed Task entity definition
2. Create contracts/cli-interface.md with CLI specifications
3. Create quickstart.md with setup and usage instructions
4. Update agent context with project technology stack

---

**Research Status**: ✅ COMPLETE
**All Decisions**: ✅ APPROVED
**Constitution Compliance**: ✅ VERIFIED
**Ready for**: Phase 1 Design
