# Rollback

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [ROLLBACK_WORKFLOW](../docs/workflow/ROLLBACK_WORKFLOW.md)
- [BACKUP_RECOVERY](../docs/operations/BACKUP_RECOVERY.md)

## Procedure

1. Inspect impact, a known-good artifact, schema compatibility, and authority for recovery.
2. Compare rollout pause, feature flags, restore, and forward-fix risks.
3. Perform the smallest authorized recovery action and verify data integrity and service metrics.
4. Record data effects and recovery time; a forward fix can be safer than restoring incompatible state.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
