---
name: visual-review
description: "Use to inspect and refine the running UI in a Flutter app. Compare actual captures and interactions against an agreed design, report specific defects, and verify authorized corrections."
---

# Inspect and refine the running UI

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Confirm the target screen, task, and approved reference or review priorities if missing.
2. Run the app in an available target environment and record commit, viewport, pixel ratio, font, locale, text scale, theme, and fixture.
3. Capture and actually view the relevant states, then exercise the primary action, keyboard flow, and important recovery path.
4. Report specific hierarchy, typography, spacing, contrast, content, interaction, or motion discrepancies with their user impact.
5. When correction is authorized, fix the highest-impact discrepancy and recapture under comparable conditions.
6. Stop when the agreed criteria are met; never approve a baseline or claim visual success without inspecting the relevant image.

## References to load for this task

- [VISUAL_REVIEW](../../../docs/design/VISUAL_REVIEW.md)
- [GOLDEN_TESTING](../../../docs/testing/GOLDEN_TESTING.md)
- [SCREEN_SPEC_TEMPLATE](../../../docs/design/SCREEN_SPEC_TEMPLATE.md)
- [Task prompt](../../../prompts/57-visual-review.md)

## Completion contract

Reproducible captures, criterion-level findings, actual interaction results, before/after comparison, and unverified cells.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
