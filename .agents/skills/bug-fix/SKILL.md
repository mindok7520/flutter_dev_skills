---
name: bug-fix
description: "Use to fix a reproducible bug in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Fix a reproducible bug

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Reproduce the reported input, state, environment, and failure before changing implementation.
2. Trace the causal boundary and distinguish the root cause from a visible symptom.
3. Restore the intended contract with a focused correction; do not bundle a redesign or state-management migration.
4. Reuse an approved design when fixing a visual regression; ask only if the correction changes an unresolved product decision.
5. Add or adjust a meaningful regression check, rerun the failing scenario, and verify affected recovery and lifecycle paths.

## References to load for this task

- [DEVELOPMENT_WORKFLOW](../../../docs/workflow/DEVELOPMENT_WORKFLOW.md)
- [TEST_STRATEGY](../../../docs/testing/TEST_STRATEGY.md)
- [Task prompt](../../../prompts/08-fix-bug.md)

## Completion contract

Reproduction, root cause, targeted correction, regression evidence, and residual limitations.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
