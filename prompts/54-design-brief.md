# Ask the user and establish a design brief

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [DESIGN_WORKFLOW](../docs/design/DESIGN_WORKFLOW.md)
- [PRODUCT_DESIGN_BRIEF](../docs/design/PRODUCT_DESIGN_BRIEF.md)

## Procedure

1. Inspect PROJECT.md, existing UI, prior decisions, and any references before asking an informed question.
2. Ask about the missing user task, audience, preferred direction, real content, platforms, and constraints; ask one focused question at a time or at most three related questions.
3. Wait for the answer before producing a new design. A recommendation, preselected option, or silence is not user agreement.
4. If the user has no preference, ask whether to use a reasoned recommendation; explicit delegation then supplies the decision.
5. Record confirmed answers, assumptions, unresolved questions, and the first representative screen in the product brief.
6. Prepare the next design comparison without creating application code in the materials repository.

## Evidence and completion

User questions and answers, a product-specific brief with honest decision status, and the next design action.
