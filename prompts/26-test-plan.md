# Plan tests from observable risks

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [TEST_STRATEGY](../docs/testing/TEST_STRATEGY.md)
- [GOLDEN_TESTING](../docs/testing/GOLDEN_TESTING.md)
- [VISUAL_REVIEW](../docs/design/VISUAL_REVIEW.md)

## Procedure

1. Map agreed requirements and important failure modes to the smallest useful test layers.
2. Separate pure logic, repository contracts, state transitions, widget interaction, integration, accessibility, and visual checks.
3. Include stale responses, repeated input, cancellation, lifecycle cleanup, and platform differences where the feature can fail.
4. Choose representative screenshots only after a baseline has been reviewed; an image comparison is not a usability test.
5. Define deterministic fixtures, needed environments, raw evidence, and explicitly unverified cells.

## Evidence and completion

Requirement-to-test map, priority, fixture and environment plan, visual criteria, and justified exclusions.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
