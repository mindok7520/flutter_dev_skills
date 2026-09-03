# Accessible interaction and presentation

Make the core task usable with assistive technology, different input methods, and visual or motor constraints.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Use WCAG 2.2 AA as a web accessibility reference, while checking applicable platform guidance and product obligations separately.
- Check text contrast against actual backgrounds: generally 4.5:1 for normal text and 3:1 for qualifying large text. Essential non-text controls and focus cues generally need 3:1; understand the criterion exceptions.
- Use appropriately sized touch regions. Android 48 logical pixels and iOS 44 points are common platform targets; WCAG 2.2 web target sizing is a different criterion with spacing and other exceptions.
- Give controls accessible names, roles, values, states, and predictable traversal. Exclude purely decorative content and avoid duplicate announcements.
- Support text enlargement, localized content, keyboard-only use, and visible unobscured focus. Do not encode success, error, or selection only with color.
- Provide alternatives to drag-only or gesture-only actions when needed. Respect reduced motion and avoid flashes or animation that prevents interaction.
- Explain errors in context and announce important asynchronous changes without flooding the accessibility tree.

## Procedure

1. Identify the target flow, platforms, input modes, and accessibility expectations with the user.
2. Run available semantics, contrast, and target-size checks in the target app.
3. Complete the flow with keyboard and the relevant native screen reader; inspect focus after dialogs, navigation, and errors.
4. Test large text, long translations, reduced motion, and state changes using actual rendered screens.

## Required evidence

- [ ] The main task works with the relevant assistive/input modes and documented environments.
- [ ] Errors and dynamic updates have useful, nonduplicated announcements.
- [ ] Automatic checks and manual observations are recorded separately.

## Tradeoffs and failure handling

Automated tests cover only a subset of accessibility. A pass is not a claim of legal compliance or suitability for every disability. Prefer a clear, tested interaction over decorative novelty that requires additional explanation.

## Sources and related work

[Flutter accessibility](https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility), [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/), and [Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
