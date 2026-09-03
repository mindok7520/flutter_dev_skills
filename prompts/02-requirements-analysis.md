# Turn an idea into product requirements

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
