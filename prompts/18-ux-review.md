# Review a complete user experience

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
