# Write meaningful tests

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [UNIT_TESTING](../docs/testing/UNIT_TESTING.md)
- [WIDGET_TESTING](../docs/testing/WIDGET_TESTING.md)
- [GOLDEN_TESTING](../docs/testing/GOLDEN_TESTING.md)

## Procedure

1. Identify a public behavior or regression risk and inspect existing test conventions before adding a test.
2. Use fakes at useful boundaries and assert observable outcomes rather than duplicating implementation logic.
3. Exercise the relevant success, error, ordering, cancellation, and lifecycle paths with deterministic control.
4. For UI, test interaction and semantics; use golden images selectively for stable reviewed appearances.
5. Run the test, verify that it would detect the targeted failure, and report unavailable platform or visual coverage separately.

## Evidence and completion

Tested contracts, changed tests, actual execution results, regression sensitivity, and limits.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
