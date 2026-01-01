# Tasks: Todo CLI App (Phase I)

**Input**: Design documents from `/specs/001-todo-cli-phase1/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/cli-interface.md

**Tests**: Manual CLI testing only for Phase I (no automated tests generated)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize Python 3.13+ project with UV (run `uv init --python 3.13` main folder name todo-cli-app at project root)
- [ ] T002 Create source directory structure: src/, src/models/, src/services/, src/cli/
- [ ] T003 [P] Create __init__.py files in src/, src/models/, src/services/, src/cli/
- [ ] T004 [P] Create pyproject.toml with project metadata (name: todo-cli-app, requires-python: ">=3.13")
- [ ] T005 [P] Create README.md with project overview and Phase I constraints note
- [ ] T006 [P] Create .gitignore for Python projects (include __pycache__, *.pyc, .venv, .python-version)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Create Task validation module in src/models/task.py with type hints
- [ ] T008 [P] Implement validate_title() function in src/models/task.py (returns tuple[bool, str])
- [ ] T009 [P] Implement validate_description() function in src/models/task.py (returns tuple[bool, str])
- [ ] T010 [P] Implement validate_task_id() function in src/models/task.py (returns tuple[bool, int, str])
- [ ] T011 Create TaskManager service in src/services/task_manager.py with module-level _tasks list and _next_id counter
- [ ] T012 Create CLI display module in src/cli/display.py with type hints
- [ ] T013 Implement display_tasks() function in src/cli/display.py (handles empty list, shows table with ID, Status, Title, Description)
- [ ] T014 Create main menu module in src/cli/menu.py with type hints
- [ ] T015 Implement display_main_menu() function in src/cli/menu.py (shows 6 options with proper formatting)
- [ ] T016 Implement get_user_choice() function in src/cli/menu.py (validates choice 1-6, re-prompts on error)
- [ ] T017 Create application entry point in src/main.py with main() function and if __name__ == "__main__" guard
- [ ] T018 Implement startup message in src/main.py (warning about in-memory storage)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can add tasks with title and optional description, then view all tasks with IDs and completion status

**Independent Test**: Launch app, add 3 tasks (some with descriptions, some without), view list showing all tasks with IDs, titles, and status indicators (✗ for all since newly created)

### Implementation for User Story 1

- [ ] T019 [P] [US1] Implement add_task() function in src/services/task_manager.py (validates title, creates dict with id/title/description/completed, appends to _tasks, increments _next_id, returns task)
- [ ] T020 [P] [US1] Implement get_all_tasks() function in src/services/task_manager.py (returns copy of _tasks list)
- [ ] T021 [US1] Implement handle_add_task() function in src/cli/menu.py (prompts for title, validates, prompts for description, calls add_task(), displays confirmation)
- [ ] T022 [US1] Implement handle_view_tasks() function in src/cli/menu.py (calls get_all_tasks(), calls display_tasks())
- [ ] T023 [US1] Integrate add_task and view_tasks handlers into main menu loop in src/main.py (handle choices 1 and 2)
- [ ] T024 [US1] Add error handling for empty title in handle_add_task() in src/cli/menu.py (display "Title cannot be empty", re-prompt)
- [ ] T025 [US1] Test complete User Story 1 workflow manually: add 3 tasks, view list, verify IDs are sequential, verify all show as incomplete

**Checkpoint**: User Story 1 complete - application has MVP functionality (add and view tasks)

---

## Phase 4: User Story 2 - Mark Tasks Complete or Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status to track progress

**Independent Test**: Add tasks using US1, mark task ID 1 as complete, view list showing ✓ for task 1, mark task ID 1 as incomplete, verify ✗ status

### Implementation for User Story 2

- [ ] T026 [P] [US2] Implement find_task_by_id() helper function in src/services/task_manager.py (searches _tasks, returns task dict or None)
- [ ] T027 [US2] Implement toggle_task_completion() function in src/services/task_manager.py (finds task, toggles completed boolean, returns tuple[bool, str, bool] for success/message/new_status)
- [ ] T028 [US2] Implement handle_toggle_completion() function in src/cli/menu.py (prompts for ID, validates ID format, calls toggle_task_completion(), displays success/error message with new status)
- [ ] T029 [US2] Integrate toggle completion handler into main menu loop in src/main.py (handle choice 5)
- [ ] T030 [US2] Add error handling for non-existent task ID in handle_toggle_completion() in src/cli/menu.py (display "Task ID {id} not found")
- [ ] T031 [US2] Add error handling for non-numeric ID in handle_toggle_completion() in src/cli/menu.py (display "Invalid ID: must be a positive number")
- [ ] T032 [US2] Test complete User Story 2 workflow manually: add 2 tasks, mark ID 1 complete, verify ✓ status, toggle back to incomplete, verify ✗ status, test invalid ID

**Checkpoint**: User Story 2 complete - users can track task completion independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: Users can edit task title and description to correct mistakes or add information

**Independent Test**: Add task using US1, update task ID 1 title to "New Title", verify change, update description, verify change, test with Enter key to keep current values

### Implementation for User Story 3

- [ ] T033 [US3] Implement update_task() function in src/services/task_manager.py (finds task, validates new title if provided, updates title/description, returns tuple[bool, str])
- [ ] T034 [US3] Implement handle_update_task() function in src/cli/menu.py (prompts for ID, validates ID, displays current task, prompts for new title with "press Enter to keep current", prompts for new description, calls update_task(), displays confirmation)
- [ ] T035 [US3] Integrate update task handler into main menu loop in src/main.py (handle choice 3)
- [ ] T036 [US3] Add logic to keep current values when user presses Enter in handle_update_task() in src/cli/menu.py
- [ ] T037 [US3] Add error handling for empty new title in handle_update_task() in src/cli/menu.py (display error, keep previous title)
- [ ] T038 [US3] Add error handling for non-existent task ID in handle_update_task() in src/cli/menu.py (display "Task ID {id} not found")
- [ ] T039 [US3] Test complete User Story 3 workflow manually: add task, update title only, update description only, update both, test Enter to keep current, test invalid ID

**Checkpoint**: User Story 3 complete - users can edit task details independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Users can remove tasks to keep list clean and focused

**Independent Test**: Add 3 tasks using US1, delete task ID 2, view list showing only IDs 1 and 3, delete last task, verify empty list message

### Implementation for User Story 4

- [ ] T040 [US4] Implement delete_task() function in src/services/task_manager.py (finds task, removes from _tasks, returns tuple[bool, str])
- [ ] T041 [US4] Implement handle_delete_task() function in src/cli/menu.py (prompts for ID, validates ID, displays task details, prompts for y/n confirmation, calls delete_task() if confirmed, displays result)
- [ ] T042 [US4] Integrate delete task handler into main menu loop in src/main.py (handle choice 4)
- [ ] T043 [US4] Add confirmation prompt logic in handle_delete_task() in src/cli/menu.py (only delete on 'y' or 'Y', cancel on any other input)
- [ ] T044 [US4] Add error handling for non-existent task ID in handle_delete_task() in src/cli/menu.py (display "Task ID {id} not found")
- [ ] T045 [US4] Test complete User Story 4 workflow manually: add 3 tasks, delete middle task, verify list, delete with 'n' response, verify not deleted, delete last task, verify empty list

**Checkpoint**: User Story 4 complete - all user stories now functional independently

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final touches

- [ ] T046 [P] Implement exit handler in src/cli/menu.py (displays goodbye message, returns exit signal)
- [ ] T047 Integrate exit handler into main menu loop in src/main.py (handle choice 6, break from loop)
- [ ] T048 [P] Add KeyboardInterrupt handling in src/main.py (catch Ctrl+C, display goodbye message gracefully)
- [ ] T049 [P] Add input validation for title length (max 200 chars) in src/models/task.py validate_title()
- [ ] T050 [P] Add input validation for description length (max 500 chars) in src/models/task.py validate_description()
- [ ] T051 [P] Implement display_startup_message() function in src/cli/display.py (warning about data loss on exit)
- [ ] T052 Refine display_tasks() formatting in src/cli/display.py (ensure proper column alignment, truncate long titles/descriptions)
- [ ] T053 Add UTF-8 symbols (✓ and ✗) for status display in src/cli/display.py
- [ ] T054 Update README.md with usage instructions, Phase I limitations, and quickstart link
- [ ] T055 Create tests/manual/test_scenarios.md with manual test cases from spec acceptance scenarios
- [ ] T056 Run complete manual testing of all 4 user stories end-to-end (follow test_scenarios.md)
- [ ] T057 Verify all success criteria from spec.md: add task < 2s, view < 1s, 100% error messages, workflow without assistance
- [ ] T058 Final code review for PEP 8 compliance, type hints, function length < 20 lines, meaningful names

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 functionality but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Uses US1 to add tasks but independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Uses US1 to add tasks but independently testable

### Within Each User Story

- Foundation tasks (T007-T018) MUST complete before any user story tasks
- Within each user story phase:
  - Service layer tasks before CLI handlers
  - CLI handlers before main menu integration
  - Error handling after core functionality
  - Manual testing last
- Tasks marked [P] can run in parallel within their phase

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003, T004, T005, T006)
- All Foundational validation functions can run in parallel (T008, T009, T010)
- Once Foundational phase completes, all user stories (T019-T045) can start in parallel if team capacity allows
- All Polish tasks marked [P] can run in parallel (T046, T048, T049, T050, T051, T053)

---

## Parallel Example: Foundational Phase

```bash
# Launch foundational validation functions together:
Task: "Implement validate_title() in src/models/task.py"
Task: "Implement validate_description() in src/models/task.py"
Task: "Implement validate_task_id() in src/models/task.py"
```

## Parallel Example: User Story 1

```bash
# Launch service functions together (different components, no dependencies):
Task: "Implement add_task() in src/services/task_manager.py"
Task: "Implement get_all_tasks() in src/services/task_manager.py"
```

## Parallel Example: After Foundational Complete

```bash
# Launch all user stories in parallel (if team has 4 developers):
Developer A: Phase 3 - User Story 1 (T019-T025)
Developer B: Phase 4 - User Story 2 (T026-T032)
Developer C: Phase 5 - User Story 3 (T033-T039)
Developer D: Phase 6 - User Story 4 (T040-T045)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T018)
3. Complete Phase 3: User Story 1 (T019-T025)
4. **STOP and VALIDATE**: Test US1 independently - add and view tasks
5. Deploy/demo if ready (working todo list app!)

