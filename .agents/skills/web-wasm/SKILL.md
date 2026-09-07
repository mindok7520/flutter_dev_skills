---
name: web-wasm
description: "Use to evaluate webassembly for the target app in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Evaluate WebAssembly for the target app

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Inspect the actual SDK, build configuration, package compatibility, browser requirements, and deployment headers.
2. Compare the current build with the proposed WebAssembly path on representative browsers and devices.
3. Measure transfer, startup, memory, and interaction rather than assuming WebAssembly is always faster.
4. Check plugin and platform integration, fallback behavior, and unsupported environments.
5. Record a keep/adopt/defer decision with compatibility, migration, operational cost, and actual measurements.

## References to load for this task

- [WASM_STRATEGY](../../../docs/performance/WASM_STRATEGY.md)
- [WEB_PERFORMANCE](../../../docs/performance/WEB_PERFORMANCE.md)
- [Task prompt](../../../prompts/22-wasm-review.md)

## Completion contract

Verified version and browser matrix, comparative measurements, compatibility gaps, and adoption decision.
