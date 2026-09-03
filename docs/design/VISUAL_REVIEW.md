# Review actual UI evidence

Use [the design workflow](DESIGN_WORKFLOW.md) and compare against the agreed [brief](PRODUCT_DESIGN_BRIEF.md), not an imagined ideal or the reviewer's favorite style. Separate reference fidelity, visual coherence, usability, accessibility, and runtime correctness.

## Capture a reproducible state

Record commit, device/browser, viewport in logical units, pixel ratio, OS, font availability, locale, text scaling, theme, data fixture, and navigation steps. Capture the running app with the environment's supported screenshot facility. Inspect the image itself; a successful build, an image filename, or a tool's generic success response does not mean the screen was viewed.

Use sanitized fixtures. Wait for a documented stable state rather than an arbitrary sleep, and distinguish deliberate loading captures from incomplete rendering. Record transient-state timing when examining an animation. Never present a generated mockup as a capture of the implemented app.

## Compare by criterion

| Criterion | Inspect |
| --- | --- |
| Hierarchy | Can the primary information and action be found quickly? Are emphasis levels competing? |
| Typography | Readability, line length, baseline alignment, wrapping, localized glyphs, and text scaling. |
| Layout | Consistent spacing, alignment, grouping, constrained reading width, scrolling, and keyboard clearance. |
| Color and content | Semantic colors, actual contrast, state distinctions, real copy, image quality, and icon consistency. |
| Interaction | Visible affordances, immediate feedback, focus, hit targets, error recovery, and retained input. |
| Direction | Does this implementation support the brief's audience and character? Which specific decision does not? |
| Motion | Purpose, interruption, reduced motion, offscreen/background behavior, and frame stability. |

Report a finding with the screen/state, image region or component, observed mismatch, user impact, and smallest useful correction. Distinguish a blocking defect from an optional aesthetic alternative. Do not justify a redesign solely by "looks generic" or a self-assigned score.

## Exercise behavior and verify corrections

Run the main action, error/retry path, keyboard navigation, and relevant screen-reader flow. In Flutter web, a canvas screenshot and DOM-based automation have different visibility; verify available semantics and hit-testing rather than assuming React-style DOM selectors exist. Native platform behavior must be checked with the target platform's available tools.

Recapture changed states under the same conditions and compare before/after. Use [golden testing](../testing/GOLDEN_TESTING.md) selectively to prevent regressions after a baseline has been reviewed. Do not overwrite baselines merely to make CI pass. If execution or image viewing is unavailable, provide the static findings and exact missing evidence; retain visual verification as incomplete.

## Completion record

List accepted criteria, actual evidence, corrected findings, remaining tradeoffs, and unavailable environments. Stop optional polishing once the agreed outcome is met. A request for a different aesthetic is a new decision for the user, not a reason to silently extend the work.
