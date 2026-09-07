# Synchronize instructions and documentation

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [DOCUMENTATION_UPDATE_POLICY](../docs/agent/DOCUMENTATION_UPDATE_POLICY.md)
- [OVERVIEW](../docs/architecture/OVERVIEW.md)

## Procedure

1. Identify the authoritative code, user decisions, sources, and actual validation results affected by the change.
2. Update the canonical document and keep adapters as references instead of copying divergent policies.
3. Keep language boundaries explicit: reusable execution prose may be English while user explanation and the README map remain Korean.
4. Verify links, catalogs, skill metadata, examples, required files, and installed-project portability.
5. Record what changed, why, actual evidence, and remaining work without inventing approval or completion.

## Evidence and completion

Updated authoritative documents, synchronized discovery paths, source evidence, validation, and remaining discrepancies.
