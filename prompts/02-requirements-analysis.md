# Turn an idea into product requirements

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [REQUIREMENTS](../docs/product/REQUIREMENTS.md)
- [PROJECT.md](../PROJECT.md)
- [PRODUCT_DESIGN_BRIEF](../docs/design/PRODUCT_DESIGN_BRIEF.md)

## Procedure

1. Separate the user problem, audience, key task, first-release scope, exclusions, constraints, and measurable acceptance criteria.
2. Inspect the current product definition and implementation. Do not mark planned features as already built.
3. Ask focused questions about missing product decisions, at most three closely related questions at a time; wait for the answers that determine scope.
4. For UI work, capture preferred direction, references, real content, accessibility, platforms, and the main screen through the design workflow.
5. Write confirmed decisions separately from assumptions and open questions, and derive the first complete implementation slice.

## Evidence and completion

Updated product definition, requirement identifiers, acceptance criteria, exclusions, open decisions, and first task.
