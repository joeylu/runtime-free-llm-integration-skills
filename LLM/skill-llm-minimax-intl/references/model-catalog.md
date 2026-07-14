# MiniMax International Model Catalog

Models with maintained runtime rules in this provider skill.

Region: International.

| Model Type | Operation | Input Modalities | Output Modalities | Flow Kind | API Model | Status | Identifier Kind | Resolves To | Effective From | Deprecates At | Retires At | Replacement Model | Region Scope | Context Window Tokens | Max Input Tokens | Max Output Tokens | Notes | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `text-generation` | `text` | `text` | `chat` | `MiniMax-M3` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `international` | `1000000` | `unknown` | `524288` | `1M M-series model with adaptive thinking, multimodal messages, and function tools` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` |
| `vision` | `multimodal-understanding` | `text,image,video` | `text` | `vision` | `MiniMax-M3` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `international` | `1000000` | `unknown` | `524288` | `supports image and video input; this skill maintains image-input rules` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` |
| `imaging` | `image-generation` | `text` | `image` | `text-to-image` | `image-01` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `international` | `n/a` | `n/a` | `n/a` | `text-to-image` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/image-generation-t2i` |
| `music` | `music-generation` | `text` | `audio` | `text-to-music` | `music-2.6` | `active` | `opaque-provider-id` | `n/a` | `unknown` | `unknown` | `unknown` | `n/a` | `international` | `n/a` | `n/a` | `n/a` | `music generation; streaming requires hex output` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/music-generation` |

## Usage

Match the exact `API Model`, then read `capability-matrix.md` and the corresponding transport. Model maintenance follows `../../_shared/sync-policy.md`.
