# Analytics instrumentation

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [EVENT_SCHEMA](../docs/analytics/EVENT_SCHEMA.md)
- [PRIVACY_SAFE_ANALYTICS](../docs/analytics/PRIVACY_SAFE_ANALYTICS.md)

## Procedure

1. Choose only events needed for an explicit product metric.
2. Implement allowed fields, schema versions, deduplication, sampling, and consent.
3. Verify offline operation, collection failure, and consent withdrawal preserve app behavior and privacy.
4. Version incompatible event changes and record the transition period to preserve metric interpretation.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
