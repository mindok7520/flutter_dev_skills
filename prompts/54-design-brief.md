# Ask the user and establish a design brief

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
