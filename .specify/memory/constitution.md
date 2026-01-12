<!--
Sync Impact Report:
- Version change: 1.0.0 → 2.0.0
- Updated constitution to reflect multi-phase evolution
- Principles revised for multi-phase development:
  1. Spec-Driven Refinement
  2. Clean Code & Readability
  3. Single-Feature Scope
  4. Multi-Phase Evolution Strategy
  5. Technology Stack Continuity
- Templates requiring updates:
  ✅ Constitution updated
  ⚠ spec-template.md - Pending review for multi-phase alignment
  ⚠ plan-template.md - Pending review for multi-phase alignment
  ⚠ tasks-template.md - Pending review for multi-phase alignment
- Follow-up TODOs: Review dependent templates for multi-phase constraints alignment
-->

# Todo App Constitution (Multi-Phase Evolution)

## Purpose

Define the governing rules for building a multi-phase Todo application that evolves from a console app to a full-stack web application with AI chatbot and Kubernetes deployment. This constitution establishes the foundation for iterative development across multiple phases, ensuring code quality, architectural consistency, and clear feature boundaries at each stage.

## Core Principles

### I. Spec-Driven Refinement

Specifications MUST be refined iteratively until they produce correct output. No implementation begins until the spec is approved and unambiguous.

**Rationale**: Prevents scope creep, reduces rework, and ensures shared understanding between all stakeholders before code is written.

### II. Clean Code & Readability

All code MUST follow clean code principles: meaningful names, single responsibility, small functions, and clear structure. Code is written for humans first, machines second.

**Rationale**: Maintainability and team collaboration depend on readable, well-structured code. Technical debt begins with unclear code.

### III. Single-Feature Scope

One feature equals one clear specification. Features MUST NOT be bundled or interdependent beyond explicit requirements.

**Rationale**: Enables parallel development, simplifies testing, and allows incremental delivery without artificial dependencies.

### IV. Multi-Phase Evolution Strategy (NON-NEGOTIABLE)

Implementation MUST follow the defined phase progression:
- **Phase I**: Console App (Python 3.13+, UV, In-memory storage)
- **Phase II**: Web Application (Next.js 16+, FastAPI, Neon PostgreSQL, Better Auth JWT)
- **Phase III**: AI Chatbot (OpenAI ChatKit, OpenAI Agents SDK, MCP SDK)
- **Phase IV**: Kubernetes (Docker, Minikube, Helm Charts, kubectl-ai)
- **Phase V**: Production Deployment (Cloud infrastructure, monitoring, CI/CD)

**Rationale**: Ensures systematic complexity addition, validates foundations before building upon them, and enables iterative delivery with working software at each phase.

### V. Technology Stack Continuity

Each phase MUST maintain compatibility with previous phases where applicable and follow the defined technology stack:
- **Phase I**: Python 3.13+, UV package manager, in-memory storage
- **Phase II**: Next.js 16+ (App Router), FastAPI, SQLModel, Neon PostgreSQL, Better Auth (JWT)
- **Phase III**: OpenAI ChatKit, OpenAI Agents SDK, Model Context Protocol (MCP) tools
- **Phase IV**: Docker, Minikube, Helm Charts, kubectl-ai, Kagent

**Rationale**: Maintains consistent development experience, reduces context switching, and ensures smooth phase transitions.

## Mandatory Features by Phase

### Phase I: Console App
The following features MUST be implemented and fully functional:
1. **Add Task**: Create a new task with title and optional description
2. **View Task List**: Display all tasks with their status and IDs
3. **Update Task**: Modify existing task title or description by ID
4. **Delete Task**: Remove a task by ID
5. **Mark Complete/Incomplete**: Toggle task completion status by ID

**Acceptance**: All five features MUST work via CLI without errors before Phase I is considered complete.

### Phase II: Web Application
The following features MUST be implemented and fully functional:
1. **User Authentication**: Secure login/logout with JWT tokens
2. **Task CRUD Operations**: Create, Read, Update, Delete tasks via web interface
3. **User Isolation**: Tasks are isolated by user ID in database
4. **Responsive UI**: Works on desktop and mobile devices
5. **Real-time Updates**: Live task list updates across sessions

**Acceptance**: All features MUST work via web interface with proper authentication before Phase II is considered complete.

