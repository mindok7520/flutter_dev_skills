# Design architecture for the actual product

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [APP_ARCHITECTURE](../docs/architecture/APP_ARCHITECTURE.md)
- [STATE_MANAGEMENT](../docs/architecture/STATE_MANAGEMENT.md)
- [DEPENDENCY_RULES](../docs/architecture/DEPENDENCY_RULES.md)

## Procedure

1. Map the existing modules, one important user flow, state owners, external trust boundaries, and resource lifetimes.
2. Compare the current approach with a feasible alternative using correctness, isolation, testing, complexity, and migration cost.
3. Separate presentation, state transitions, repository coordination, and external services; add domain/use-case layers only for actual complexity.
4. Evaluate state-management choices with prompt 58 when needed instead of silently installing a preferred package.
5. Record the decision and verify it with a representative slice and contract tests. UI direction changes still require the design consultation.

## Evidence and completion

Responsibility and data-flow map, ownership contracts, alternatives, architecture decision, migration and verification plan.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
