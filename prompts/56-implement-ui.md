# Implement the approved screen

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [DESIGN_WORKFLOW](../docs/design/DESIGN_WORKFLOW.md)
- [SCREEN_SPEC_TEMPLATE](../docs/design/SCREEN_SPEC_TEMPLATE.md)
- [COMPONENT_GUIDELINES](../docs/design/COMPONENT_GUIDELINES.md)
- [STATE_MANAGEMENT](../docs/architecture/STATE_MANAGEMENT.md)

## Procedure

1. Read the actual approved brief or supplied design and scope. Resolve missing design decisions with the user before application implementation.
2. Specify layout, content, navigation, states, focus, feedback, and state ownership for the representative screen.
3. Reuse production components and token roles; keep business authority and network effects outside presentation widgets.
4. Implement realistic loading, data, empty, error, retry, and input behavior applicable to the screen.
5. Verify adaptive layouts, large text, supported inputs, and cleanup; inspect actual captures rather than only code.
6. Correct discrepancies within the agreed direction and document any unresolved target environment.

## Evidence and completion

Implemented screen and state contracts, reused/new components, functional and visual evidence, and remaining gaps.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
