# Payment integration

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [PAYMENTS](../docs/monetization/PAYMENTS.md)
- [PAYMENT_SECURITY](../docs/monetization/PAYMENT_SECURITY.md)

## Procedure

1. Confirm product type, countries, platforms, and provider against current official policies.
2. Implement server verification, an idempotent ledger, entitlement updates, and restoration contracts.
3. Test cancellation, pending state, duplicates, reordered webhooks, and recovery in a sandbox.
4. Preserve platform and country distinctions; do not assume in-app purchases are always mandatory or always optional.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
