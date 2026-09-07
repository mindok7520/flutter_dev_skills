# Evaluate and verify a shader effect

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [SHADER_GUIDE](../docs/performance/SHADER_GUIDE.md)
- [PROFILING_GUIDE](../docs/performance/PROFILING_GUIDE.md)
- [DESIGN_WORKFLOW](../docs/design/DESIGN_WORKFLOW.md)

## Procedure

1. Confirm the desired effect, important targets, constraints, and acceptable static/reduced-motion fallback with the user.
2. Compare a built-in effect, image, custom paint, and fragment shader instead of assuming GPU code is automatically faster.
3. Inspect the installed SDK and renderer support, distinguishing Canvas shader use from ImageFilter.shader and other backend-specific APIs.
4. Specify asset loading, uniform and sampler contracts, coordinates, alpha expectations, mutable instance ownership, and resource disposal.
5. Exercise sizes, densities, transparency, resize, first use, sustained animation, backgrounding, and unsupported/load-failure paths.
6. Measure actual UI/raster timing, memory, sampling and affected-area costs, then report unsupported and unverified targets honestly.

## Evidence and completion

Alternative comparison, renderer matrix, uniform/lifecycle contract, fallback behavior, captures, and measured costs.
