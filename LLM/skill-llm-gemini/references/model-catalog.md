# Gemini Model Catalog

Gemini Developer API global service.

| Model Type | Operation | Input Modalities | Output Modalities | Flow Kind | API Model | Status | Identifier Kind | Resolves To | Effective From | Deprecates At | Retires At | Replacement Model | Region Scope | Context Window Tokens | Max Input Tokens | Max Output Tokens | Notes | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `text-generation` | `text` | `text` | `chat` | `gemini-3.6-flash` | `active` | `opaque-provider-id` | `n/a` | `2026-07-21` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `Stable; multimodal inputs are represented by the vision row.` | 2026-08-06 | `https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash` |
| `vision` | `multimodal-understanding` | `text,image,video,audio,pdf` | `text` | `vision` | `gemini-3.6-flash` | `active` | `opaque-provider-id` | `n/a` | `2026-07-21` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `Image, video, audio, and PDF input; text output.` | 2026-08-06 | `https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash` |
| `chat` | `text-generation` | `text` | `text` | `chat` | `gemini-3.1-pro-preview` | `preview` | `preview-id` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `Preview contract; do not treat as stable.` | 2026-08-06 | `https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview` |
| `vision` | `multimodal-understanding` | `text,image,video,audio,pdf` | `text` | `vision` | `gemini-3.1-pro-preview` | `preview` | `preview-id` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `Multimodal preview model.` | 2026-08-06 | `https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview` |
| `imaging` | `image-generation` | `text,image,video,pdf` | `text,image` | `text-to-image,image-edit,video-to-image` | `gemini-3.1-flash-image` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `131072` | `131072` | `32768` | `The model page declares PDF input; the image-generation guide additionally provides an exact video-to-image example. Image generation/editing supports up to 14 references with role-specific limits.` | 2026-08-06 | `https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image ; https://ai.google.dev/gemini-api/docs/image-generation` |
| `imaging` | `image-generation` | `text,image` | `text,image` | `text-to-image,image-edit` | `gemini-3-pro-image` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `65536` | `65536` | `32768` | `Professional image generation/editing; up to 14 references with object, character, and style limits.` | 2026-08-06 | `https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image ; https://ai.google.dev/gemini-api/docs/image-generation` |

## Rule

Use the exact API ID and then resolve the exact surface row. Preview status is not active stability.
