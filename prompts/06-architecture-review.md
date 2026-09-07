# Review architecture against code

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [APP_ARCHITECTURE](../docs/architecture/APP_ARCHITECTURE.md)
- [DEPENDENCY_RULES](../docs/architecture/DEPENDENCY_RULES.md)
- [DEPENDENCY_INJECTION](../docs/architecture/DEPENDENCY_INJECTION.md)

## Procedure

1. Trace actual imports, construction, state writes, and external calls for the requested feature.
2. Look for cycles, implicit globals, transport details in UI, competing state owners, and objects retained across invalid lifetimes.
3. Distinguish a demonstrated defect from a style preference or an optional architectural convention.
4. Recommend the smallest corrective boundary and evaluate migration, compatibility, testing, and cleanup implications.
5. For a review-only request, report evidence and recommendations without starting an unrelated rewrite.

## Evidence and completion

Prioritized findings with code paths, failure conditions, impact, corrections, and explicitly limited review coverage.
