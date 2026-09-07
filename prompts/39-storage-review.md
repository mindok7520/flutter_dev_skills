# Storage review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [LOCAL_STORAGE](../docs/architecture/LOCAL_STORAGE.md)
- [PLATFORM_STORAGE_SECURITY](../docs/security/PLATFORM_STORAGE_SECURITY.md)

## Procedure

1. Identify data classification, ownership, schema, and key lifetime.
2. Review migration, atomicity, deletion, backup, and corruption recovery.
3. Verify account switching, full storage, interrupted writes, and key invalidation.
4. Keep caches recoverable and avoid persisting unnecessary personal data; identify the authoritative business ledger.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
