# Integration test

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [INTEGRATION_TESTING](../docs/testing/INTEGRATION_TESTING.md)
- [CROSS_PLATFORM_MATRIX](../docs/testing/CROSS_PLATFORM_MATRIX.md)

## Procedure

1. Record device, OS, SDK, and test environment.
2. Run critical flows across the changed platform boundaries.
3. Verify recovery from permission denial, lifecycle transitions, and network failures.
4. Mark unavailable device toolchains as untested; verify the installed SDK browser test procedure before using it.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
