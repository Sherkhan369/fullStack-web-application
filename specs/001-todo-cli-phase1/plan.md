# Implementation Plan: Todo CLI App (Phase I)

**Branch**: `001-todo-cli-phase1` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-cli-phase1/spec.md`

## Summary

Build a Python 3.13+ command-line todo list application with in-memory storage. Users can add tasks (with title and optional description), view all tasks with status indicators, update task details, delete tasks, and toggle completion status. All operations are performed via an interactive CLI menu. The application uses UV for project initialization and dependency management, adhering to Phase I constraints: no persistence, no external services, single-user single-session design.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (no external packages for Phase I)
**Storage**: In-memory (list of dictionaries)
**Testing**: Manual CLI testing (automated tests optional for Phase I)
**Target Platform**: Cross-platform CLI (Windows, macOS, Linux)
**Project Type**: Single project (CLI application)
**Performance Goals**: < 2 seconds to add task, < 1 second to view list, handle 100+ tasks without degradation
**Constraints**: In-memory only (no persistence), CLI-only interface, single-session, no external APIs/services
**Scale/Scope**: Single-user, single-session, 100+ tasks capacity

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ Principle I: Spec-Driven Refinement
- Specification approved and unambiguous (passed validation checklist)
- All requirements clearly defined with acceptance criteria
- **Status**: PASS

### ✅ Principle II: Clean Code & Readability
- Plan includes code organization (models, services, CLI layers)
- Will follow PEP 8, use type hints, keep functions < 20 lines
- Meaningful names, single responsibility principle
- **Status**: PASS

### ✅ Principle III: Single-Feature Scope
- This plan covers one feature: Phase I Todo CLI
- No bundling with other features
- Clear boundaries defined in spec
- **Status**: PASS

### ✅ Principle IV: Phase I Constraints (NON-NEGOTIABLE)
- ✅ In-memory storage only (no DB, no files)
- ✅ Console-based interaction only
- ✅ Single-user, single-session design
- ✅ Python 3.13+ with UV package manager
- ✅ No external services or APIs
- **Status**: PASS - All constraints satisfied

### ✅ Principle V: CLI-Only Interaction
- Interactive CLI menu interface planned
- All operations via command-line
- Tasks identified by unique integer IDs
- **Status**: PASS

### Overall Gate Status: ✅ APPROVED FOR IMPLEMENTATION

No constitution violations. All principles satisfied. Proceed to Phase 0 research.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli-phase1/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (technical decisions and rationale)
├── data-model.md        # Phase 1 output (Task entity definition)
├── quickstart.md        # Phase 1 output (how to run the app)
├── contracts/           # Phase 1 output (CLI interface contracts)
│   └── cli-interface.md # CLI command specifications
└── checklists/
    └── requirements.md  # Spec validation checklist (complete)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── models/
│   ├── __init__.py
│   └── task.py          # Task data model (dict-based)
├── services/
│   ├── __init__.py
│   └── task_manager.py  # Task CRUD operations
├── cli/
│   ├── __init__.py
│   ├── menu.py          # Main menu and user interaction
│   └── display.py       # Task list formatting and display
└── main.py              # Application entry point

tests/                   # Optional for Phase I
├── __init__.py
└── manual/
    └── test_scenarios.md  # Manual test cases from spec

pyproject.toml           # UV project configuration
README.md                # Project overview
.gitignore               # Git ignore patterns
```

**Structure Decision**: Single project structure selected because this is a standalone CLI application with no frontend/backend separation needed. The structure follows Python best practices with clear separation of concerns:
- `models/`: Data structures and validation
- `services/`: Business logic (task operations)
- `cli/`: User interface layer
- `tests/`: Manual test documentation

## Complexity Tracking

> No constitution violations detected. This section is empty.

## Phase 0: Research & Technical Decisions

### Research Tasks

1. **UV Project Initialization**: Best practices for initializing Python 3.13+ project with UV
2. **In-Memory Data Structure**: Optimal approach for storing tasks (list of dicts vs. list of objects)
3. **CLI Menu Pattern**: Standard patterns for interactive CLI menus in Python
4. **ID Generation Strategy**: Auto-increment implementation without database
5. **Input Validation**: Python standard library approaches for validating user input
6. **Error Handling**: CLI error display best practices

### Decisions Summary

(Detailed research findings will be documented in research.md)

**Key Technical Decisions**:
1. **Data Storage**: List of dictionaries for task storage (simple, no external dependencies)
2. **ID Strategy**: Counter variable for auto-incrementing IDs
3. **CLI Framework**: Native `input()` with numbered menu options (no external CLI library needed)
4. **Validation**: Built-in string methods for input validation
5. **Display**: Manual string formatting for task list display

## Phase 1: Design Artifacts

### Data Model

(Detailed entity definitions will be in data-model.md)

**Task Entity**:
- `id`: int (auto-assigned, auto-incremented)
- `title`: str (required, non-empty)
- `description`: str (optional, can be empty)
- `completed`: bool (default: False)

### CLI Interface Contracts

(Detailed contracts will be in contracts/cli-interface.md)

**Main Menu**:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Task Completion
6. Exit

**Operations**:
- Add: Prompt for title and optional description
- View: Display all tasks in table format
- Update: Prompt for ID, then title/description
- Delete: Prompt for ID, confirm removal
- Toggle: Prompt for ID, flip completion status

### Quickstart

(Detailed instructions will be in quickstart.md)

**Setup**:
```bash
# Install UV (if not already installed)
# Initialize project
uv init
uv add --dev pytest  # Optional for Phase I

# Run application
uv run python src/main.py
```

## Architecture Decisions

### 1. Three-Layer Architecture

