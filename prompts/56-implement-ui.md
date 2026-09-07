# Implement the approved screen

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

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
