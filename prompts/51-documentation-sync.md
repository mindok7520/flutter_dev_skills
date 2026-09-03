# Synchronize instructions and documentation

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [DOCUMENTATION_UPDATE_POLICY](../docs/agent/DOCUMENTATION_UPDATE_POLICY.md)
- [OVERVIEW](../docs/architecture/OVERVIEW.md)

## Procedure

1. Identify the authoritative code, user decisions, sources, and actual validation results affected by the change.
2. Update the canonical document and keep adapters as references instead of copying divergent policies.
3. Keep language boundaries explicit: reusable execution prose may be English while user explanation and the README map remain Korean.
4. Verify links, catalogs, skill metadata, examples, required files, and installed-project portability.
5. Record what changed, why, actual evidence, and remaining work without inventing approval or completion.

## Evidence and completion

Updated authoritative documents, synchronized discovery paths, source evidence, validation, and remaining discrepancies.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
