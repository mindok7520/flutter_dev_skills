# Security review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [SECURITY_ARCHITECTURE](../docs/security/SECURITY_ARCHITECTURE.md)
- [SECURITY_TESTING](../docs/security/SECURITY_TESTING.md)

## Procedure

1. Identify assets, inputs, and trust boundaries.
2. Inspect authentication, authorization, secrets, logging, supply chain, and storage.
3. Ground findings in feasible attack paths and gaps in actual defenses.
4. Do not treat obfuscation or root detection as independent security boundaries; prioritize server validation and secret separation.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
