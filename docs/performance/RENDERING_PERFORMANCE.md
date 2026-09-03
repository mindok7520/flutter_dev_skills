# Rendering bottlenecks and frame delivery

Locate frame delays in the actual rendering pipeline and correct the relevant work.

Apply this guidance in the target Flutter app. Inspect its actual SDK, dependencies, and existing implementation first. These are project defaults and decision criteria, not claims that checks have already passed. Follow the [shared contract](../agent/PROMPT_CONTRACT.md).

## Decisions and rules

- Inspect build/layout/paint and raster/compositing evidence separately. Do not attribute every slow frame to widget rebuilds.
- Check intrinsic layout, large unbounded content, repeated image decoding, expensive painting, offscreen layers, clips, opacity, and backdrop effects when traces implicate them.
- Use lazy list/grid construction for large or unbounded content and stable identity where reordering/state retention matters.
- Add RepaintBoundary only to isolate an independently changing expensive paint region when measurement supports it. It can increase layer and memory cost.
- Limit the affected area and sampling cost of filters/shaders, and verify custom effects on each required renderer.
- Treat a smooth screenshot as no evidence of smooth motion; capture actual frame timings.

## Procedure

1. Reproduce the slow interaction with realistic data on representative hardware.
2. Inspect slow frames and isolate build, layout, paint, raster, shader, or I/O contributions.
3. Test a focused correction and repeat the same scene, including first-use and sustained animation where relevant.
4. Verify visual fidelity, hit-testing, accessibility, and memory after the change.

## Required evidence

- [ ] The report identifies which pipeline stage was slow and why the change affects it.
- [ ] Frame distribution and resource costs are compared under the same conditions.
- [ ] No visual behavior, state update, or interaction was suppressed merely to lower timing.

## Tradeoffs and failure handling

Caching layers and reducing effect complexity can improve rendering but trade memory or appearance. Discuss those tradeoffs against the approved design instead of silently changing it.

## Sources and related work

[Flutter performance guidance](https://docs.flutter.dev/perf/best-practices) and [DevTools](https://docs.flutter.dev/tools/devtools/performance). [Shader guide](SHADER_GUIDE.md) and [motion](../design/ANIMATION_MOTION.md).

See [reference research](../REFERENCE_RESEARCH.md) for checked dates, repository revisions, and deliberate adaptations. A newer reference does not authorize a dependency upgrade.
