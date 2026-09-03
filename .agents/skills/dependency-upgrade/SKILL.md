---
name: dependency-upgrade
description: "Use to upgrade dependencies deliberately in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Upgrade dependencies deliberately

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Read the current manifest and lockfile, then verify release notes and migration guidance for the exact proposed change.
2. Identify breaking APIs, generated output, renderer/runtime changes, security implications, and minimum platform/toolchain shifts.
3. Change a coherent dependency group and preserve unrelated versions and user edits.
4. Run the affected contracts and representative app behavior; use visual and frame checks for rendering, animation, and state-library changes.
5. Document actual results, unresolved compatibility, and the concrete rollback path.

## References to load for this task

- [PACKAGE_POLICY](../../../docs/engineering/PACKAGE_POLICY.md)
- [DEPRECATION_POLICY](../../../docs/engineering/DEPRECATION_POLICY.md)
- [Task prompt](../../../prompts/25-dependency-upgrade.md)

## Completion contract

Version delta, migration changes, affected checks, compatibility evidence, and recovery instructions.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
