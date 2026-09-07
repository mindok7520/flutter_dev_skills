---
name: performance
description: "Use to investigate a performance problem in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Investigate a performance problem

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Define the user-visible delay, representative workload, target device, refresh rate, build mode, renderer, and acceptance budget.
2. Capture comparable baseline traces and distributions; separate cold/warm conditions and avoid reporting debug timing as release performance.
3. Locate the dominant cost in CPU work, build/layout, raster/compositing, network, memory, or assets.
4. Change one causal factor and rerun the same scenario, preserving correctness, accessibility, and approved visual behavior.
5. Compare raw evidence and variability, including costs moved to another stage, and retain only justified optimizations.

## References to load for this task

- [PERFORMANCE_GUIDE](../../../docs/performance/PERFORMANCE_GUIDE.md)
- [PROFILING_GUIDE](../../../docs/performance/PROFILING_GUIDE.md)
- [Task prompt](../../../prompts/13-performance-audit.md)

## Completion contract

Environment, workload, raw profiles, causal hypothesis, before/after distribution, and regression risks.
