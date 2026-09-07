# Error handling review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [ERROR_HANDLING](../docs/architecture/ERROR_HANDLING.md)
- [ERROR_POLICY](../docs/engineering/ERROR_POLICY.md)

## Procedure

1. Trace errors from origin through conversion, UI state, and reporting.
2. Find swallowed errors, duplicate reporting, unbounded retries, and sensitive output.
3. Define recoverable state and the next user action at the owning boundary.
4. Catch only where recovery or consistent reporting is possible; do not suppress defects globally.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
