# Image and asset efficiency

Preserve intended visual quality while controlling transfer, decode, allocation, and repaint costs.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Measure compressed size, decoded dimensions, cache behavior, and visible display size separately.
- Request/decode an appropriate resolution for the actual display and pixel density instead of decoding every image at source resolution.
- Use suitable formats and responsive assets for the target; verify transparency, color, animation, and decoder support rather than assuming one format is always best.
- Provide meaningful loading and failure presentation. Preserve aspect ratio or layout space to avoid disruptive jumps.
- Bound prefetching and caches; avoid downloading every asset before the first useful screen.

## Procedure

1. Inventory dominant assets by transfer and decoded memory cost.
2. Compare candidate sizes/formats in the actual rendered screen, including high density and dark mode.
3. Measure load/decode and scroll behavior with representative network and cache states.
4. Check accessibility descriptions, attribution, and failure states.

## Required evidence

- [ ] The visible result retains the agreed quality at representative sizes.
- [ ] Memory and network changes are measured separately.
- [ ] Slow or missing assets do not block the main task unnecessarily.

## Tradeoffs and failure handling

Compression can damage text, gradients, and fine detail. Inspect the asset in context, and avoid claiming resource savings from file size alone.

## Sources and related work

[Flutter performance guidance](https://docs.flutter.dev/perf/best-practices) and [DevTools](https://docs.flutter.dev/tools/devtools/performance). [Visual review](../design/VISUAL_REVIEW.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
