---
name: documentation-sync
description: "Use to synchronize instructions and documentation in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Synchronize instructions and documentation

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Identify the authoritative code, user decisions, sources, and actual validation results affected by the change.
2. Update the canonical document and keep adapters as references instead of copying divergent policies.
3. Keep language boundaries explicit: reusable execution prose may be English while user explanation and the README map remain Korean.
4. Verify links, catalogs, skill metadata, examples, required files, and installed-project portability.
5. Record what changed, why, actual evidence, and remaining work without inventing approval or completion.

## References to load for this task

- [DOCUMENTATION_UPDATE_POLICY](../../../docs/agent/DOCUMENTATION_UPDATE_POLICY.md)
- [OVERVIEW](../../../docs/architecture/OVERVIEW.md)
- [Task prompt](../../../prompts/51-documentation-sync.md)

## Completion contract

Updated authoritative documents, synchronized discovery paths, source evidence, validation, and remaining discrepancies.
