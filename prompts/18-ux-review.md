# Review a complete user experience

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [UX_GUIDELINES](../docs/design/UX_GUIDELINES.md)
- [USER_JOURNEYS](../docs/product/USER_JOURNEYS.md)
- [SCREEN_SPEC_TEMPLATE](../docs/design/SCREEN_SPEC_TEMPLATE.md)

## Procedure

1. Ask for the main task and user context if they were not supplied; a scoped audit request already supplies its review direction.
2. Walk through entry, prerequisites, successful completion, interruption, cancellation, and recovery.
3. Check status visibility, understandable language, retained input, discoverable actions, and proportionate confirmation.
4. Look for blocked tasks, surprising side effects, hidden cancellation, coercive consent, or misleading success feedback.
5. Separate an expert review from observations of representative users and prioritize the cost to the user.

## Evidence and completion

User journey, observed obstacles, impact, recovery gaps, improvement order, and evidence limitations.
