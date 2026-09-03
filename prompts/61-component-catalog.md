# Maintain a useful component catalog

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [COMPONENT_GUIDELINES](../docs/design/COMPONENT_GUIDELINES.md)
- [DESIGN_SYSTEM](../docs/design/DESIGN_SYSTEM.md)
- [GOLDEN_TESTING](../docs/testing/GOLDEN_TESTING.md)

## Procedure

1. Inspect the actual reusable components and agreed visual system; ask about missing design intent before creating new visual variants.
2. Use the existing local showcase or compare a minimal in-app catalog with Widgetbook when the component scope justifies it.
3. Render production components with deterministic fixtures for applicable default, focus, selected, disabled, pending, error, empty, and long-content states.
4. Include relevant themes, locales, text scaling, and width constraints without generating a separate demonstration-only implementation.
5. Exercise interactions and semantics, then review a small set of meaningful golden baselines.
6. Document how examples stay synchronized; hosted services and new dependencies remain explicit choices.

## Evidence and completion

Component/state inventory, local examples, interaction/accessibility evidence, reviewed baselines, and maintenance rules.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
