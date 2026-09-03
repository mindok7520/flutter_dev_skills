# State ownership and state-management selection

Read the target manifest and lockfile before naming APIs or recommending migration. No state-management package is a default dependency of this material repository. Apply the [shared contract](../agent/PROMPT_CONTRACT.md).

## Inventory state before choosing a tool

For each state value, record its owner, readers, writers, lifetime, persistence needs, source of truth, and asynchronous dependencies. Distinguish transient presentation state (focus, expansion, animation progress), screen/application state (loading, filters, selection), and authoritative domain data (account entitlements, stored records). Derived values should normally be computed from authoritative state rather than maintained as competing writable copies.

| Candidate | Appropriate starting point | Costs and checks |
| --- | --- | --- |
| Existing solution | It already supports the required behavior and testing | Prefer consistency; change only for a concrete limitation. |
| Local widget state / ValueNotifier | Small, local, short-lived presentation state | Keep rebuild scope local; dispose owned objects and avoid promoting every flag globally. |
| ChangeNotifier with explicit dependency injection | Small-to-medium observable view models | Manage listeners and mutation visibility; test transitions and avoid broad notifications. |
| Riverpod | Scoped dependencies and asynchronous state with explicit lifecycle needs | Verify installed APIs, code-generation choices, provider identity, invalidation, caching, and disposal. |
| Cubit / Bloc | Explicit state transitions; Bloc is useful when event ordering and transformations matter | Assess event/state boilerplate, equality, selector boundaries, side effects, and concurrency semantics. |

These are decision criteria, not performance rankings. Compare at most the plausible candidates for the actual application, including keeping the existing solution. Record the reason in an architecture decision before introducing a new project-wide convention.

## Asynchronous behavior

Define initial/loading/data/empty/error/refreshing behavior according to the feature. Retain valid previous data during refresh if the product requires it. A new query or account switch must prevent an older response from overwriting current state. Use cancellation when supported and a request identity or equivalent stale-result check when cancellation alone does not prove ordering.

For Riverpod, review automatic disposal, invalidation, family parameters, and bounded cache lifetimes against the installed version. Register cleanup with the appropriate lifecycle hook; do not mutate other providers as a cleanup side effect. Disposing a provider is not proof that an external request was cancelled.

For Bloc, select event semantics deliberately: concurrent work, sequential processing, ignoring duplicates while busy, or latest-intent replacement serve different products. A transformer on one handler does not automatically serialize every event type. Cancelling an event handler does not undo a remote write; persistent mutations need server-side consistency and idempotency where relevant.

## Rendering and side effects

Subscribe only to the state a component needs, with stable equality and immutable snapshots where practical. Measure before adding selectors everywhere. Keep one-time navigation, dialogs, and messages from replaying after rebuild or state restoration. Animation controllers belong to their presentation lifecycle; animation state is not payment or authorization state.

## Verification

Test the feature's actual state transitions, stale responses, repeated actions, retry, route exit, account switching, and cleanup. Verify behavior rather than the exact number of notifications. When a change claims faster rendering, capture a representative before/after profile; a different package name is not evidence of improvement.

Use [58-state-management-decision](../../prompts/58-state-management-decision.md), [data flow](DATA_FLOW.md), and [concurrency](../engineering/ASYNC_CONCURRENCY.md). Sources: [Flutter recommendations](https://docs.flutter.dev/app-architecture/recommendations), [Riverpod](https://github.com/rrousselGit/riverpod), [Bloc concurrency](https://github.com/felangel/bloc/tree/master/packages/bloc_concurrency). Checked repository revisions and adaptations: [reference research](../REFERENCE_RESEARCH.md).
