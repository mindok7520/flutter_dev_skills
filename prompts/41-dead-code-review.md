# Dead code review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [CLEAN_CODE](../docs/engineering/CLEAN_CODE.md)
- [DEPRECATION_POLICY](../docs/engineering/DEPRECATION_POLICY.md)

## Procedure

1. Check static references, dynamic registration, platform conditions, and generated code paths.
2. Establish evidence that each removal candidate is unreachable or obsolete.
3. Remove only authorized candidates and verify affected builds, tests, and documentation.
4. Do not confuse shorter code with simpler behavior or remove error handling and lifetime management as clutter.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
