# Session handoff

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [HANDOFF_PROTOCOL](../docs/agent/HANDOFF_PROTOCOL.md)
- [CONTEXT_RECOVERY](../docs/agent/CONTEXT_RECOVERY.md)

## Procedure

1. Compare the current branch, commit, dirty files, and execution plan with actual artifacts.
2. Record completed and remaining criteria, approved decisions, failures, attempts, and evidence paths.
3. Write one exact next command or file-level action and its required environment for the receiving model.
4. Preserve secrets by linking sanitized evidence instead of copying raw logs. Re-read current Git state when resuming; an old passing result is not current verification.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
