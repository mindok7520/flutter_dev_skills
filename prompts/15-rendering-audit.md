# Investigate rendering performance

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

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
