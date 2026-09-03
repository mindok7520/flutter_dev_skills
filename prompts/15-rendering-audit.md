# Investigate rendering performance

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [RENDERING_PERFORMANCE](../docs/performance/RENDERING_PERFORMANCE.md)
- [REBUILD_OPTIMIZATION](../docs/performance/REBUILD_OPTIMIZATION.md)
- [SHADER_GUIDE](../docs/performance/SHADER_GUIDE.md)

## Procedure

1. Reproduce the slow scene with representative content and capture actual frame evidence.
2. Separate build/layout/paint work from raster/compositing and first-use asset or shader work.
3. Investigate expensive regions, lazy construction, intrinsic layout, effects, layers, and image decoding only when evidence points to them.
4. Avoid blanket RepaintBoundary, const, caching, or selector changes; evaluate their specific cost and memory tradeoff.
5. Reprofile the same scene and visually verify that required state updates and interactions still work.

## Evidence and completion

Slow-frame evidence, responsible stage, focused change, before/after timings, visual and memory checks.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
