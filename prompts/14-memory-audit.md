# Investigate memory growth

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [MEMORY_GUIDE](../docs/performance/MEMORY_GUIDE.md)
- [DEPENDENCY_INJECTION](../docs/architecture/DEPENDENCY_INJECTION.md)

## Procedure

1. Specify the expected steady state and repeat route entry/exit, scrolling, account changes, or animation cycles that reproduce the growth.
2. Distinguish Dart heap, native/external memory, decoded images, caches, and GPU resources when tooling permits.
3. Compare snapshots and follow retaining paths to their actual owner; do not label a single high reading a leak.
4. Correct the lifetime or bounded cache policy without disposing shared resources still in use.
5. Repeat the same cycles and verify both memory behavior and the active consumers' correctness.

## Evidence and completion

Measured growth pattern, retaining path, lifetime correction, repeated measurements, and remaining uncertainty.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
