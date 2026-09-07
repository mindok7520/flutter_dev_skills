# Repository analysis

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [OVERVIEW](../docs/architecture/OVERVIEW.md)
- [PACKAGE_POLICY](../docs/engineering/PACKAGE_POLICY.md)

## Procedure

1. Inspect entry points, modules, dependencies, platforms, CI, and tests.
2. Separate implemented behavior from plans and rank risks by user impact.
3. Identify improvement candidates using actual file paths before editing.
4. Prefer the minimum boundaries needed for current complexity; document significant decisions in an ADR.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
