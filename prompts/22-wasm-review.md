# Evaluate WebAssembly for the target app

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [WASM_STRATEGY](../docs/performance/WASM_STRATEGY.md)
- [WEB_PERFORMANCE](../docs/performance/WEB_PERFORMANCE.md)

## Procedure

1. Inspect the actual SDK, build configuration, package compatibility, browser requirements, and deployment headers.
2. Compare the current build with the proposed WebAssembly path on representative browsers and devices.
3. Measure transfer, startup, memory, and interaction rather than assuming WebAssembly is always faster.
4. Check plugin and platform integration, fallback behavior, and unsupported environments.
5. Record a keep/adopt/defer decision with compatibility, migration, operational cost, and actual measurements.

## Evidence and completion

Verified version and browser matrix, comparative measurements, compatibility gaps, and adoption decision.
