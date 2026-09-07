# Ad integration

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [ADS](../docs/monetization/ADS.md)
- [AD_PRIVACY_CONSENT](../docs/monetization/AD_PRIVACY_CONSENT.md)

## Procedure

1. Confirm supported platforms, ad formats, consent requirements, and test identifiers.
2. Implement SDK initialization, ad ownership and disposal, frequency limits, and failure UI.
3. Verify refusal, withdrawal, offline operation, re-entry, and memory behavior.
4. Measure abandonment, accidental clicks, and complaints alongside revenue; reuse approved visual decisions.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
