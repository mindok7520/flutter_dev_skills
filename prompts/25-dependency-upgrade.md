# Upgrade dependencies deliberately

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [PACKAGE_POLICY](../docs/engineering/PACKAGE_POLICY.md)
- [DEPRECATION_POLICY](../docs/engineering/DEPRECATION_POLICY.md)

## Procedure

1. Read the current manifest and lockfile, then verify release notes and migration guidance for the exact proposed change.
2. Identify breaking APIs, generated output, renderer/runtime changes, security implications, and minimum platform/toolchain shifts.
3. Change a coherent dependency group and preserve unrelated versions and user edits.
4. Run the affected contracts and representative app behavior; use visual and frame checks for rendering, animation, and state-library changes.
5. Document actual results, unresolved compatibility, and the concrete rollback path.

## Evidence and completion

Version delta, migration changes, affected checks, compatibility evidence, and recovery instructions.
