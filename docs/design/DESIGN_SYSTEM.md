# Product design system

Turn an approved visual direction into a small, coherent set of reusable decisions and components.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Begin with a product brief and existing UI inventory, not a new dependency or a universal aesthetic preset.
- Separate semantic design roles from literal values. Define surfaces, content emphasis, actions, feedback, text roles, spacing, shape, elevation, and motion.
- Reuse existing components before adding variants. A variant represents a user meaning or state, not a one-off workaround.
- Keep product-wide rules authoritative and document narrow screen overrides with a reason and owner.
- Keep component behavior, accessibility, focus, state ownership, and error feedback consistent as well as appearance.
- Choose Material, Cupertino, or a tailored system according to the target product. Do not transplant React/CSS components into Flutter.
- Maintain representative component states in a local catalog; Widgetbook is an option when its benefits justify a dependency.

## Procedure

1. Confirm the visual direction and representative screen with the user.
2. Inventory repeated elements and map them to token roles and component contracts.
3. Implement the smallest shared set that supports a real screen and its state variants.
4. Check multiple consumers, themes, locales, text sizes, and input methods before expanding the abstraction.
5. Record decisions and migration impact; keep examples synchronized with the actual components.

## Required evidence

- [ ] Each shared role has a purpose, owner, and applicable variants.
- [ ] The component catalog uses real production components and deterministic fixtures.
- [ ] A screen can be assembled without inventing unrelated spacing and color values.

## Tradeoffs and failure handling

Centralizing every value creates a difficult API; centralize stable semantics and repeated choices. Keep first-time local components local until a shared contract is clear. Do not claim that a catalog proves accessibility or product usability.

## Sources and related work

[Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md). [shadcn design principles](https://ui.shadcn.com/docs) and [Widgetbook](https://github.com/widgetbook/widgetbook).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
