# Screen specification template

Use after the [design brief](PRODUCT_DESIGN_BRIEF.md) establishes the product direction. A specification describes expected behavior; it does not claim implementation or test success.

| Field | Required decision |
| --- | --- |
| User task | What the person needs to accomplish and how they reach this screen. |
| Primary information | What must be understood first, what can be deferred, and why. |
| Actions | Exact visible labels, enabled conditions, side effects, pending behavior, and completion feedback. |
| Navigation | Entry/exit, back behavior, deep link or restoration needs, unsaved input handling. |
| Content | Realistic localized copy, examples, lengths, imagery, and attribution. |
| Layout | Reading order, alignment, spacing roles, width constraints, keyboard insets, and adaptive changes. |
| State owner | The local state, shared/domain state, requests, and object lifetimes. |
| Accessibility | Semantic names/roles/values, traversal, focus restoration, scalable text, target sizes, contrast. |
| Motion | Trigger, purpose, interruption, reduced-motion equivalent, and whether motion is necessary. |
| Evidence | Approved reference, actual captures, functional checks, and unverified targets. |

## State and interaction table

Fill one row for every applicable state: initial, loading, success, empty, refreshing, offline, validation error, request failure, permission denied, disabled, and destructive confirmation. For each state record visible content, allowed actions, screen-reader announcement when needed, retained data, retry/cancel behavior, and the transition that leaves it. Mark inapplicable states with a reason instead of inventing flows.

## Component inventory

List existing components to reuse and the smallest justified additions. Define labels, data inputs, callbacks, focus ownership, and state variants. Keep analytics, payment authorization, and network calls outside visual components. Document changed shared components so other screens can be checked.

## Acceptance walkthrough

Describe the shortest realistic successful flow and the relevant failure path. Include one content extreme and one accessibility/adaptive scenario. Associate each criterion with a behavioral test, manual interaction, or image comparison; a test category is not evidence that it ran.
