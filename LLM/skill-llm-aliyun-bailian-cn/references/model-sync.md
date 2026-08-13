# Model Sync

Last verified: `2026-08-13`.

Maintained allowlist: `qwen3.8-max`, `qwen3.7-plus`, `qwen-image-3.0`, `qwen-image-3.0-pro`, `wan2.7-image`, `wan2.7-image-pro`.

## Rule

Verify exact model ID, region, model page, connection profile, every Base URL placeholder and its configuration source, API-Key/workspace binding, API surface, request example, capability flags, limits, pricing, and transport together. Generic parameter pages do not override model-specific evidence. Preserve `unknown` when exact evidence is absent.

When official references conflict on an exact model/surface, record the conflict as `unknown` and fail closed instead of choosing one source.
