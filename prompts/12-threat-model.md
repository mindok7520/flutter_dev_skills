# Threat model

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [THREAT_MODEL](../docs/security/THREAT_MODEL.md)
- [DATA_INVENTORY](../docs/privacy/DATA_INVENTORY.md)

## Procedure

1. Inventory assets, actors, entry points, and external providers.
2. Derive threats from attacker capabilities and trust boundaries.
3. Connect mitigation, detection, recovery, residual risk, and an owner.
4. Prioritize by actual asset value and exposure rather than listing all threats as equally urgent.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
