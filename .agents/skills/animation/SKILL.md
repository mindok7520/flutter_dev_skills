---
name: animation
description: "Use to design and validate purposeful animation in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Design and validate purposeful animation

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Ask the user about the visual purpose, important interaction, motion preference, and constraints unless the approved brief already supplies them.
2. Compare a static or built-in transition with controller-driven animation, flutter_animate, or a Rive asset when relevant.
3. Specify triggers, start/end states, timing roles, interruption/reversal, repeated input, and the reduced-motion equivalent.
4. Define controller, listener, asset, and ticker ownership; pause or stop work when offscreen or backgrounded as appropriate.
5. Implement only inside the approved visual scope and exercise navigation, rapid changes, and cleanup.
6. Inspect the actual motion and capture representative frame/memory evidence; preserve usability if the effect is removed.

## References to load for this task

- [ANIMATION_MOTION](../../../docs/design/ANIMATION_MOTION.md)
- [DESIGN_WORKFLOW](../../../docs/design/DESIGN_WORKFLOW.md)
- [RENDERING_PERFORMANCE](../../../docs/performance/RENDERING_PERFORMANCE.md)
- [Task prompt](../../../prompts/59-animation-design.md)

## Completion contract

Motion purpose and timeline, mechanism decision, lifecycle and reduced-motion behavior, actual visual/performance evidence.
