# Reproducible profiling

Produce evidence another developer can use to reproduce and assess a performance claim.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Record commit, Flutter/Dart versions, OS, device/GPU, renderer, build mode, refresh rate, data size, network conditions, and power/thermal state where relevant.
- Use profile mode and DevTools on supported native targets. Use the actual browser's performance tools for web behavior and record the renderer/browser separately.
- Separate cold start, warm start, first interaction, sustained operation, and background/resume scenarios.
- Select relevant measures: frame-time distribution, input-to-result latency, CPU work, allocation/retention, network timing, or decoded image memory.
- Keep sanitized raw traces and commands. Note instrumentation overhead and unavailable data.

## Procedure

1. Define a repeatable navigation/input sequence and stable fixture.
2. Warm up only the scenario intended to be warm; do not hide first-use costs.
3. Capture several comparable runs and inspect the slow tail rather than selecting the best run.
4. Change one causal factor, capture again, and explain uncertainty and regression risk.

## Required evidence

- [ ] Baseline and candidate use comparable conditions and the same workload.
- [ ] Raw evidence and its environment metadata can be located from the execution plan.
- [ ] Conclusions identify the measured bottleneck and the remaining uncertainty.

## Tradeoffs and failure handling

A profiler changes the system slightly. Use the lowest-cost instrumentation that answers the question, and use end-to-end timing to validate a local improvement when the user-visible effect matters.

## Sources and related work

[Flutter performance guidance](https://docs.flutter.dev/perf/best-practices) and [DevTools](https://docs.flutter.dev/tools/devtools/performance). [Performance test prompt](../../prompts/30-performance-test.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
