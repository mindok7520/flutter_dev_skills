# Release readiness

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [RELEASE_CHECKLIST](../docs/release/RELEASE_CHECKLIST.md)
- [QUALITY_GATES](../docs/testing/QUALITY_GATES.md)

## Procedure

1. Identify the release SHA, version, configuration, tests, signing, policy, and operations evidence.
2. Separate missing work and blocking conditions by platform.
3. Run the actual readiness checker when installed and assess its evidence rather than its exit code alone.
4. An unconfigured base should fail readiness; never invent evidence or enable readiness merely to pass a gate.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
