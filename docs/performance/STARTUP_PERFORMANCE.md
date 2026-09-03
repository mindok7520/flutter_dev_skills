# First useful screen and startup work

Reduce time to the first usable product state without concealing initialization failures.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Define the first useful screen and action, not only the first painted frame or splash dismissal.
- Separate cold and warm starts, authentication restoration, asset loading, data fetching, and first-interaction work.
- Initialize only what is required on the critical path. Deferred work still needs an owner, error handling, and a nonblocking recovery path.
- Avoid loading every animation, shader, image, or optional SDK at startup without a measured reason.
- Keep required consent and security checks correct while deferring unrelated work.

## Procedure

1. Record the startup timeline on representative devices and network/cache conditions.
2. Find synchronous work and dependency chains blocking the first useful action.
3. Move or simplify a measured cost and verify both initial and deferred failure paths.
4. Repeat cold/warm measurements and inspect the real screen for flash or unstable layout.

## Required evidence

- [ ] The first useful action has a repeatable definition and measurement.
- [ ] Deferred initialization failures remain observable and recoverable.
- [ ] No required security or user-consent behavior was bypassed.

## Tradeoffs and failure handling

Deferring all work can merely move a freeze to the first tap. Measure startup and the first interaction together when work is shifted between them.

## Sources and related work

[Flutter performance guidance](https://docs.flutter.dev/perf/best-practices) and [DevTools](https://docs.flutter.dev/tools/devtools/performance). [Profiling](PROFILING_GUIDE.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
