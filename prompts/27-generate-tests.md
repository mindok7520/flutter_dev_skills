# Write meaningful tests

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

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
