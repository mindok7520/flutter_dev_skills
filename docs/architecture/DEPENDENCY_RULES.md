# Dependency direction and boundaries

Keep implementation choices replaceable and prevent presentation code from becoming the authority for data behavior.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Inspect current module relationships before adding abstractions or moving files.
- Keep data/services independent of Flutter widgets. A repository must not retain BuildContext to display errors.
- Pass intent and immutable data across boundaries; avoid exposing mutable transport objects directly to unrelated layers.
- Define interfaces at boundaries with multiple implementations, test seams, or meaningful external coupling. Do not mirror every class with an interface by default.
- Avoid cyclic imports, cross-feature access to private implementation, and globally mutable service registries.
- Keep dependency construction and disposal in an identifiable composition scope.

## Procedure

1. Trace one user action from view to state owner, repository, and service, then back to rendering.
2. Identify cycles, implicit globals, concrete external dependencies, and objects retained beyond their owner.
3. Choose the smallest boundary change that improves the demonstrated problem.
4. Test the contract with a fake and verify existing production behavior remains intact.

## Required evidence

- [ ] Dependency direction is visible in imports and construction, not only a diagram.
- [ ] External effects can be isolated in tests without mocking the entire application.
- [ ] Resource ownership survives the refactoring.

## Tradeoffs and failure handling

Interfaces and factories impose maintenance cost. Use them where the boundary has value, and document why a migration is worth changing familiar code.

## Sources and related work

[Flutter architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations), [Compass example](https://github.com/flutter/samples/tree/main/compass_app), and [state management](STATE_MANAGEMENT.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
