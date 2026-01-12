---
id: 002
title: Generate Tasks for Full-Stack Todo Application
stage: tasks
date: 2026-01-07
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-fullstack-todo-auth
branch: 001-fullstack-todo-auth
user: user
command: sp.tasks
labels: ["tasks", "user-stories", "spec-kit", "organization"]
links:
  spec: ../specs/001-fullstack-todo-auth/spec.md
  plan: ../specs/001-fullstack-todo-auth/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-fullstack-todo-auth/tasks.md
tests:
  - No tests included (not explicitly requested in feature specification)
---

## Prompt

# Task Breakdown – Phase II

## Specs
- Write system architecture spec
- Write REST API endpoint spec
- Write database schema spec
- Write authentication flow spec
- Write UI components & pages spec

## Backend Tasks
- Setup FastAPI + SQLModel
- Configure Neon PostgreSQL connection
- Implement JWT verification middleware
- Implement task CRUD endpoints
- Enforce user-based data filtering

## Frontend Tasks
- Setup Next.js App Router
- Integrate Better Auth with JWT
- Build auth pages
- Build task dashboard
- Attach Authorization header to API calls

## DevOps
- Setup env variables
- Configure monorepo structure
- Ensure Claude Code instructions per service

## Response snapshot

I'll help you generate the tasks.md file for Phase II. Let me start by running the prerequisites check and then work through the task generation workflow.

<tool_call>
<function=Bash>
<parameter=command>
.specify/scripts/powershell/check-prerequisites.ps1 -Json