### Incremental Delivery (Recommended)

1. Complete Setup (Phase 1) + Foundational (Phase 2) → Foundation ready
2. Add User Story 1 (Phase 3) → Test independently → Deploy/Demo (MVP! ✓)
3. Add User Story 2 (Phase 4) → Test independently → Deploy/Demo (Completion tracking ✓)
4. Add User Story 3 (Phase 5) → Test independently → Deploy/Demo (Editing ✓)
5. Add User Story 4 (Phase 6) → Test independently → Deploy/Demo (Deletion ✓)
6. Add Polish (Phase 7) → Final validation → Production release
7. Each story adds value without breaking previous stories

### Parallel Team Strategy (4 Developers)

With multiple developers:

1. **Team completes Setup + Foundational together** (T001-T018)
2. **Once Foundational is done**:
   - Developer A: User Story 1 (T019-T025)
   - Developer B: User Story 2 (T026-T032)
   - Developer C: User Story 3 (T033-T039)
   - Developer D: User Story 4 (T040-T045)
3. **Stories complete and integrate independently**
4. **Team tackles Polish together** (T046-T058)

---

## Task Summary

**Total Tasks**: 58

**By Phase**:
- Phase 1 (Setup): 6 tasks
- Phase 2 (Foundational): 12 tasks (BLOCKING)
- Phase 3 (User Story 1 - P1): 7 tasks
- Phase 4 (User Story 2 - P2): 7 tasks
- Phase 5 (User Story 3 - P3): 7 tasks
- Phase 6 (User Story 4 - P4): 6 tasks
- Phase 7 (Polish): 13 tasks

