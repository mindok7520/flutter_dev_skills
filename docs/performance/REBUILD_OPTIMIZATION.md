# Targeted rebuild optimization

Reduce unnecessary UI work without making state updates stale or introducing fragile equality rules.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Measure the slow interaction before assuming a rebuild is expensive. A rebuild is not equivalent to a full repaint.
- Keep subscriptions close to the values consumed and avoid notifying unrelated large subtrees.
- Use stable immutable inputs and meaningful equality where practical. A selector that suppresses a required update is a correctness bug.
- Keep synchronous computation and side effects out of build. Move derived work to an appropriate owner and invalidate it correctly.
- Use const or extracted reusable widgets when appropriate, but do not claim a speedup without relevant evidence.

## Procedure

1. Find the state change and measured build/layout cost it produces.
2. Narrow the dependency or extract the expensive region without changing the state contract.
3. Test every state field that should update the region and relevant selection/reordering behavior.
4. Reprofile the same interaction and verify the actual screen.

## Required evidence

- [ ] Required updates remain visible and one-time effects are not duplicated.
- [ ] The measured workload improves or the change is justified as maintainability only.
- [ ] No unnecessary project-wide state-management migration was introduced.

## Tradeoffs and failure handling

Fine-grained subscriptions increase indirection and can retain more objects. Keep them where they solve a real cost or clarify a stable contract.

## Sources and related work

[State management](../architecture/STATE_MANAGEMENT.md) and [Flutter performance guidance](https://docs.flutter.dev/perf/best-practices) and [DevTools](https://docs.flutter.dev/tools/devtools/performance).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
