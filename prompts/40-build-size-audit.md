# Audit application and asset size

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [BUILD_SIZE_BUDGET](../docs/performance/BUILD_SIZE_BUDGET.md)
- [IMAGE_ASSET_OPTIMIZATION](../docs/performance/IMAGE_ASSET_OPTIMIZATION.md)

## Procedure

1. Measure the actual target artifact and distinguish download/compressed size, installed size, and runtime decoded memory.
2. Identify dominant code, fonts, images, runtime assets, and optional SDK contributions.
3. Compare removal, deferred loading, resolution/format changes, and simpler assets against functionality and quality.
4. Inspect visual quality at realistic density and themes after asset changes, and exercise load/failure behavior.
5. Record comparable before/after sizes and any compatibility or latency costs.

## Evidence and completion

Artifact and asset contributions, measured reduction, visual evidence, compatibility and runtime tradeoffs.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
