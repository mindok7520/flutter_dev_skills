# Repository responsibilities

Give application code a consistent data contract across remote, local, cached, and test implementations.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Put data coordination, mapping, caching rules, and consistency boundaries in repositories when those responsibilities exist.
- Keep transport parsing and low-level platform access in services or adapters. Do not return raw transport exceptions as user-facing text.
- Define source precedence, freshness, invalidation, account scoping, and offline reconciliation explicitly.
- Keep an injectable fake or test implementation at a useful boundary; a fake should reproduce the contract, not just happy-path data.

## Procedure

1. Identify the user-visible data promise and external failure modes.
2. Define inputs, outputs, errors, cancellation expectations, and cache behavior.
3. Test refresh, offline, stale data, duplicate mutation, and account isolation where relevant.
4. Verify that presentation consumes the contract without knowing transport details.

## Required evidence

- [ ] Cache and server disagreement has a documented reconciliation path.
- [ ] Errors and cancellations preserve data integrity.
- [ ] Tests isolate external I/O without asserting internal call sequences unnecessarily.

## Tradeoffs and failure handling

A trivial local value may not need a repository layer. Add the pattern to manage a real data boundary, not to satisfy a folder diagram.

## Sources and related work

[Flutter architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations), [Compass example](https://github.com/flutter/samples/tree/main/compass_app), and [state management](STATE_MANAGEMENT.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
