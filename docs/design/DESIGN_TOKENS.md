# Design tokens and typography

Make visual decisions explicit, reusable, and adaptable to themes and content.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Use semantic color names for background, surface, foreground emphasis, primary action, focus, error, warning, and success. Do not encode meaning only in hue.
- Define title, body, label, caption, and data roles with size, weight, line height, and locale-appropriate fallback. A font family is not universally good or bad.
- Use a compact spacing scale; 4, 8, 12, 16, 24, and 32 logical pixels are a starting example, not a mandatory platform standard.
- Separate visual icon size from the interactive hit region. Define shape and elevation only where their hierarchy is meaningful.
- Map tokens to the existing theme and typed extensions where suitable; avoid scattered literals and duplicated parallel theme systems.
- Record light/dark/high-contrast intent, text scaling behavior, and motion roles. Avoid locking text to a fixed scale to preserve a screenshot.

## Procedure

1. Inspect the current theme, fonts, component defaults, and repeated literals.
2. Choose the smallest semantic vocabulary that serves the approved screen and its states.
3. Check the actual foreground/background pairs, localized glyphs, and long content.
4. Apply tokens through real components and recapture representative themes and large text.

## Required evidence

- [ ] Every new shared value has a reason and no conflicting duplicate source.
- [ ] Both themes preserve emphasis, contrast, and non-color state cues.
- [ ] Korean and other supported scripts render with readable metrics and predictable fallback.

## Tradeoffs and failure handling

A mathematically regular scale still needs optical adjustment. Record small exceptions when a real glyph, icon, or platform control requires them; do not create a new token for each isolated pixel adjustment.

## Sources and related work

[Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md). [Wonderous styling source](https://github.com/gskinnerTeam/flutter-wonderous-app).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
