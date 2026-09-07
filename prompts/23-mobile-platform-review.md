# Mobile platform review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [MOBILE_SECURITY](../docs/security/MOBILE_SECURITY.md)
- [NATIVE_INTEGRATION](../docs/architecture/NATIVE_INTEGRATION.md)

## Procedure

1. Inspect permissions, deep links, background behavior, and native resource lifetimes.
2. Review minimum platform versions, signing, privacy, and plugin differences.
3. Exercise the changed boundaries on actual supported Android and iOS environments.
4. Check current official platform requirements; generated defaults alone do not prove release readiness.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
