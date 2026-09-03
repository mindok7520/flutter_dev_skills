# Evaluate and verify a shader effect

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
