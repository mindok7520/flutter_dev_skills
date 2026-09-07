# Refactor while preserving behavior

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [CLEAN_CODE](../docs/engineering/CLEAN_CODE.md)
- [DEPENDENCY_RULES](../docs/architecture/DEPENDENCY_RULES.md)

## Procedure

1. Identify the concrete maintenance, correctness, or measured performance problem and the public behavior to preserve.
2. Trace state ownership, resources, external interfaces, and test seams before moving code.
3. Compare a small structural change with the cost of broader abstraction or migration.
4. Keep visual direction and product semantics stable; route any deliberate UX change through the design workflow.
5. Verify observable behavior and cleanup, then update architecture and examples so they reflect the actual structure.

## Evidence and completion

Before/after responsibility map, preserved contracts, change rationale, validation, and migration cost.
