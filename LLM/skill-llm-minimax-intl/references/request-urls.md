# MiniMax International Request URLs

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat,vision` | `MiniMax-M3` | `chat-completions` | `v1` | `openai-compatible` | `POST` | `https://api.minimax.io/v1` | `/chat/completions` | `https://api.minimax.io/v1/chat/completions` | `body-param` | `verified` | 2026-08-06 | `https://platform.minimax.io/docs/api-reference/text-chat-openai` | `OpenAI-compatible contract.` |
| `chat,vision` | `MiniMax-M3` | `anthropic-messages` | `v1` | `provider-compatible` | `POST` | `https://api.minimax.io/anthropic` | `/v1/messages` | `https://api.minimax.io/anthropic/v1/messages` | `body-param` | `verified` | 2026-08-06 | `https://platform.minimax.io/docs/api-reference/text-anthropic-api` | `Anthropic-compatible contract.` |
| `chat,vision` | `MiniMax-M3` | `anthropic-count-tokens` | `v1` | `provider-compatible` | `POST` | `https://api.minimax.io/anthropic` | `/v1/messages/count_tokens` | `https://api.minimax.io/anthropic/v1/messages/count_tokens` | `n/a` | `verified` | 2026-08-06 | `https://platform.minimax.io/docs/api-reference/text-anthropic-api` | `Token counting only.` |
| `imaging` | `image-01` | `image-generation` | `v1` | `provider-compatible` | `POST` | `https://api.minimax.io/v1` | `/image_generation` | `https://api.minimax.io/v1/image_generation` | `n/a` | `verified` | 2026-08-06 | `https://platform.minimax.io/docs/api-reference/image-generation-t2i ; https://platform.minimax.io/docs/api-reference/image-generation-i2i` | `Native image-generation route; no image-01 streaming contract is asserted.` |
| `music` | `music-3.0` | `music-generation` | `v1` | `provider-compatible` | `POST` | `https://api.minimax.io/v1` | `/music_generation` | `https://api.minimax.io/v1/music_generation` | `body-param` | `verified` | 2026-08-06 | `https://platform.minimax.io/docs/api-reference/music-generation` | `Streaming only with hex output.` |

## Rule

Never change the regional domain or compatibility prefix as fallback.
