# Architecture sized to the product

Keep presentation, state transitions, and data access understandable without introducing layers that have no current responsibility.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Inspect the existing structure and user requirements before selecting an architecture. Preserve working conventions unless a measured or reproducible problem justifies migration.
- Separate UI composition from application state and data access. Views render state and forward intent; repositories coordinate data semantics; services adapt external APIs.
- Use an optional domain/use-case layer when business rules are repeated or too complex for the existing boundary. Do not create empty forwarding layers for every screen.
- Make state transitions and data flow explicit. Keep the server authoritative for authorization, payments, and shared persistent facts.
- Inject dependencies through the existing composition mechanism. Keep lifetime and cleanup ownership visible, with separate fakes for external boundaries.
- Choose state management based on scope, lifecycle, asynchronous complexity, testability, and team familiarity; an architecture diagram does not mandate a package.
- For new or changed UI, first follow the user consultation and design agreement workflow.

## Procedure

1. Map current files, external boundaries, state owners, and one representative user flow.
2. Compare the existing approach with at least one feasible alternative; explain correctness, complexity, migration, and operational implications.
3. Record the selected responsibilities and dependency direction in an architecture decision.
4. Implement or plan one vertical slice before replicating its structure across the product.
5. Verify repository contracts, state transitions, error paths, UI behavior, and relevant platform boundaries.

## Required evidence

- [ ] The actual code paths correspond to the architecture diagram and decision record.
- [ ] State, requests, caches, controllers, and subscriptions have identified owners.
- [ ] Tests can exercise business behavior without constructing the entire UI or contacting production services.

## Tradeoffs and failure handling

The Flutter guidance is a recommendation with conditional choices, not a requirement to install its example stack. Additional layers can improve isolation but also increase indirection, generated code, and onboarding cost.

## Sources and related work

[Flutter architecture recommendations](https://docs.flutter.dev/app-architecture/recommendations), [Compass example](https://github.com/flutter/samples/tree/main/compass_app), and [state management](STATE_MANAGEMENT.md). [Design workflow](../design/DESIGN_WORKFLOW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