### Phase III: AI Chatbot
The following features MUST be implemented and fully functional:
1. **Task Management Commands**: Add_task, list_tasks, complete_task, delete_task, update_task via natural language
2. **Stateless Architecture**: Proper persistence with database backend
3. **Natural Language Processing**: Understand user intents and extract parameters
4. **Conversation Context**: Maintain conversation history and context
5. **Error Handling**: Graceful handling of invalid commands and edge cases

**Acceptance**: All MCP tools MUST work reliably with natural language interface before Phase III is considered complete.

### Phase IV: Kubernetes
The following features MUST be implemented and fully functional:
1. **Container Orchestration**: Deploy application components using Kubernetes
2. **Service Discovery**: Proper networking between frontend, backend, and database
3. **Configuration Management**: Manage environment variables and secrets securely
4. **Scaling**: Horizontal pod autoscaling based on demand
5. **Monitoring**: Health checks and metrics collection

**Acceptance**: Application MUST run reliably in Kubernetes cluster before Phase IV is considered complete.

## Technology Stack

### Phase I (Console App)
- **Language**: Python 3.13 or higher (REQUIRED)
- **Package Manager**: UV (REQUIRED)
- **Storage**: In-memory data structures (list of dicts or similar)
- **Interface**: Command-line only
- **Dependencies**: Standard library preferred; minimize external packages

### Phase II (Web Application)
- **Frontend**: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python 3.11+, SQLModel, Pydantic
- **Database**: Neon PostgreSQL with connection pooling
- **Authentication**: Better Auth with JWT tokens
- **Package Manager**: npm/pnpm for frontend, UV for backend

### Phase III (AI Chatbot)
- **Framework**: OpenAI ChatKit, OpenAI Agents SDK
- **Protocol**: Model Context Protocol (MCP) for tool integration
- **Tools**: Custom MCP tools for task management (add_task, list_tasks, etc.)
- **Persistence**: Database-backed conversation storage
- **Interface**: Natural language processing and response generation

### Phase IV (Kubernetes)
- **Containerization**: Docker with multi-stage builds
- **Orchestration**: Kubernetes with Minikube for local development
- **Packaging**: Helm Charts for deployment configuration
- **CLI**: kubectl-ai for enhanced Kubernetes interactions
- **Automation**: Kagent for AI-assisted Kubernetes operations

**Rationale**: Each stack is chosen for its specific strengths in the respective phase while maintaining continuity and developer productivity.

## Development Workflow

### Spec-First Approach

1. Write or refine specification for feature
2. Get spec approval
3. Create architectural plan
4. Break down into granular tasks
5. Implement tasks incrementally
6. Validate against spec acceptance criteria
7. Transition to next phase only after current phase completion

### Code Standards

- Follow PEP 8 style guide for Python, ESLint/TypeScript standards for frontend
- Use type hints for function signatures and interfaces
- Keep functions under 20 lines where practical
- Write docstrings for public interfaces
- No magic numbers or unexplained constants
- Consistent naming conventions across all phases

### Testing Requirements

- Each feature MUST have test cases defined in tasks
- Tests validate spec acceptance criteria
- Manual testing via appropriate interface (CLI/web/NLP) MUST pass before completion
- Unit, integration, and end-to-end tests where applicable
- No untested code merged

## Definition of Done

A feature or phase is considered complete when:

1. ✅ Application runs without errors
2. ✅ All mandatory features work via appropriate interface
3. ✅ Code follows this constitution exactly
4. ✅ Implementation matches approved spec
5. ✅ All acceptance criteria validated
6. ✅ No placeholder or TODO code remaining
7. ✅ Tests pass and coverage meets minimum threshold
8. ✅ Documentation updated for new features

## Governance

### Authority

This constitution supersedes all other development practices, preferences, or conventions. When in doubt, refer to this document.

### Amendments

Constitution amendments MUST:
- Document clear rationale for change
- Identify affected specs, plans, and code
- Include migration plan if breaking changes introduced
- Update version following semantic versioning (MAJOR.MINOR.PATCH)
- Consider impact across all phases, not just current phase

### Compliance

- All PRs/commits MUST verify compliance with this constitution
- Violations MUST be corrected before merge
- Complexity or deviation MUST be explicitly justified in writing
- Team members can challenge non-compliance at any time
- Phase transition requires explicit approval and completion verification

### Version Control

- **MAJOR**: Backward incompatible principle changes or removals, new phases added
- **MINOR**: New principles added or materially expanded guidance for existing phases
- **PATCH**: Clarifications, wording fixes, non-semantic refinements

---

**Version**: 2.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-12
