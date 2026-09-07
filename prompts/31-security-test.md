# Security test

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [SECURITY_TESTING](../docs/security/SECURITY_TESTING.md)
- [SECURITY_TESTING](../docs/testing/SECURITY_TESTING.md)

## Procedure

1. Define authorized targets and threat-specific checks.
2. Test authorization bypass, forged inputs, replay, secret leakage, and oversized input where relevant.
3. Correct authorized findings and retest the same path.
4. An empty scanner report does not prove safety; inspect business authorization and payment rules separately.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
