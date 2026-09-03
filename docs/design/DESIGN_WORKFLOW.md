# Consult, design, implement, inspect

Use this workflow for new screens, substantial layout or navigation changes, and new motion or visual effects. It applies even when the request enters through a general feature prompt. Combine it with the [shared contract](../agent/PROMPT_CONTRACT.md).

## 1. Inspect and ask before starting design

Read `PROJECT.md`, the existing product design brief, the relevant screen, and any user-provided references. Determine whether this is an audit, a new design, a redesign, or implementation of an already approved specification. Read-only inspection may happen before asking so the question is informed.

Ask the user one focused question at a time, or at most three tightly related questions. Start with the decision that changes the work most. Cover missing information about:

- Primary user and task; what the screen must help them do.
- Platforms, input methods, language, accessibility needs, and real content.
- Desired feeling and information density; references and the exact qualities to borrow.
- Existing brand, components, constraints, prohibited directions, and implementation scope.

Wait for the user's answer before producing a new visual direction, mockup, prototype, or application UI. Do not invent preferences, interpret silence as agreement, or assume that a default option was selected. If images cannot be viewed, say so and request an accessible image or textual description rather than claiming to have inspected them.

For an audit, ask for the target flow and review priorities when they were not supplied. A scoped review request already answers that question; inspect and report without imposing a design-approval ceremony. If the user asks for a new design but has no preferences, ask whether to proceed with a reasoned recommendation; an explicit delegation then supplies that decision.

## 2. Record the brief and compare approaches

Use [the product design brief](PRODUCT_DESIGN_BRIEF.md). Record confirmed answers separately from assumptions and open decisions. A small change may use a short section in its execution plan; a new product or cross-screen redesign needs a durable brief.

Use real or explicitly representative content. Compare two feasible directions on one important screen when the visual direction is open. Explain differences in hierarchy, density, typography, imagery, navigation, and implementation cost. A fixed brand or supplied design does not need artificial alternatives. Reference patterns by purpose; do not copy unrelated product chrome or require novelty at the expense of usability.

Present a concise proposal and ask which direction the user wants before application implementation. Readable sketches or explicitly requested design artifacts can support that decision. Record the user's chosen direction, scope, and evidence in the plan. An earlier explicit request to implement a supplied complete design already provides this approval; cite and reuse it.

## 3. Specify the screen and shared rules

Use [the screen specification](SCREEN_SPEC_TEMPLATE.md). Cover navigation, real content, states, actions, feedback, focus, and recovery before polishing decoration. Define semantic color roles, text roles, spacing, shape, motion, and reusable component states using [design tokens](DESIGN_TOKENS.md) and [component guidelines](COMPONENT_GUIDELINES.md).

Check [UI](UI_GUIDELINES.md), [UX](UX_GUIDELINES.md), [accessibility](ACCESSIBILITY.md), and [adaptive behavior](RESPONSIVE_ADAPTIVE.md). Choose the smallest suitable implementation; a shader, custom painter, animation package, or new state manager needs an explicit benefit and cost assessment.

## 4. Implement within the agreement

Implement a representative vertical slice in the target app. Keep the original materials repository free of app code. Reuse the app's existing components and state conventions. Keep presentation changes separate from authorization, billing, and persistent data semantics unless those changes were requested too.

Continue routine implementation and verification autonomously inside the approved scope. Ask again only when a new product decision or material departure is necessary, stating the changed decision. Do not repeatedly request permission to run local checks or make corrections that fulfill the agreement.

## 5. Inspect the running result and refine

Follow [visual review](VISUAL_REVIEW.md): capture the actual screen, execute the main flow, and record specific discrepancies against the brief. Include representative narrow/wide layouts, content extremes, text scaling, themes, and error/empty/loading states. Static mockups do not prove runtime behavior; screenshots do not prove focus or screen-reader behavior.

Fix the highest-impact discrepancy first and recapture the affected state. Stop when the agreed criteria are met and remaining tradeoffs are explicit. Avoid unlimited cosmetic loops; revisit the direction with the user if it cannot meet the brief within constraints. A missing runtime or visual tool is an unverified area, not an automatic pass.

## Decision examples

| Request | Correct next action |
| --- | --- |
| "Make my app look premium" with no brief | Inspect the app and ask what users should feel or prioritize; wait for the answer. |
| "Use the attached approved design and implement the settings screen" | Verify that the design is accessible and sufficiently specified, reuse approval, and implement the stated scope. |
| "Audit this checkout flow for keyboard accessibility" | The target and priority are supplied; perform the scoped audit and report evidence. |
| "The approved button clips at large text sizes; fix it" | Restore the approved behavior and verify it; ask only if the correction would change the product direction. |
| "Add a full-screen animated shader behind the payment form" | Confirm purpose and constraints, compare a simpler alternative, and agree the readable fallback before implementation. |

These are adaptations of external ideas, not installation of Superpowers. See [research and adaptation decisions](../REFERENCE_RESEARCH.md).
