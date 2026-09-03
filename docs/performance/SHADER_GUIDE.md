# Shader selection, implementation, and verification

A fragment shader computes pixel output on the GPU. Use one only for an approved visual purpose or a measured rendering need that a simpler widget, gradient, image, or painter cannot reasonably meet. Follow the [design consultation workflow](../design/DESIGN_WORKFLOW.md) before adding a new visible effect.

## Decide whether a shader is appropriate

Compare a static asset, built-in effect, custom paint, and shader on visual fidelity, affected pixel area, texture samples, animation frequency, target renderer support, memory, power, and maintenance. A shader is not automatically faster. A decorative effect needs a legible static/reduced-motion fallback and must not obscure input or required status information.

Inspect the target SDK, renderer, and package APIs. The official guide checked on 2026-09-03 distinguishes Canvas shader use from `ImageFilter.shader`: the latter is documented as Impeller-only. Do not assume native, web, Skia, Impeller, and third-party runtime paths are interchangeable. Record a supported/unsupported/unverified matrix for the actual product targets.

## Implementation contract

- Declare shader assets through the target app's supported Flutter manifest mechanism; compile and load them through the installed SDK APIs.
- Cache reusable programs at an appropriate owner. Keep mutable shader instances and their uniforms from leaking state across independently rendered widgets.
- Define the complete Dart/GLSL interface: names, types, float slots or supported named accessors, sampler slots, units, coordinate space, ranges, and initialization. Float and sampler indices are separate; vector values occupy multiple float slots when using indexed setters.
- Verify coordinates, device scale, image orientation, transparent pixels, and premultiplied color expectations. Use Flutter's documented coordinate helper where applicable rather than assuming backend-independent behavior from a raw GLSL example.
- Respect API-specific reserved uniforms. Image-filter shaders may receive input texture and size from the engine; do not overwrite those slots as though they were a standalone Canvas shader.
- Limit the painted or filtered area. Avoid unnecessary full-screen offscreen passes, repeated asset loads, allocations on every frame, and continuously ticking invisible content.
- Identify who releases shader instances, images, listeners, and animation controllers using the installed APIs. Handle load/compile/runtime failure with the agreed fallback.

## Procedure and evidence

1. Ask about the visual purpose, important devices, motion preference, and acceptable fallback unless the current approved brief already supplies them.
2. Inspect a small relevant example from the pinned source inventory and verify the API against the target SDK. Do not copy the example's entire application architecture.
3. Specify the uniform/coordinate contract and renderer matrix before implementation.
4. Exercise representative sizes, pixel densities, alpha edges, resize, first use, sustained animation, backgrounding, and disposal.
5. Record UI and raster timing, affected area, texture size, memory, and comparative visual evidence. Test the static/reduced-motion and unsupported-renderer paths too.

Golden tests may help protect stable appearances on a fixed environment, but they do not prove cross-GPU fidelity or runtime frame cost. If the required backend cannot be run, leave that cell unverified and do not label the effect production-ready.

Use [60-shader-review](../../prompts/60-shader-review.md), [rendering performance](RENDERING_PERFORMANCE.md), and [motion guidance](../design/ANIMATION_MOTION.md). Primary references: [Flutter fragment shaders](https://docs.flutter.dev/ui/design/graphics/fragment-shaders), [flutter_shaders utilities](https://github.com/jonahwilliams/flutter_shaders), and [flutter_animate](https://github.com/gskinner/flutter_animate). Exact repository revisions and adaptation decisions are in [reference research](../REFERENCE_RESEARCH.md).
