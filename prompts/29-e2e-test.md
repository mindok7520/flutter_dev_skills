# E2e test

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [E2E_TESTING](../docs/testing/E2E_TESTING.md)
- [TEST_DATA_POLICY](../docs/testing/TEST_DATA_POLICY.md)

## Procedure

1. Prepare isolated accounts, test data, and authorized provider sandboxes.
2. Compare outcomes from the UI through the server ledger.
3. Verify interrupted flows, resumption, duplicates, and test data cleanup.
4. Do not hide instability with retries; preserve boundary logs and a smaller reproduction.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