**By User Story**:
- Setup + Foundation: 18 tasks (shared infrastructure)
- User Story 1 (Add/View): 7 tasks
- User Story 2 (Toggle Complete): 7 tasks
- User Story 3 (Update): 7 tasks
- User Story 4 (Delete): 6 tasks
- Polish: 13 tasks

**Parallel Opportunities**: 16 tasks marked [P] can run in parallel

**Independent Test Criteria**:
- US1: Add 3 tasks, view list (MVP!)
- US2: Add tasks, toggle completion, verify status changes
- US3: Add task, update title/description, verify changes
- US4: Add 3 tasks, delete one, verify removal

**Suggested MVP Scope**: Phases 1-3 (Setup + Foundation + User Story 1) = 25 tasks for working todo list app

---

## Notes

- [P] tasks = different files, no dependencies (can run in parallel)
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- **Phase I**: Manual testing only (no pytest, no automated tests)
- **Type hints**: Use throughout (e.g., `list[dict]`, `tuple[bool, str]`, `Optional[str]`)
- **PEP 8**: Follow style guide (flake8/black can be used for formatting)
- **Functions**: Keep under 20 lines where practical
- **Error handling**: User-friendly messages, never crash on invalid input

---

**Tasks Status**: ✅ READY FOR IMPLEMENTATION
**Format Validation**: ✅ ALL TASKS FOLLOW CHECKLIST FORMAT
**Organization**: ✅ ORGANIZED BY USER STORY
**Independence**: ✅ EACH STORY INDEPENDENTLY TESTABLE
**Next Command**: Start with Phase 1 (T001-T006) or MVP scope (T001-T025)
