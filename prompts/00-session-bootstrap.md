# Restore context and start a session

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [SESSION_BOOTSTRAP](../docs/agent/SESSION_BOOTSTRAP.md)
- [CONTEXT_RECOVERY](../docs/agent/CONTEXT_RECOVERY.md)

## Procedure

1. Inspect the current branch, uncommitted changes, manifest, toolchain, active plan, and user request; distinguish the material repository from a target app.
2. Recover decisions and completed evidence from files and the conversation. Do not infer approval from an unchecked plan or a generated recommendation.
3. Identify the next bounded task and its relevant baseline checks. If new UI direction is unresolved, start design consultation before implementation.
4. Continue already approved work without asking the same questions again, and leave a precise next action when a required answer is missing.

## Evidence and completion

Current state, authoritative references, next task, actual checks, unresolved decisions, and the next concrete action.
