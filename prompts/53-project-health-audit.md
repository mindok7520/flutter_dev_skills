# Project health audit

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [CI_CD](../docs/operations/CI_CD.md)
- [PACKAGE_POLICY](../docs/engineering/PACKAGE_POLICY.md)

## Procedure

1. Inspect dependencies, CI, failing tests, long-lived plans, feature flags, and documentation drift.
2. Rank security, performance, and maintenance risks by user impact.
3. Propose bounded improvement tasks with measurable acceptance criteria; implement within the authorized scope.
4. Repository files do not activate hosting protection rules; verify actual settings separately without assuming service-tier support.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
