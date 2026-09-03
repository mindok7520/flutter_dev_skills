# User experience and task flows

Design the complete route from user intent to a recoverable outcome, including interruptions and mistakes.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Consult the user about the target task and success criteria before an unscoped UX redesign.
- Make system status visible promptly. Distinguish a pending request, background refresh, confirmed save, and failure.
- Use familiar language and consistent action names. Recognizing options should be easier than remembering undocumented steps.
- Reveal complexity as needed while keeping essential information discoverable. A shorter screen is not useful if it hides a required step.
- Prevent foreseeable mistakes through constraints and clear labels. Explain what failed and how to recover near the relevant control.
- Preserve form values, selection, scroll position, and navigation context when appropriate. Define unsaved-change behavior.
- Use confirmation or undo in proportion to consequence and reversibility. Do not ask for confirmation on every harmless action.
- Make consent and cancellation understandable. Never hide rejection, preselect paid consent, or disguise advertising as a primary action.

## Procedure

1. Map entry, main task, success, cancellation, interruption, and retry with the user.
2. Identify prerequisites, permission requests, data availability, and offline behavior.
3. Write the shortest meaningful successful walkthrough and a likely recovery path.
4. Exercise the flow as a first-time user with representative content and an assistive/input mode where relevant.
5. Prioritize blocked tasks and lost work before cosmetic friction; validate the correction in the same flow.

## Required evidence

- [ ] A user can complete the task and understand the outcome without undocumented knowledge.
- [ ] Cancellation and failure do not trap the user or silently discard recoverable work.
- [ ] Observed usability findings are separated from assumptions and optional preferences.

## Tradeoffs and failure handling

A developer walkthrough is useful evidence but does not replace research with representative users. Record the participant and context when claiming observed usability; otherwise label the assessment as an expert review.

## Sources and related work

[Design workflow](DESIGN_WORKFLOW.md), [screen specification](SCREEN_SPEC_TEMPLATE.md), and [visual review](VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
