---
id: 001
title: Create Todo App Constitution Phase I
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "phase-i", "todo-app", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

# Todo App Constitution (Phase I)

## Purpose
Define rules for building a Python in-memory Todo CLI app.

## Core Principles
- ✅ Specs must be refined until correct output is produced
- ✅ One feature = one clear spec
- ✅ Python clean code & readable structure

## Scope (Phase I Only)
- In-memory storage (no DB, no files)
- Console-based interaction
- Single-user, single-session

## Mandatory Features
- Add Task
- View Task List
- Update Task
- Delete Task
- Mark Task as Complete / Incomplete

## Constraints
- UV
- Python 3.13+
- CLI only
- Tasks identified by unique ID
- No external services

## Definition of Done
- App runs without errors
- All basic features work via CLI
- Code follows spec exactly

## Response snapshot

Created comprehensive Todo App Constitution (v1.0.0) with 5 core principles:

1. **Spec-Driven Refinement**: Specifications must be refined until correct output is produced
2. **Clean Code & Readability**: Python clean code principles mandatory
3. **Single-Feature Scope**: One feature = one clear spec
4. **Phase I Constraints (NON-NEGOTIABLE)**: In-memory, CLI-only, Python 3.13+, UV, single-session
5. **CLI-Only Interaction**: Console-based with unique task IDs

Key sections:
- **Mandatory Features**: Add, View, Update, Delete, Mark Complete/Incomplete
- **Technology Stack**: Python 3.13+, UV, standard library preferred
- **Development Workflow**: Spec-first approach with 6-step process
- **Code Standards**: PEP 8, type hints, <20 line functions, docstrings
- **Definition of Done**: 6 clear acceptance criteria
- **Governance**: Amendment process, compliance rules, semantic versioning

Constitution file created at `.specify/memory/constitution.md` with Sync Impact Report embedded.

## Outcome

- ✅ Impact: Constitution v1.0.0 ratified for Todo App Phase I development. Establishes clear governance and technical constraints.
- 🧪 Tests: None (governance document)
- 📁 Files: 1 created (.specify/memory/constitution.md)
- 🔁 Next prompts: Create feature spec for first mandatory feature (e.g., Add Task), run /sp.specify
- 🧠 Reflection: Constitution successfully defines Phase I boundaries with NON-NEGOTIABLE constraints. All templates reviewed for alignment - no changes needed. Ready for spec creation.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All placeholders filled, version set to 1.0.0, dates formatted correctly, principles clear and testable
- Prompt variant (if applicable): Standard constitution creation
- Next experiment (smallest change to try): None - baseline constitution established successfully
