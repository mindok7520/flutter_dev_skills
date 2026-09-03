---
name: ui-design
description: "Use for new UI/UX, screen redesigns, or choosing a visual direction. Ask the user about missing goals and constraints before design work, establish the brief, and agree the direction before implementation."
---

# Ask the user and establish a design brief

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Inspect PROJECT.md, existing UI, prior decisions, and any references before asking an informed question.
2. Ask about the missing user task, audience, preferred direction, real content, platforms, and constraints; ask one focused question at a time or at most three related questions.
3. Wait for the answer before producing a new design. A recommendation, preselected option, or silence is not user agreement.
4. If the user has no preference, ask whether to use a reasoned recommendation; explicit delegation then supplies the decision.
5. Record confirmed answers, assumptions, unresolved questions, and the first representative screen in the product brief.
6. Prepare the next design comparison without creating application code in the materials repository.

Continue with [visual direction](../../../prompts/55-visual-direction.md) after the brief, then [UI implementation](../../../prompts/56-implement-ui.md) within the approved scope. For a shared system, use [component catalog](../../../prompts/61-component-catalog.md).

## References to load for this task

- [DESIGN_WORKFLOW](../../../docs/design/DESIGN_WORKFLOW.md)
- [PRODUCT_DESIGN_BRIEF](../../../docs/design/PRODUCT_DESIGN_BRIEF.md)
- [Task prompt](../../../prompts/54-design-brief.md)

## Completion contract

User questions and answers, a product-specific brief with honest decision status, and the next design action.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
