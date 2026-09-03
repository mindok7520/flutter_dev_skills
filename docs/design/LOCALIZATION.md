# Localized UI and content

Treat translated text and cultural formatting as inputs to layout and interaction design.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Product copy follows supported locales even when execution instructions are English.
- Externalize user-visible strings and avoid concatenating fragments that break grammar, plural forms, or screen-reader output.
- Verify Korean glyphs, fallback metrics, line wrapping, dates, numbers, currencies, and time zones in context.
- Design for short, typical, and long content. Do not reduce all text to fit a fixed screenshot.
- Support directional layout and traversal if right-to-left languages are in scope. Directional icons should be assessed by meaning.
- Keep essential information accessible when truncation is used; errors and primary actions must remain understandable.

## Procedure

1. Confirm launch locales and inspect the app's localization toolchain.
2. Use real localized examples and test expansion or pseudolocalization where supported.
3. Inspect narrow layouts, large text, dialogs, forms, and data tables.
4. Verify semantics, keyboard ordering, and recovery messages in the supported languages.

## Required evidence

- [ ] No important action or error is clipped or replaced with unreadable small text.
- [ ] Locale changes do not lose state or corrupt stored data.
- [ ] Generated localization files and visible copy match the source strings.

## Tradeoffs and failure handling

A translation review and a layout review catch different defects. Machine translation alone does not prove product terminology is appropriate; record unreviewed languages explicitly.

## Sources and related work

[Flutter internationalization](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization) and [Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
