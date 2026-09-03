# Restore context and start a session

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
