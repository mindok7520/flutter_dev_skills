# Dark mode and contrast

Preserve hierarchy and readability when the luminance and surface relationships change.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Design semantic dark roles instead of mechanically inverting every color.
- Check actual contrast for body text, muted labels, borders, focus, disabled controls, charts, and images.
- Use surface hierarchy deliberately; shadow alone may not distinguish elevated dark surfaces.
- Avoid automatic pure-black requirements. Choose surfaces for the product and test on representative devices.
- Provide non-color cues for states and adjust artwork only when its meaning and rights allow it.

## Procedure

1. Confirm supported theme variants and inspect the current semantic palette.
2. Compare the same realistic content and state in both light and dark themes.
3. Check transitions, overlays, system bars, and loading placeholders for flashes and poor contrast.
4. Record approved roles and any asset-specific exceptions.

## Required evidence

- [ ] Information and interaction priorities are equivalent across themes.
- [ ] Charts and status labels remain understandable without hue alone.
- [ ] Theme switching does not expose unreadable transitional states.

## Tradeoffs and failure handling

A darker palette can change the visual weight of text and images. Review the actual result rather than accepting numeric color inversion. Battery benefits depend on the display and workload; do not promise them without measurement.

## Sources and related work

[Theming](THEMING.md), [accessibility](ACCESSIBILITY.md), and [visual review](VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
