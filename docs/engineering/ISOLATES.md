# Isolate decisions and worker lifecycle

Move demonstrated CPU work away from interactive execution only when the target platform and transfer costs justify it.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Measure parsing, transformation, or computation before introducing a worker. Asynchronous I/O alone is not a reason to spawn an isolate.
- Account for startup, message transfer, copies, result materialization, peak memory, and repeated-job amortization.
- Define job identity, bounded queues, cancellation, progress, error transport, and shutdown for persistent workers.
- Do not assume web compute provides parallel execution. Verify the chosen API and target; Flutter documentation describes compute running on the main thread on web.
- Check plugin/platform limitations and transferable object rules. Isolate separation does not automatically provide a secure sandbox for untrusted work.

## Procedure

1. Capture the blocking work and its input-size distribution.
2. Compare in-isolate execution with the smallest supported worker design on the actual platform.
3. Measure total user-visible latency and memory, including transfer overhead.
4. Test cancellation, worker failure, queue saturation, and resource cleanup.

## Required evidence

- [ ] The worker improves the relevant measured workload rather than only an isolated microbenchmark.
- [ ] Large messages and cancelled results do not cause unbounded memory retention.
- [ ] Web and native results are reported separately.

## Tradeoffs and failure handling

A worker can make short tasks slower and large tasks more memory-hungry. Keep the simple implementation if overhead dominates, and optimize the underlying algorithm before adding orchestration.

## Sources and related work

[Flutter isolates](https://docs.flutter.dev/perf/isolates) and [profiling](../performance/PROFILING_GUIDE.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
