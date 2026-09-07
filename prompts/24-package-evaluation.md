# Evaluate a package from evidence

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [PACKAGE_POLICY](../docs/engineering/PACKAGE_POLICY.md)
- [DEPENDENCY_RULES](../docs/architecture/DEPENDENCY_RULES.md)

## Procedure

1. State the requirement the existing SDK or project cannot meet, then identify only plausible candidates.
2. Inspect official source, releases, license, maintenance, supported platforms, installed-version compatibility, and issue patterns.
3. Compare API fit, ownership/disposal, testing, binary/runtime cost, migration, and the option of no new dependency.
4. For state, animation, shader, or design packages, follow the corresponding specialist guidance and preserve the approved UI direction.
5. Use a small relevant experiment when necessary; do not install candidates or add a global convention merely from popularity.

## Evidence and completion

Candidate comparison, versioned sources, concrete tradeoffs, experiment evidence, and justified decision.
