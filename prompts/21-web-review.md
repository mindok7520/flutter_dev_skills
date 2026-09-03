# Review Flutter web behavior

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [WEB_ARCHITECTURE](../docs/architecture/WEB_ARCHITECTURE.md)
- [WEB_PERFORMANCE](../docs/performance/WEB_PERFORMANCE.md)
- [RESPONSIVE_ADAPTIVE](../docs/design/RESPONSIVE_ADAPTIVE.md)

## Procedure

1. Inspect the target Flutter version, web renderer, plugins, deployment path, and supported browsers.
2. Exercise navigation, refresh, deep links, keyboard/pointer use, text input, and loading/error behavior.
3. Verify the browser-visible semantics and actual canvas rendering rather than assuming a React-style DOM.
4. Measure startup, asset transfer, input latency, and representative frame behavior in the actual browser.
5. Record browser/backend differences and verify that fallbacks preserve the product's main task.

## Evidence and completion

Browser and deployment matrix, actual behavior and performance evidence, limitations, and focused corrections.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
