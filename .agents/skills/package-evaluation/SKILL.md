---
name: package-evaluation
description: "Use to evaluate a package from evidence in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Evaluate a package from evidence

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. State the requirement the existing SDK or project cannot meet, then identify only plausible candidates.
2. Inspect official source, releases, license, maintenance, supported platforms, installed-version compatibility, and issue patterns.
3. Compare API fit, ownership/disposal, testing, binary/runtime cost, migration, and the option of no new dependency.
4. For state, animation, shader, or design packages, follow the corresponding specialist guidance and preserve the approved UI direction.
5. Use a small relevant experiment when necessary; do not install candidates or add a global convention merely from popularity.

## References to load for this task

- [PACKAGE_POLICY](../../../docs/engineering/PACKAGE_POLICY.md)
- [DEPENDENCY_RULES](../../../docs/architecture/DEPENDENCY_RULES.md)
- [Task prompt](../../../prompts/24-package-evaluation.md)

## Completion contract

Candidate comparison, versioned sources, concrete tradeoffs, experiment evidence, and justified decision.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
