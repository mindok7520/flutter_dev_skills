# Memory retention and resource ownership

Distinguish live data, caches, transient allocations, and leaks using ownership and repeated measurements.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Record the workload and expected steady state. A single high memory reading is not enough to identify a leak.
- Inspect Dart heap, native/external allocations, images, and GPU-related resources separately when tools allow.
- Repeat route entry/exit, scrolling, account switching, and animation start/stop; compare snapshots and retaining paths after comparable idle periods.
- Bound caches by a meaningful policy and invalidate account-scoped data. Cached decoded images may use far more memory than compressed downloads.
- Dispose owned controllers, listeners, streams, images, shader instances, and runtime assets using their installed APIs. Garbage collection is not a substitute for deterministic native cleanup.

## Procedure

1. Define what should remain alive at each lifecycle boundary.
2. Capture baseline and repeated-cycle memory evidence with environment metadata.
3. Follow retaining paths to the owner and fix the lifetime or cache policy.
4. Repeat the workload and verify that cleanup does not break active consumers.

## Required evidence

- [ ] Observed growth is linked to a retained object/resource and its owner.
- [ ] Repeated operations converge toward an explained steady state or a documented bound.
- [ ] Account isolation and active shared consumers remain correct.

## Tradeoffs and failure handling

Aggressive cache eviction can increase network, decoding, and battery costs. Choose a bounded policy from the workload rather than deleting useful caches indiscriminately.

## Sources and related work

[DevTools memory](https://docs.flutter.dev/tools/devtools/memory), [resource lifetime](../architecture/DEPENDENCY_INJECTION.md), and [image assets](IMAGE_ASSET_OPTIMIZATION.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
