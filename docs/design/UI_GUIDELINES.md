# UI fundamentals

Make the intended task, information hierarchy, and available actions legible before adding visual effects.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Ask about the missing design goal and constraints before new UI work using the design workflow; reuse an approved scope.
- Give the main task a clear visual priority. Secondary actions remain discoverable without competing with it; multiple equal-priority actions need a reason.
- Use alignment, proximity, whitespace, and text hierarchy to express actual relationships. Borders, cards, and shadows should clarify grouping rather than surround every element.
- Use meaningful text roles and a consistent spacing scale. Do not choose a font, gradient, oversized heading, or card grid solely because it is a familiar generated pattern.
- Keep labels visible and actions explicit. An icon-only control needs an accessible name and an understandable affordance; a tooltip cannot be its only touch explanation.
- Represent loading, empty, error, disabled, selected, and success states. Preserve user input on recoverable failure and prevent unintentional duplicate submissions.
- Use real localized content and representative data lengths. Ellipsis is appropriate only when users can still access the information needed to act.
- Treat Material or Cupertino as available starting points. Preserve platform behavior and product identity; neither stock widgets nor custom drawing guarantee good design.

## Procedure

1. Identify the user task, reading order, main action, existing components, and agreed direction.
2. Describe the screen and state table before implementation. Map each visual value to a shared role.
3. Implement one representative state and the important failure/empty path with realistic content.
4. Inspect the rendered result at narrow and wide widths, large text, and applicable themes; exercise its main action.
5. Correct concrete hierarchy, spacing, clipping, or feedback defects and record before/after evidence.

## Required evidence

- [ ] The first-use walkthrough finds the main task without unexplained controls.
- [ ] Long content, empty data, loading, error, and repeated input remain usable.
- [ ] Color, text, spacing, shape, and icons follow recorded rules or documented exceptions.
- [ ] Actual screen captures and behavioral checks support the result; unviewed states remain unverified.

## Tradeoffs and failure handling

A visually distinctive interface can require extra assets, custom widgets, and maintenance. Spend that complexity on the agreed product goal. Do not reduce legibility or familiar interaction merely to appear original.

## Sources and related work

[Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
