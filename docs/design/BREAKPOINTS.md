# Content-driven layout boundaries

Define when layout changes are useful and make boundary behavior testable.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Treat suggested width categories as hypotheses. A 600 or 1024 logical-pixel boundary may be useful, but it is not a universal rule for every component.
- Record each breakpoint with the content problem it solves, navigation/pane change, and minimum usable region sizes.
- Use parent constraints for embedded components; a wide app can contain a narrow panel.
- Consider height, text scale, locale, and input capabilities alongside width.

## Procedure

1. Start with the smallest supported usable layout and representative content.
2. Increase/decrease available space until a meaningful structural change is required.
3. Test just below, at, and just above each selected boundary, plus an intermediate width and a short viewport.
4. Check state preservation, focus order, and scroll reachability while crossing boundaries.

## Required evidence

- [ ] Every breakpoint is tied to a content or task requirement.
- [ ] Boundary checks use the product-selected values rather than unrelated fixed constants.
- [ ] Long translations and enlarged text remain usable near boundaries.

## Tradeoffs and failure handling

A fixed table is easy to share but can obscure component-level constraints. Use one shared vocabulary while allowing documented local adaptations. Remove obsolete boundaries when a flexible layout solves the problem.

## Sources and related work

[Adaptive behavior](RESPONSIVE_ADAPTIVE.md) and [Flutter guidance](https://docs.flutter.dev/ui/adaptive-responsive/best-practices).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
