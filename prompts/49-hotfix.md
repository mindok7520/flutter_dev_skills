# Hotfix

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [HOTFIX_WORKFLOW](../docs/workflow/HOTFIX_WORKFLOW.md)
- [INCIDENT_RESPONSE](../docs/security/INCIDENT_RESPONSE.md)

## Procedure

1. Determine impact, the current released version, and available immediate mitigation.
2. Use an issue branch from master for a minimal fix and regression verification.
3. Connect authorized release, develop synchronization, and post-change observation.
4. Avoid unrelated refactoring. When an immediate code change is riskier, evaluate disabling the affected feature or server-side mitigation.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
