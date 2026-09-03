# Asynchronous work and concurrency policy

Protect state and resources across asynchronous gaps; single-isolate execution does not remove logical races.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- For each operation specify owner, timeout, cancellation, ordering, duplicate handling, queue bound, error propagation, and shutdown behavior.
- Treat a mounted check as a UI-lifetime guard, not protection from stale data, duplicate remote writes, or cross-account results.
- Apply backpressure when producers can outpace consumers: bounded queues, coalescing, latest-intent processing, or explicit rejection according to the task.
- Separate cancellation of observation from cancellation of work. Remote mutations may complete after a local future or handler is abandoned.
- Close owned subscriptions, controllers, timers, and workers on teardown. Avoid unobserved failures and detached work with no owner.

## Procedure

1. Trace overlapping inputs, route changes, account changes, and delayed responses.
2. Choose ordering semantics for the actual operation and document why alternatives would be wrong.
3. Reproduce cancellation, timeout, failure, and shutdown deterministically with fakes.
4. Verify visible state, persistent effects, and cleanup after each interleaving.

## Required evidence

- [ ] Stale results cannot overwrite the current user intent or account.
- [ ] Queues and resource use remain bounded under repeated input.
- [ ] Failures propagate to an observable recovery path and teardown completes.

## Tradeoffs and failure handling

Serializing everything can stall unrelated work; running everything concurrently can violate consistency. Choose at the ownership boundary and test interactions across event types, not just inside one handler.

## Sources and related work

[State management](../architecture/STATE_MANAGEMENT.md), [Dart concurrency](https://dart.dev/language/concurrency), and [Bloc concurrency](https://github.com/felangel/bloc/tree/master/packages/bloc_concurrency).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
