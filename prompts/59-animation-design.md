# Design and validate purposeful animation

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [ANIMATION_MOTION](../docs/design/ANIMATION_MOTION.md)
- [DESIGN_WORKFLOW](../docs/design/DESIGN_WORKFLOW.md)
- [RENDERING_PERFORMANCE](../docs/performance/RENDERING_PERFORMANCE.md)

## Procedure

1. Ask the user about the visual purpose, important interaction, motion preference, and constraints unless the approved brief already supplies them.
2. Compare a static or built-in transition with controller-driven animation, flutter_animate, or a Rive asset when relevant.
3. Specify triggers, start/end states, timing roles, interruption/reversal, repeated input, and the reduced-motion equivalent.
4. Define controller, listener, asset, and ticker ownership; pause or stop work when offscreen or backgrounded as appropriate.
5. Implement only inside the approved visual scope and exercise navigation, rapid changes, and cleanup.
6. Inspect the actual motion and capture representative frame/memory evidence; preserve usability if the effect is removed.

## Evidence and completion

Motion purpose and timeline, mechanism decision, lifecycle and reduced-motion behavior, actual visual/performance evidence.
