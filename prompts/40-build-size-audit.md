# Audit application and asset size

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [BUILD_SIZE_BUDGET](../docs/performance/BUILD_SIZE_BUDGET.md)
- [IMAGE_ASSET_OPTIMIZATION](../docs/performance/IMAGE_ASSET_OPTIMIZATION.md)

## Procedure

1. Measure the actual target artifact and distinguish download/compressed size, installed size, and runtime decoded memory.
2. Identify dominant code, fonts, images, runtime assets, and optional SDK contributions.
3. Compare removal, deferred loading, resolution/format changes, and simpler assets against functionality and quality.
4. Inspect visual quality at realistic density and themes after asset changes, and exercise load/failure behavior.
5. Record comparable before/after sizes and any compatibility or latency costs.

## Evidence and completion

Artifact and asset contributions, measured reduction, visual evidence, compatibility and runtime tradeoffs.
