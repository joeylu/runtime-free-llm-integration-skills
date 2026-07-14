# Gemini Model Catalog

Models with maintained runtime rules in this provider skill.

Region: Gemini Developer API global service.

| Model Type | Operation | Input Modalities | Output Modalities | Flow Kind | API Model | Status | Identifier Kind | Resolves To | Effective From | Deprecates At | Retires At | Replacement Model | Region Scope | Context Window Tokens | Max Input Tokens | Max Output Tokens | Notes | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `text-generation` | `text` | `text` | `chat` | `gemini-3.5-flash` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `text, image, video, audio, and PDF input; text output` | `2026-07-14` | `https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash` |
| `vision` | `multimodal-understanding` | `text,image,video,audio,pdf` | `text` | `vision` | `gemini-3.5-flash` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `image-understanding rules are maintained in this skill` | `2026-07-14` | `https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash` |
| `chat` | `text-generation` | `text` | `text` | `chat` | `gemini-3.1-pro-preview` | `preview` | `preview-id` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `higher-quality preview model` | `2026-07-14` | `https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview` |
| `vision` | `multimodal-understanding` | `text,image,video,audio,pdf` | `text` | `vision` | `gemini-3.1-pro-preview` | `preview` | `preview-id` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1048576` | `1048576` | `65536` | `multimodal preview model` | `2026-07-14` | `https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview` |
| `imaging` | `image-generation` | `text,image` | `image` | `text-to-image,image-edit` | `gemini-3.1-flash-image` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `131072` | `131072` | `32768` | `image generation and editing` | `2026-07-14` | `https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image` |
| `imaging` | `image-generation` | `text,image` | `image` | `text-to-image,image-edit` | `gemini-3-pro-image` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `65536` | `65536` | `32768` | `higher-quality image generation and editing` | `2026-07-14` | `https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image` |

## Usage

Match the exact `API Model`, then read `capability-matrix.md` and the corresponding transport. Model maintenance follows `../../_shared/sync-policy.md`.
