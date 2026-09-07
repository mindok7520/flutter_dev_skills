# Fix a reproducible bug

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [DEVELOPMENT_WORKFLOW](../docs/workflow/DEVELOPMENT_WORKFLOW.md)
- [TEST_STRATEGY](../docs/testing/TEST_STRATEGY.md)

## Procedure

1. Reproduce the reported input, state, environment, and failure before changing implementation.
2. Trace the causal boundary and distinguish the root cause from a visible symptom.
3. Restore the intended contract with a focused correction; do not bundle a redesign or state-management migration.
4. Reuse an approved design when fixing a visual regression; ask only if the correction changes an unresolved product decision.
5. Add or adjust a meaningful regression check, rerun the failing scenario, and verify affected recovery and lifecycle paths.

## Evidence and completion

Reproduction, root cause, targeted correction, regression evidence, and residual limitations.
