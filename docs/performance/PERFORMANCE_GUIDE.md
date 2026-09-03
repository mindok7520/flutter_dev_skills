# Measure before optimizing

Connect optimization work to a user-visible problem, a reproducible workload, and a measurable outcome.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Identify whether the problem is startup, input latency, frame delivery, memory, network, or artifact size; these require different evidence.
- Use representative hardware and data. Native debug-mode timing and emulator results are not release performance claims.
- Record the target refresh rate and distribution, not only average FPS. Frame intervals are about 16.7 ms at 60 Hz and 8.3 ms at 120 Hz; the app's budget must be agreed for its device and workload.
- Separate build/layout work from raster/compositing and external I/O. An expensive shader cannot be fixed by adding const to an unrelated widget.
- Optimize the measured bottleneck one change at a time and retain correctness, accessibility, and recovery behavior.
- Do not install a package, move code to isolates, or add caching solely because it is described as faster.

## Procedure

1. Specify a hypothesis, representative scenario, baseline, and acceptance budget.
2. Capture a trace/profile and identify the dominant cost with source-level evidence.
3. Make the smallest relevant change and rerun the same workload with comparable conditions.
4. Compare distributions and memory costs; revert or explain changes that do not support the hypothesis.

## Required evidence

- [ ] Environment, workload, sample count, warm/cold conditions, and raw results are recorded.
- [ ] The measured improvement corresponds to the original user-visible problem.
- [ ] Behavior and other important resource costs remain within the agreed constraints.

## Tradeoffs and failure handling

More benchmarks do not necessarily improve confidence. Repeat enough to distinguish an effect from noise and stop once the concrete risk is resolved. Never present proposed budgets or synthetic samples as product measurements.

## Sources and related work

[Flutter performance guidance](https://docs.flutter.dev/perf/best-practices) and [DevTools](https://docs.flutter.dev/tools/devtools/performance). [Profiling procedure](PROFILING_GUIDE.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
