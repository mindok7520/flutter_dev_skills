---
name: session-bootstrap
description: "Use to restore context and start a session in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Restore context and start a session

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Inspect the current branch, uncommitted changes, manifest, toolchain, active plan, and user request; distinguish the material repository from a target app.
2. Recover decisions and completed evidence from files and the conversation. Do not infer approval from an unchecked plan or a generated recommendation.
3. Identify the next bounded task and its relevant baseline checks. If new UI direction is unresolved, start design consultation before implementation.
4. Continue already approved work without asking the same questions again, and leave a precise next action when a required answer is missing.

## References to load for this task

- [SESSION_BOOTSTRAP](../../../docs/agent/SESSION_BOOTSTRAP.md)
- [CONTEXT_RECOVERY](../../../docs/agent/CONTEXT_RECOVERY.md)
- [Task prompt](../../../prompts/00-session-bootstrap.md)

## Completion contract

Current state, authoritative references, next task, actual checks, unresolved decisions, and the next concrete action.
