# Evaluate WebAssembly for the target app

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
