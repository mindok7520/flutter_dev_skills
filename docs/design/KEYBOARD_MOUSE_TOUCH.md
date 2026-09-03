# Keyboard, pointer, and touch input

Make the same task available through the input methods supported by the product.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Expose visible focus and logical traversal; overlays must not conceal the focused control.
- Use platform-appropriate activation and shortcuts. Do not intercept text editing shortcuts or browser navigation without a task-specific reason.
- Provide focus restoration when dialogs, menus, or routes close. Avoid keyboard traps.
- Hover may reveal supplemental information, but essential actions must also be available to touch and keyboard users.
- Provide alternatives for drag, swipe, and precision gestures where relevant. Prevent accidental duplicate commands without swallowing valid input.
- Use appropriately sized hit regions and preserve input while the software keyboard appears or disappears.

## Procedure

1. List supported inputs and the complete primary interaction sequence.
2. Test keyboard-only navigation, activation, dismissal, and focus restoration.
3. Test touch and pointer behavior including overlapping targets, scroll gestures, and disabled states.
4. Repeat the error path and verify that feedback and recovery remain reachable.

## Required evidence

- [ ] Each essential action is reachable through the supported input methods.
- [ ] Focus is visible and restored predictably after transient UI.
- [ ] Hover-only content does not hide required information.

## Tradeoffs and failure handling

Duplicating every desktop convention on mobile adds clutter. Preserve task equivalence while adapting the interaction to the platform. Avoid global gesture handlers that silently interfere with nested controls.

## Sources and related work

[Accessibility](ACCESSIBILITY.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [Flutter adaptive guidance](https://docs.flutter.dev/ui/adaptive-responsive/best-practices).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
