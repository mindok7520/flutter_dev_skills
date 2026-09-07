# Review Flutter web behavior

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

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
