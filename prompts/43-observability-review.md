# Observability review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [OBSERVABILITY](../docs/operations/OBSERVABILITY.md)
- [CRASH_REPORTING](../docs/analytics/CRASH_REPORTING.md)

## Procedure

1. Connect metrics, logs, traces, and correlation identifiers for critical operations.
2. Inspect sampling, bounded queues, consent, secrets, and retention.
3. Use a test fault and alert to verify investigation and response are possible.
4. Separate impact-based alerts from long-term trends; document gaps and actionable owners.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
