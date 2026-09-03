# Review localization in real UI

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [LOCALIZATION](../docs/design/LOCALIZATION.md)
- [ACCESSIBILITY](../docs/design/ACCESSIBILITY.md)

## Procedure

1. Confirm supported locales and inspect source strings, generated localization, and fallback fonts.
2. Check complete messages, pluralization, dates, numbers, currency, and domain terminology in context.
3. Inspect long localized text, narrow layouts, large text, and directional behavior when in scope.
4. Verify semantic labels, focus order, errors, and primary actions in the supported languages.
5. Distinguish translation review from layout verification and record unreviewed languages.

## Evidence and completion

Locale-specific findings, string and layout corrections, generation/check results, and remaining language coverage.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
