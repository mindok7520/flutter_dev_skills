# Investigate a performance problem

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [PERFORMANCE_GUIDE](../docs/performance/PERFORMANCE_GUIDE.md)
- [PROFILING_GUIDE](../docs/performance/PROFILING_GUIDE.md)

## Procedure

1. Define the user-visible delay, representative workload, target device, refresh rate, build mode, renderer, and acceptance budget.
2. Capture comparable baseline traces and distributions; separate cold/warm conditions and avoid reporting debug timing as release performance.
3. Locate the dominant cost in CPU work, build/layout, raster/compositing, network, memory, or assets.
4. Change one causal factor and rerun the same scenario, preserving correctness, accessibility, and approved visual behavior.
5. Compare raw evidence and variability, including costs moved to another stage, and retain only justified optimizations.

## Evidence and completion

Environment, workload, raw profiles, causal hypothesis, before/after distribution, and regression risks.
