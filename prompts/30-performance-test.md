# Measure a performance hypothesis

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [PROFILING_GUIDE](../docs/performance/PROFILING_GUIDE.md)
- [PERFORMANCE_BUDGET](../docs/performance/PERFORMANCE_BUDGET.md)

## Procedure

1. Define a workload, device/browser, renderer, build mode, cache state, sample count, and metric that corresponds to user experience.
2. Capture a baseline and candidate under comparable conditions, separating cold start, warm interaction, and sustained operation.
3. Inspect distributions and slow-tail behavior; record raw traces and variability instead of selecting the best run.
4. Check memory, power-related workload, and correctness when an optimization moves costs elsewhere.
5. Compare against an agreed budget and state whether the evidence supports the hypothesis; proposed or synthetic data must be labeled.

## Evidence and completion

Reproducible environment and workload, raw evidence, distribution comparison, budget result, and uncertainty.
