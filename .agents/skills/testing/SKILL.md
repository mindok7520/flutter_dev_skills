---
name: testing
description: "Use to plan tests from observable risks in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Plan tests from observable risks

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Map agreed requirements and important failure modes to the smallest useful test layers.
2. Separate pure logic, repository contracts, state transitions, widget interaction, integration, accessibility, and visual checks.
3. Include stale responses, repeated input, cancellation, lifecycle cleanup, and platform differences where the feature can fail.
4. Choose representative screenshots only after a baseline has been reviewed; an image comparison is not a usability test.
5. Define deterministic fixtures, needed environments, raw evidence, and explicitly unverified cells.

## References to load for this task

- [TEST_STRATEGY](../../../docs/testing/TEST_STRATEGY.md)
- [GOLDEN_TESTING](../../../docs/testing/GOLDEN_TESTING.md)
- [VISUAL_REVIEW](../../../docs/design/VISUAL_REVIEW.md)
- [Task prompt](../../../prompts/26-test-plan.md)

## Completion contract

Requirement-to-test map, priority, fixture and environment plan, visual criteria, and justified exclusions.
