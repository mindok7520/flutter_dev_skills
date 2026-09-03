# Responsive and adaptive behavior

Adapt information structure to available space and input capabilities while preserving user state.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Use the actual constraints available to a component rather than a device name or an assumption that a platform is always narrow.
- Choose breakpoints when content or navigation needs to change. Record the decision and test around the boundary.
- Constrain long reading lines and avoid stretching mobile layouts across a large window. Change navigation or pane structure when the task benefits.
- Preserve selection, drafts, scroll position, and navigation context across resize, rotation, and split-screen transitions.
- Account for safe areas, display cutouts, keyboard insets, short landscape heights, pointer input, and large text.
- Keep reading and focus order coherent when visual arrangement changes; do not duplicate hidden interactive copies of a screen.

## Procedure

1. Confirm supported platforms and the important user task, then inspect current layout constraints.
2. Specify narrow, expanded, and short-height behavior for real content.
3. Resize continuously through each chosen boundary and repeat with a keyboard and enlarged text.
4. Verify preserved state and capture representative layouts for visual review.

## Required evidence

- [ ] Critical controls remain reachable without unintended horizontal scrolling or clipped content.
- [ ] Resize/rotation does not reset a draft or cause duplicate requests.
- [ ] The expanded layout has purposeful hierarchy and usable reading width.

## Tradeoffs and failure handling

More breakpoints increase maintenance and test combinations. Prefer a few content-driven structural changes with flexible behavior between them. Validate native interactions on the target platform rather than inferring them from a browser resize.

## Sources and related work

[Flutter adaptive best practices](https://docs.flutter.dev/ui/adaptive-responsive/best-practices) and [Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
