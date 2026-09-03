# Refactor while preserving behavior

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
