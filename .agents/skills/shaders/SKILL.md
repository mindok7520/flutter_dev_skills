---
name: shaders
description: "Use to evaluate and verify a shader effect in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Evaluate and verify a shader effect

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Confirm the desired effect, important targets, constraints, and acceptable static/reduced-motion fallback with the user.
2. Compare a built-in effect, image, custom paint, and fragment shader instead of assuming GPU code is automatically faster.
3. Inspect the installed SDK and renderer support, distinguishing Canvas shader use from ImageFilter.shader and other backend-specific APIs.
4. Specify asset loading, uniform and sampler contracts, coordinates, alpha expectations, mutable instance ownership, and resource disposal.
5. Exercise sizes, densities, transparency, resize, first use, sustained animation, backgrounding, and unsupported/load-failure paths.
6. Measure actual UI/raster timing, memory, sampling and affected-area costs, then report unsupported and unverified targets honestly.

## References to load for this task

- [SHADER_GUIDE](../../../docs/performance/SHADER_GUIDE.md)
- [PROFILING_GUIDE](../../../docs/performance/PROFILING_GUIDE.md)
- [DESIGN_WORKFLOW](../../../docs/design/DESIGN_WORKFLOW.md)
- [Task prompt](../../../prompts/60-shader-review.md)

## Completion contract

Alternative comparison, renderer matrix, uniform/lifecycle contract, fallback behavior, captures, and measured costs.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
