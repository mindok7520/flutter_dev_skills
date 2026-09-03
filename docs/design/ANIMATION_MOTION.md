# Purposeful motion and animation

Use motion to communicate continuity, feedback, and attention without reducing control, accessibility, or performance.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Ask about purpose and visual constraints before adding new motion. Record its trigger, start/end state, duration/curve roles, and priority.
- Prefer built-in implicit animation for a simple property transition; use an owned controller for coordinated, reversible, or interruptible timelines.
- Consider flutter_animate for repeated effect composition and Rive for designer-authored interactive assets only when the project benefits. Compare runtime, asset, platform, and maintenance costs.
- Respect reduced-motion settings with a stable or simplified equivalent. Required information and success feedback must remain available without animation.
- Handle interruption, reverse, repeated taps, navigation, app backgrounding, and offscreen widgets. Do not leave perpetual tickers running unnoticed.
- Assign controller/listener/asset ownership and cleanup explicitly. Do not replay decorative entrances on every state rebuild.
- Measure layout, paint, raster, compositing, and memory costs. Web CSS compositor advice cannot be mechanically applied to Flutter rendering.

## Procedure

1. Confirm the intended user benefit and compare the static alternative.
2. Specify a timeline and state transitions in the screen specification.
3. Implement the smallest suitable mechanism using the installed package APIs.
4. Exercise interruption and reduced motion; inspect frame traces on a representative device in profile mode.
5. Capture the real result and retain a simpler fallback if the effect cannot meet the agreed constraints.

## Required evidence

- [ ] Motion has a documented purpose and does not delay essential input.
- [ ] Reduced motion, route exit, backgrounding, and repeated activation behave correctly.
- [ ] Controllers/resources are cleaned up and the representative workload stays within its measured budget.

## Tradeoffs and failure handling

More animation increases testing combinations and can compete with reading. A static transition may be the right result. Rive state-machine events must not become the authority for payment or domain state.

## Sources and related work

[Animation SDK guidance](https://docs.flutter.dev/ui/animations), [flutter_animate](https://github.com/gskinner/flutter_animate), [Rive Flutter](https://github.com/rive-app/rive-flutter), and [rendering performance](../performance/RENDERING_PERFORMANCE.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
