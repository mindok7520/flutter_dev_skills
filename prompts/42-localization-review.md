# Review localization in real UI

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

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
