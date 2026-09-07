# Api contract review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [NETWORKING](../docs/architecture/NETWORKING.md)
- [AUTHORIZATION](../docs/security/AUTHORIZATION.md)

## Procedure

1. Inspect schema, input limits, pagination, authentication, and authorization.
2. Review timeouts, idempotency, error codes, compatibility, and retry contracts.
3. Test malformed input, older clients, duplicates, throttling, and server failure.
4. A timeout need not cancel the underlying operation. Do not retry an uncertain payment with a new idempotency key.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
