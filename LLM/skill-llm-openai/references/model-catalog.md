# OpenAI Model Catalog

Models with maintained runtime rules in this provider skill.

Region: global.

| Model Type | Operation | Input Modalities | Output Modalities | Flow Kind | API Model | Status | Identifier Kind | Resolves To | Effective From | Deprecates At | Retires At | Replacement Model | Region Scope | Context Window Tokens | Max Input Tokens | Max Output Tokens | Notes | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `text-generation` | `text` | `text` | `chat` | `gpt-5.6-sol` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1050000` | `unknown` | `128000` | `frontier professional-work model` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-sol` |
| `vision` | `multimodal-understanding` | `text,image` | `text` | `vision` | `gpt-5.6-sol` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1050000` | `unknown` | `128000` | `accepts image input on verified surfaces` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-sol` |
| `chat` | `text-generation` | `text` | `text` | `chat` | `gpt-5.6-terra` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1050000` | `unknown` | `128000` | `balanced production model` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-terra` |
| `vision` | `multimodal-understanding` | `text,image` | `text` | `vision` | `gpt-5.6-terra` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1050000` | `unknown` | `128000` | `accepts image input on verified surfaces` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-terra` |
| `chat` | `text-generation` | `text` | `text` | `chat` | `gpt-5.6-luna` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1050000` | `unknown` | `128000` | `cost-sensitive high-volume model` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-luna` |
| `vision` | `multimodal-understanding` | `text,image` | `text` | `vision` | `gpt-5.6-luna` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `1050000` | `unknown` | `128000` | `accepts image input on verified surfaces` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-luna` |
| `imaging` | `image-generation` | `text,image` | `image` | `text-to-image,image-edit` | `gpt-image-2` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `global` | `n/a` | `n/a` | `n/a` | `image generation and editing` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-image-2` |

## Usage

Match the exact `API Model`, then read `capability-matrix.md` and the corresponding transport. Model maintenance follows `../../_shared/sync-policy.md`.
