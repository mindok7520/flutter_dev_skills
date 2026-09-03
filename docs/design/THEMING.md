# Theme implementation

Apply the approved design consistently across components, system settings, and overlays.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Inspect the existing theme before adding a new one. Keep semantic roles authoritative and reuse the app's selected design components.
- Specify system/light/dark behavior and whether a user preference persists. Treat persistence as a product/state decision.
- Cover dialogs, sheets, menus, disabled controls, selected states, and system UI contrast, not only the main background.
- Keep fixed brand colors distinct from semantic feedback colors and supply tested variants where needed.

## Procedure

1. Confirm the theme behavior and approved palette with the user.
2. Map shared roles to components and inspect any theme extensions or legacy overrides.
3. Switch themes while a form, overlay, and asynchronous operation are active.
4. Capture the important states and check contrast, focus, icons, and images.

## Required evidence

- [ ] Theme changes preserve user state and update every relevant surface.
- [ ] Color roles remain meaningful and readable across variants.
- [ ] Persisted settings follow the agreed product requirement.

## Tradeoffs and failure handling

Avoid maintaining independent color systems in every feature. Theme animation is optional and must not flash unreadable content or ignore reduced motion.

## Sources and related work

[Design tokens](DESIGN_TOKENS.md), [dark mode](DARK_MODE.md), and [Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
