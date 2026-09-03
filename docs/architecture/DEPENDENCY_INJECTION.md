# Dependency construction and lifetime

Make dependencies and their ownership explicit while keeping object creation practical.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Prefer explicit construction or the project's existing container/provider mechanism. Do not introduce a second DI system without a concrete integration need.
- Assign application, account, feature, and widget lifetimes. A shared client and a screen controller need different owners.
- Pass fakes at external boundaries for tests rather than changing global state across tests.
- Define disposal order and late-callback behavior; injecting an object does not imply the receiver owns it.

## Procedure

1. Inventory constructors, providers, singleton registrations, and resource owners.
2. Map lifetime boundaries to route exit, logout, app shutdown, and test cleanup.
3. Inject the smallest contract required by each consumer.
4. Test multiple scopes and teardown without leaked listeners or reused account data.

## Required evidence

- [ ] Each disposable dependency has exactly one documented owner.
- [ ] Tests can replace external effects without order-dependent global mutations.
- [ ] Logout and route teardown release or invalidate correctly scoped resources.

## Tradeoffs and failure handling

Containers reduce wiring but can hide dependency graphs. Keep construction inspectable and avoid service lookup deep inside widgets or domain methods.

## Sources and related work

[Flutter architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations), [Compass example](https://github.com/flutter/samples/tree/main/compass_app), and [state management](STATE_MANAGEMENT.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
