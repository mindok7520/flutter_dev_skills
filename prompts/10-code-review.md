# Code review

Apply [AGENTS.md](../AGENTS.md) and the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Report in Korean; keep code and comments in English.

## Inputs

Read the goal, acceptance criteria, actual files and toolchain, current plan, and relevant user decisions. Preserve existing work and distinguish a review request from authorization to implement.

## Task-specific references

- [CODE_REVIEW](../docs/workflow/CODE_REVIEW.md)
- [SECURE_CODING](../docs/security/SECURE_CODING.md)

## Procedure

1. Read requirements, the diff, and affected callers together.
2. Prioritize correctness, authorization, resource lifetime, and data loss.
3. Report severity, reproduction conditions, file and line, impact, and a concrete correction.
4. Avoid speculative findings. State the review scope and unavailable evidence even when no defect is found.

## Evidence and completion

Report the task-specific artifacts and decisions from the procedure, source paths, actual checks and results, unverified conditions, and next action. For authorized changes, update the active plan and satisfy the relevant quality gates from the shared contract.
