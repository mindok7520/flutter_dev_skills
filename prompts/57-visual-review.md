# Inspect and refine the running UI

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [VISUAL_REVIEW](../docs/design/VISUAL_REVIEW.md)
- [GOLDEN_TESTING](../docs/testing/GOLDEN_TESTING.md)
- [SCREEN_SPEC_TEMPLATE](../docs/design/SCREEN_SPEC_TEMPLATE.md)

## Procedure

1. Confirm the target screen, task, and approved reference or review priorities if missing.
2. Run the app in an available target environment and record commit, viewport, pixel ratio, font, locale, text scale, theme, and fixture.
3. Capture and actually view the relevant states, then exercise the primary action, keyboard flow, and important recovery path.
4. Report specific hierarchy, typography, spacing, contrast, content, interaction, or motion discrepancies with their user impact.
5. When correction is authorized, fix the highest-impact discrepancy and recapture under comparable conditions.
6. Stop when the agreed criteria are met; never approve a baseline or claim visual success without inspecting the relevant image.

## Evidence and completion

Reproducible captures, criterion-level findings, actual interaction results, before/after comparison, and unverified cells.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
