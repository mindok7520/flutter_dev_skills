# Design and validate purposeful animation

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
