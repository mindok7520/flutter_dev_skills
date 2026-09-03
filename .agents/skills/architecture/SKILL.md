---
name: architecture
description: "Use to design architecture for the actual product in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Design architecture for the actual product

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Map the existing modules, one important user flow, state owners, external trust boundaries, and resource lifetimes.
2. Compare the current approach with a feasible alternative using correctness, isolation, testing, complexity, and migration cost.
3. Separate presentation, state transitions, repository coordination, and external services; add domain/use-case layers only for actual complexity.
4. Evaluate state-management choices with prompt 58 when needed instead of silently installing a preferred package.
5. Record the decision and verify it with a representative slice and contract tests. UI direction changes still require the design consultation.

## References to load for this task

- [APP_ARCHITECTURE](../../../docs/architecture/APP_ARCHITECTURE.md)
- [STATE_MANAGEMENT](../../../docs/architecture/STATE_MANAGEMENT.md)
- [DEPENDENCY_RULES](../../../docs/architecture/DEPENDENCY_RULES.md)
- [Task prompt](../../../prompts/05-architecture-design.md)

## Completion contract

Responsibility and data-flow map, ownership contracts, alternatives, architecture decision, migration and verification plan.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
