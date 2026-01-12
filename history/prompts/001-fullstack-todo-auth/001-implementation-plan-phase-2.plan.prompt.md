---
id: 001
title: Implementation Plan Phase 2
stage: plan
date: 2026-01-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-fullstack-todo-auth
branch: 001-fullstack-todo-auth
user: user
command: /sp.plan
labels: ["spec-driven-development", "fullstack", "todo-app", "auth"]
links:
  spec: ./spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-fullstack-todo-auth/plan.md
  - specs/001-fullstack-todo-auth/research.md
  - specs/001-fullstack-todo-auth/data-model.md
  - specs/001-fullstack-todo-auth/contracts/api-contract.yaml
  - specs/001-fullstack-todo-auth/quickstart.md
  - CLAUDE.md
tests:
  - No tests run during planning phase
---

## Prompt

# Implementation fullstack-todo-auth Plan – Phase II

## Step 1: Specification
- Define architecture, API, DB schema, auth flow
- Write specs under /specs (features, api, database, ui)

## Step 2: Auth Integration
- Configure Better Auth with JWT plugin
- Define JWT claims and expiry
- Document shared secret usage

## Step 3: Backend
- Setup FastAPI project
- Implement SQLModel schemas
- Add JWT verification middleware
- Implement REST API endpoints

## Step 4: Frontend
- Build Next.js App Router structure
- Implement auth UI (signup/signin)
- Create task management UI
- Attach JWT to API requests

## Step 5: Validation
- Verify user isolation
- Test CRUD + auth flow
- Ensure specs match implementation

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

# AGENTS.md
Here is a **significantly improved, clearer, more actionable, more valuable** version of your **AGENTS.md**.
I kept the spirit but made it *practical*, *strict*, and *agent-compatible*, so Claude/Gemini/Copilot can actually follow it in real workflows.

---

# **AGENTS.md**

## **Purpose**

This project uses **Spec-Driven Development (SDD)** — a workflow where **no agent is allowed to write code until the specification is complete and approved**.
All AI agents (Claude, Copilot, Gemini, local LLMs, etc.) must follow the **Spec-Kit lifecycle**:

> **Specify → Plan → Tasks → Implement**

This prevents “vibe coding,” ensures alignment across agents, and guarantees that every implementation step maps back to an explicit requirement.

---

## **How Agents Must Work**

Every agent in this project MUST obey these rules:

1. **Never generate code without a referenced Task ID.**
2. **Never modify architecture without updating `speckit.plan`.**
3. **Never propose features without updating `speckit.specify` (WHAT).**
4. **Never change approach without updating `speckit.constitution` (Principles).**
5. **Every code file must contain a comment linking it to the Task and Spec sections.**

If an agent cannot find the required spec, it must **stop and request it**, not improvise.

---

## **Spec-Kit Workflow (Source of Truth)**

### **1. Constitution (WHY — Principles & Constraints)**

File: `speckit.constitution`
Defines the project’s non-negotiables: architecture values, security rules, tech stack constraints, performance expectations, and patterns allowed.

Agents must check this before proposing solutions.

---

### **2. Specify (WHAT — Requirements, Journeys & Acceptance Criteria)**

File: `speckit.specify`

Contains:

* User journeys
* Requirements
* Acceptance criteria
* Domain rules
* Business constraints

Agents must not infer missing requirements — they must request clarification or propose specification updates.

---

### **3. Plan (HOW — Architecture, Components, Interfaces)**

File: `speckit.plan`

Includes:

* Component breakdown
* APIs & schema diagrams
* Service boundaries
* System responsibilities
* High-level sequencing

All architectural output MUST be generated from the Specify file.

---

### **4. Tasks (BREAKDOWN — Atomic, Testable Work Units)**

File: `speckit.tasks`

Each Task must contain:

* Task ID
* Clear description
* Preconditions
* Expected outputs
* Artifacts to modify
* Links back to Specify + Plan sections

Agents **implement only what these tasks define**.

---

### **5. Implement (CODE — Write Only What the Tasks Authorize)**

Agents now write code, but must:

* Reference Task IDs
* Follow the Plan exactly
* Not invent new features or flows
* Stop and request clarification if anything is underspecified

> The golden rule: **No task = No code.**

---

## **Agent Behavior in This Project**

### **When generating code:**

Agents must reference:

```
[Task]: T-001
[From]: speckit.specify §2.1, speckit.plan §3.4
```

### **When proposing architecture:**

Agents must reference:

```
Update required in speckit.plan → add component X
```

### **When proposing new behavior or a new feature:**

Agents must reference:

```
Requires update in speckit.specify (WHAT)
```

### **When changing principles:**

Agents must reference:

```
Modify constitution.md → Principle #X
```

---

## **Agent Failure Modes (What Agents MUST Avoid)**

Agents are NOT allowed to:

* Freestyle code or architecture
* Generate missing requirements
* Create tasks on their own
* Alter stack choices without justification
* Add endpoints, fields, or flows that aren’t in the spec
* Ignore acceptance criteria
* Produce “creative” implementations that violate the plan

If a conflict arises between spec files, the **Constitution > Specify > Plan > Tasks** hierarchy applies.

---

## **Developer–Agent Alignment**

Humans and agents collaborate, but the **spec is the single source of truth**.
Before every session, agents should re-read:

1. `.memory/constitution.md`

This ensures predictable, deterministic development.


      IMPORTANT: this context may or may not be relevant to your tasks. You should not respond to this context unless it is highly relevant to your task.