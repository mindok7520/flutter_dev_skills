# Intent, state transitions, and data flow

Make user intent and asynchronous responses converge on one coherent visible state.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Name the authoritative source for each datum and keep derived presentation values consistent with it.
- Separate user intent from confirmed state. Optimistic updates require rollback or reconciliation behavior.
- Specify loading, refresh, partial data, empty, failure, cancellation, and retry transitions only where they apply.
- Account for stale responses, pagination overlap, account changes, and out-of-order events.
- Keep server authorization and persistent transaction decisions outside local UI state.

## Procedure

1. Draw the smallest intent-to-service-to-state flow and identify each writer.
2. Define event ordering and the data retained during pending or failed operations.
3. Test duplicate, late, cancelled, and conflicting outcomes with controlled fakes.
4. Verify the actual UI feedback and recovery path against the screen specification.

## Required evidence

- [ ] The newest intent cannot be overwritten by an irrelevant older response.
- [ ] One-time effects are not replayed by a routine rebuild.
- [ ] Optimistic and persisted state reconcile after failure or reconnect.

## Tradeoffs and failure handling

Optimistic UI can improve responsiveness but increases reconciliation complexity. Use it only when reversibility and conflict handling fit the operation.

## Sources and related work

[Flutter architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations), [Compass example](https://github.com/flutter/samples/tree/main/compass_app), and [state management](STATE_MANAGEMENT.md). [Screen specification](../design/SCREEN_SPEC_TEMPLATE.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
