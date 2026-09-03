# Component contracts and catalogs

Keep reusable widgets predictable in appearance, behavior, accessibility, and resource lifetime.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Specify inputs, callbacks, controlled/local state, variants, and ownership. Avoid network calls and global service lookup inside presentation components.
- Support the applicable default, hover, focus, pressed, selected, disabled, pending, error, and empty states.
- Use appropriate built-in controls and semantics before reimplementing gestures. Custom drawing does not automatically provide accessible interaction.
- Define focus entry/exit, visible focus, keyboard actions, semantic name/role/value, and the hit region.
- Dispose only resources the component owns; document externally supplied controller ownership and callbacks after unmount.
- Catalog real components with deterministic content extremes, themes, and text sizes. Avoid a separate demonstration-only implementation.

## Procedure

1. Inspect existing equivalents and decide whether reuse, a variant, or a local widget fits.
2. Write the state and event contract in the screen specification.
3. Add the component to a local catalog or existing showcase when it is shared or state-rich.
4. Verify interaction and semantics, then review selected visual baselines.

## Required evidence

- [ ] Multiple consumers do not leak selection, pending state, or listeners into each other.
- [ ] Keyboard and screen-reader behavior match the visible interaction.
- [ ] Catalog examples and tests use the shipped widget implementation.

## Tradeoffs and failure handling

Too many boolean options create invalid combinations. Prefer meaningful variants or separate components when behavior differs substantially. A catalog is optional for a tiny local widget and does not require a hosted service.

## Sources and related work

[Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md). [Widgetbook](https://github.com/widgetbook/widgetbook).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
