# Planner Skill

## Metadata
- **Name**: Planner
- **Version**: 1.0.0
- **Description**: Generates detailed architectural plans and task breakdowns from approved specifications
- **Category**: Planning & Architecture
- **Tags**: planning, architecture, task-breakdown, spec-driven-development

## Purpose
The Planner skill transforms approved specifications into actionable architectural plans and granular task lists. It bridges the gap between high-level requirements and implementation-ready work items.

## Responsibilities

### 1. Architectural Planning
- Analyze approved specs and extract technical requirements
- Make architectural decisions (frameworks, data structures, patterns)
- Define system components and their interactions
- Identify technical constraints and dependencies
- Document design rationale and trade-offs

### 2. Task Breakdown
- Decompose features into granular, testable tasks
- Establish task sequence and dependencies
- Define clear acceptance criteria for each task
- Include test cases and validation checkpoints
- Estimate complexity and identify risks

### 3. Technical Decisions
- Select appropriate data structures (e.g., in-memory list of dicts for tasks)
- Choose patterns and approaches (MVC, Repository, etc.)
- Define interfaces and contracts
- Plan error handling and edge cases
- Consider performance and scalability implications

## Inputs
- **spec.md**: Approved feature specification
- **constitution.md**: Project principles and standards
- **Existing codebase**: Current project structure and patterns

## Outputs
- **plan.md**: Detailed architectural plan including:
  - Technical approach and rationale
  - Component architecture
  - Data models and structures
  - Key decisions and trade-offs
  - Integration points
  - Risk assessment

- **tasks.md**: Granular task list including:
  - Numbered, ordered tasks
  - Clear acceptance criteria
  - Test cases for each task
  - Dependencies between tasks
  - Implementation notes and references

## Principles

### Clean Code
- Follow SOLID principles
- Prefer composition over inheritance
- Keep functions small and focused
- Use meaningful names
- Minimize coupling, maximize cohesion

### Python Best Practices
- Follow PEP 8 style guide
- Use type hints for clarity
- Leverage standard library when possible
- Structure projects logically (src/, tests/, docs/)
- Write docstrings for public interfaces

### Spec-Driven Development
- All decisions trace back to spec requirements
- No gold-plating or unnecessary features
- Clear acceptance criteria for verification
- Testable, incremental deliverables

## Execution Process

1. **Analyze Specification**
   - Read and understand approved spec.md
   - Identify functional and non-functional requirements
   - Note any ambiguities or missing details

2. **Review Context**
   - Check constitution.md for project principles
   - Examine existing codebase structure
   - Identify reusable patterns and components

3. **Make Architectural Decisions**
   - Choose appropriate technologies and patterns
   - Define data models and structures
   - Plan component interactions
   - Document rationale for significant decisions

4. **Create plan.md**
   - Write comprehensive architectural plan
   - Include diagrams if helpful (ASCII or Mermaid)
   - Document all key decisions
   - List assumptions and constraints
   - Identify risks and mitigations

5. **Generate tasks.md**
   - Break down implementation into tasks
   - Order tasks by dependency and priority
   - Write clear acceptance criteria
   - Include test cases
   - Add implementation hints

6. **Validate Outputs**
   - Ensure plan covers all spec requirements
   - Verify tasks are granular and testable
   - Check for missing dependencies
   - Confirm alignment with constitution

## Example Task Structure

```markdown
## Task 1: Create Task Data Structure
**Acceptance Criteria:**
- Define Task model with id, title, description, status, created_at
- Status enum: TODO, IN_PROGRESS, DONE
- Validate required fields

**Test Cases:**
- Can create task with all fields
- Can create task with minimal fields (id, title)
- Invalid status raises ValueError
- Missing required field raises error

**Implementation Notes:**
- Use dataclass or Pydantic model
- Store as list of dicts for simplicity
- Consider adding due_date field for future
```

## Quality Checklist

### Plan.md
- [ ] All spec requirements addressed
- [ ] Technical approach clearly explained
- [ ] Key decisions documented with rationale
- [ ] Data models defined
- [ ] Integration points identified
- [ ] Risks and mitigations listed
- [ ] Aligns with constitution principles

### Tasks.md
- [ ] Tasks are granular (< 2 hours each)
- [ ] Each task has clear acceptance criteria
- [ ] Test cases included for each task
- [ ] Dependencies clearly marked
- [ ] Tasks are ordered logically
- [ ] No ambiguous or vague tasks
- [ ] Implementation hints provided where helpful

## Common Patterns

### For CLI Applications
- Use argparse or click for command parsing
- Separate CLI layer from business logic
- Implement command pattern for actions
- Use rich or colorama for formatting

### For Data Management
- Define clear data models (dataclass, Pydantic)
- Use repository pattern for data access
- Keep business logic separate from storage
- Plan for validation at boundaries

### For Testing
- Unit tests for business logic
- Integration tests for workflows
- Use pytest fixtures for test data
- Mock external dependencies

## Anti-Patterns to Avoid

- ❌ Vague tasks like "Implement feature X"
- ❌ Tasks without acceptance criteria
- ❌ Missing dependencies between tasks
- ❌ Over-engineering simple solutions
- ❌ Ignoring existing project patterns
- ❌ Plans without technical rationale
- ❌ Tasks that are too large (> 4 hours)

## Invocation

This skill should be invoked:
- After spec is approved and ready for implementation
- When architectural guidance is needed
- Before starting implementation work
- When breaking down complex features

## Dependencies
- Requires approved spec.md
- Benefits from constitution.md context
- Should review existing codebase structure

## Success Criteria

A successful planning session produces:
1. **Complete Plan**: All spec requirements mapped to technical approach
2. **Actionable Tasks**: Developer can pick any task and implement it
3. **Clear Acceptance**: Each task has objective completion criteria
4. **Testable**: Each task includes specific test cases
5. **Ordered**: Tasks have logical sequence and dependencies
6. **Aligned**: Plan and tasks follow constitution principles

## Notes
- Focus on simplicity and clarity over sophistication
- Document the "why" behind decisions, not just the "what"
- Consider maintainability and future extensibility
- Balance thoroughness with avoiding analysis paralysis
- Prefer incremental delivery over big-bang implementation
