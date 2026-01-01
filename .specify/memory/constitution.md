<!--
Sync Impact Report:
- Version change: [INITIAL] → 1.0.0
- New constitution created from template
- Principles defined:
  1. Spec-Driven Refinement
  2. Clean Code & Readability
  3. Single-Feature Scope
  4. In-Memory Phase I Constraints
  5. CLI-Only Interaction
- Templates requiring updates:
  ✅ Constitution created
  ⚠ spec-template.md - Pending review for alignment
  ⚠ plan-template.md - Pending review for alignment
  ⚠ tasks-template.md - Pending review for alignment
- Follow-up TODOs: Review dependent templates for Phase I constraints alignment
-->

# Todo App Constitution (Phase I)

## Purpose

Define the governing rules for building a Python in-memory Todo CLI application. This constitution establishes the foundation for Phase I development, ensuring code quality, architectural consistency, and clear feature boundaries.

## Core Principles

### I. Spec-Driven Refinement

Specifications MUST be refined iteratively until they produce correct output. No implementation begins until the spec is approved and unambiguous.

**Rationale**: Prevents scope creep, reduces rework, and ensures shared understanding between all stakeholders before code is written.

### II. Clean Code & Readability

All Python code MUST follow clean code principles: meaningful names, single responsibility, small functions, and clear structure. Code is written for humans first, machines second.

**Rationale**: Maintainability and team collaboration depend on readable, well-structured code. Technical debt begins with unclear code.

### III. Single-Feature Scope

One feature equals one clear specification. Features MUST NOT be bundled or interdependent beyond explicit requirements.

**Rationale**: Enables parallel development, simplifies testing, and allows incremental delivery without artificial dependencies.

### IV. Phase I Constraints (NON-NEGOTIABLE)

Phase I implementation MUST adhere to:
- In-memory storage only (no database, no file persistence)
- Console-based interaction only
- Single-user, single-session design
- Python 3.13+ with UV package manager
- No external services or APIs

**Rationale**: Establishes a working MVP foundation before adding complexity. These constraints define the Phase I boundary and MUST NOT be violated.

### V. CLI-Only Interaction

All user interaction MUST occur through command-line interface. Tasks MUST be identified by unique IDs. The application runs as a console program with text input/output.

**Rationale**: Simplifies initial implementation, enables automation, and provides a stable interface for future GUI/API layers.

## Mandatory Features (Phase I)

The following features MUST be implemented and fully functional:

1. **Add Task**: Create a new task with title and optional description
2. **View Task List**: Display all tasks with their status and IDs
3. **Update Task**: Modify existing task title or description by ID
4. **Delete Task**: Remove a task by ID
5. **Mark Complete/Incomplete**: Toggle task completion status by ID

**Acceptance**: All five features MUST work via CLI without errors before Phase I is considered complete.

## Technology Stack

- **Language**: Python 3.13 or higher (REQUIRED)
- **Package Manager**: UV (REQUIRED)
- **Storage**: In-memory data structures (list of dicts or similar)
- **Interface**: Command-line only
- **Dependencies**: Standard library preferred; minimize external packages

**Rationale**: UV provides fast, reliable dependency management. Python 3.13+ ensures access to latest language features and security updates.

## Development Workflow

### Spec-First Approach

1. Write or refine specification for feature
2. Get spec approval
3. Create architectural plan
4. Break down into granular tasks
5. Implement tasks incrementally
6. Validate against spec acceptance criteria

### Code Standards

- Follow PEP 8 style guide
- Use type hints for function signatures
- Keep functions under 20 lines where practical
- Write docstrings for public interfaces
- No magic numbers or unexplained constants

### Testing Requirements

- Each feature MUST have test cases defined in tasks
- Tests validate spec acceptance criteria
- Manual testing via CLI MUST pass before completion
- No untested code merged

## Definition of Done

A feature or phase is considered complete when:

1. ✅ Application runs without errors
2. ✅ All mandatory features work via CLI
3. ✅ Code follows this constitution exactly
4. ✅ Implementation matches approved spec
5. ✅ All acceptance criteria validated
6. ✅ No placeholder or TODO code remaining

## Governance

### Authority

This constitution supersedes all other development practices, preferences, or conventions. When in doubt, refer to this document.

### Amendments

Constitution amendments MUST:
- Document clear rationale for change
- Identify affected specs, plans, and code
- Include migration plan if breaking changes introduced
- Update version following semantic versioning (MAJOR.MINOR.PATCH)

### Compliance

- All PRs/commits MUST verify compliance with this constitution
- Violations MUST be corrected before merge
- Complexity or deviation MUST be explicitly justified in writing
- Team members can challenge non-compliance at any time

### Version Control

- **MAJOR**: Backward incompatible principle changes or removals
- **MINOR**: New principles added or materially expanded guidance
- **PATCH**: Clarifications, wording fixes, non-semantic refinements

---

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
