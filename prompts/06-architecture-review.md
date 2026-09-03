# Review architecture against code

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [APP_ARCHITECTURE](../docs/architecture/APP_ARCHITECTURE.md)
- [DEPENDENCY_RULES](../docs/architecture/DEPENDENCY_RULES.md)
- [DEPENDENCY_INJECTION](../docs/architecture/DEPENDENCY_INJECTION.md)

## Procedure

1. Trace actual imports, construction, state writes, and external calls for the requested feature.
2. Look for cycles, implicit globals, transport details in UI, competing state owners, and objects retained across invalid lifetimes.
3. Distinguish a demonstrated defect from a style preference or an optional architectural convention.
4. Recommend the smallest corrective boundary and evaluate migration, compatibility, testing, and cleanup implications.
5. For a review-only request, report evidence and recommendations without starting an unrelated rewrite.

## Evidence and completion

Prioritized findings with code paths, failure conditions, impact, corrections, and explicitly limited review coverage.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
