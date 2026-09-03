---
name: memory
description: "Use to investigate memory growth in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Investigate memory growth

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Specify the expected steady state and repeat route entry/exit, scrolling, account changes, or animation cycles that reproduce the growth.
2. Distinguish Dart heap, native/external memory, decoded images, caches, and GPU resources when tooling permits.
3. Compare snapshots and follow retaining paths to their actual owner; do not label a single high reading a leak.
4. Correct the lifetime or bounded cache policy without disposing shared resources still in use.
5. Repeat the same cycles and verify both memory behavior and the active consumers' correctness.

## References to load for this task

- [MEMORY_GUIDE](../../../docs/performance/MEMORY_GUIDE.md)
- [DEPENDENCY_INJECTION](../../../docs/architecture/DEPENDENCY_INJECTION.md)
- [Task prompt](../../../prompts/14-memory-audit.md)

## Completion contract

Measured growth pattern, retaining path, lifetime correction, repeated measurements, and remaining uncertainty.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
