# Upgrade dependencies deliberately

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [PACKAGE_POLICY](../docs/engineering/PACKAGE_POLICY.md)
- [DEPRECATION_POLICY](../docs/engineering/DEPRECATION_POLICY.md)

## Procedure

1. Read the current manifest and lockfile, then verify release notes and migration guidance for the exact proposed change.
2. Identify breaking APIs, generated output, renderer/runtime changes, security implications, and minimum platform/toolchain shifts.
3. Change a coherent dependency group and preserve unrelated versions and user edits.
4. Run the affected contracts and representative app behavior; use visual and frame checks for rendering, animation, and state-library changes.
5. Document actual results, unresolved compatibility, and the concrete rollback path.

## Evidence and completion

Version delta, migration changes, affected checks, compatibility evidence, and recovery instructions.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