**Decision**: Separate concerns into Models, Services, and CLI layers

**Rationale**:
- **Models** handle data structure and validation
- **Services** contain business logic (CRUD operations)
- **CLI** manages user interaction and display
- Clean separation enables future expansion (e.g., web interface, API)

**Alternatives Considered**:
- Single-file monolith: Rejected for poor maintainability
- MVC pattern: Overkill for CLI app, three layers sufficient

### 2. Dictionary-Based Task Storage

**Decision**: Store tasks as list of dictionaries rather than custom classes

**Rationale**:
- Simple and lightweight for Phase I
- No serialization complexity needed
- Easy to add/remove fields
- Sufficient for in-memory storage

**Alternatives Considered**:
- Dataclasses: More structure but adds complexity
- Pydantic models: External dependency violates Phase I constraints
- Plain tuples: Less readable, harder to extend

### 3. Interactive Menu CLI

**Decision**: Use numbered menu options with `input()` loops

**Rationale**:
- No external dependencies (standard library only)
- User-friendly for CLI applications
- Clear prompts meet FR-012 requirement
- Simple to implement and test

**Alternatives Considered**:
- argparse/click for command-line arguments: Less interactive, harder for users
- Rich library: External dependency violates Phase I constraints
- Curses library: Overly complex for simple menu

### 4. Auto-Incrementing ID Counter

**Decision**: Use a module-level counter variable incremented on each task creation

**Rationale**:
- Simple to implement
- IDs never reused (FR-013 requirement)
- No database needed
- Thread-safe for single-user single-session

**Alternatives Considered**:
- UUID: Overkill, harder for users to reference tasks
- Random integers: Risk of collisions, non-sequential
- Max ID + 1: Works but slightly more complex

### 5. No Persistence Layer

**Decision**: Tasks lost when application exits (no file saving)

**Rationale**:
- Phase I constraint: in-memory only
- Simplifies architecture
- Reduces error handling complexity
- Clear user expectation (document in quickstart)

**Alternatives Considered**:
- JSON file persistence: Violates Phase I constraints
- SQLite database: Violates Phase I constraints

## Implementation Phases

### Phase 0: Research (COMPLETE)
- ✅ Document technical decisions in research.md
- ✅ Validate UV setup approach
- ✅ Confirm data structure design

### Phase 1: Design (COMPLETE)
- ✅ Create data-model.md with Task entity
- ✅ Create contracts/cli-interface.md with CLI specifications
- ✅ Create quickstart.md with setup instructions
- ✅ Update agent context with project structure

### Phase 2: Implementation (NEXT)
- Run `/sp.tasks` to generate task breakdown
- Implement models layer (Task structure)
- Implement services layer (TaskManager CRUD)
- Implement CLI layer (menu, display)
- Manual testing against acceptance scenarios
- Final integration and polish

## Risk Assessment

### Technical Risks

**Risk 1**: User accidentally exits app and loses all tasks
- **Impact**: High (data loss)
- **Probability**: Medium
- **Mitigation**: Clear warning in startup message and README
- **Acceptance**: Expected Phase I behavior, document clearly

**Risk 2**: Large task lists (100+) difficult to navigate in CLI
- **Impact**: Medium (usability)
- **Probability**: Low (Phase I scope is small-scale)
- **Mitigation**: Acceptable for Phase I, future phases add pagination
- **Acceptance**: Within Phase I constraints

**Risk 3**: Input validation edge cases (special characters, very long titles)
- **Impact**: Low (UX degradation)
- **Probability**: Medium
- **Mitigation**: Implement basic validation, test with edge cases
- **Acceptance**: Handle with user-friendly error messages

### Process Risks

**Risk 4**: Scope creep (adding features beyond Phase I)
- **Impact**: High (delays, complexity)
- **Probability**: Low (strong constitution enforcement)
- **Mitigation**: Strict adherence to spec, constitution gate checks
- **Acceptance**: Any new features require spec amendment

## Success Criteria Validation

Mapping Success Criteria from spec to implementation plan:

- **SC-001**: Add task in < 2 seconds → Simple `input()` and list append
- **SC-002**: View list in < 1 second → Direct list iteration and print
- **SC-003**: All five operations work without errors → Error handling in each service method
- **SC-004**: 100% success for valid IDs → ID validation before operations
- **SC-005**: 100% error messages for invalid IDs → Custom error messages
- **SC-006**: Complete workflow without assistance → Clear menu prompts and instructions
- **SC-007**: Clear prompts for every action → Detailed prompt design in CLI layer
- **SC-008**: Handle 100+ tasks → Python list performance sufficient

All success criteria can be met with proposed architecture.

## Next Steps

1. **Generate Tasks**: Run `/sp.tasks` to create granular task breakdown
2. **Setup Project**: Initialize UV project structure
3. **Implement MVP**: Build P1 user story (Add and View tasks)
4. **Incremental Delivery**: Add P2, P3, P4 user stories sequentially
5. **Manual Testing**: Validate against acceptance scenarios
6. **Documentation**: Complete README with usage instructions

## Dependencies

- Python 3.13+ (system requirement)
- UV package manager (for project initialization)
- No external Python packages required for Phase I

## Assumptions

1. Users have Python 3.13+ installed
2. Users have UV package manager available
3. Users understand data is lost when app closes (documented in quickstart)
4. CLI environment supports UTF-8 for ✓ and ✗ symbols
5. Single user per session (no concurrency concerns)

---

**Plan Status**: ✅ COMPLETE - Ready for task generation via `/sp.tasks`
**Constitution Compliance**: ✅ ALL GATES PASSED
**Next Command**: `/sp.tasks` to break down implementation into granular tasks
