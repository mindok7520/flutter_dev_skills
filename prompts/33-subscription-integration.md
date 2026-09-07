# Subscription integration

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [SUBSCRIPTIONS](../docs/monetization/SUBSCRIPTIONS.md)
- [ENTITLEMENTS](../docs/monetization/ENTITLEMENTS.md)

## Procedure

1. Map provider states to internal entitlements.
2. Implement renewal, grace periods, expiry, cancellation, refunds, and revocation.
3. Check missing or reordered notifications, account switching, and reconciliation.
4. Retain original provider state and verification history instead of losing meaning in a shared enum.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
