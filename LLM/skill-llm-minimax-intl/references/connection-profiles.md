# MiniMax International Connection Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Request Kinds | API Surfaces | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `minimax-intl-openai` | `MiniMax International OpenAI-compatible` | `minimax-intl` | `runtime` | `verified` | `openai-compatible` | `https://api.minimax.io/v1` | `MINIMAX_INTL_API_KEY` | `env` | `chat,vision` | `chat-completions` | `MiniMax-M3 only.` | 2026-08-06 | `Authorization: Bearer; do not reuse Anthropic header shape.` |
| `minimax-intl-anthropic` | `MiniMax International Anthropic-compatible` | `minimax-intl` | `runtime` | `verified` | `provider-compatible` | `https://api.minimax.io/anthropic` | `MINIMAX_INTL_API_KEY` | `env` | `chat,vision` | `anthropic-messages` | `MiniMax-M3 only; defaults differ from OpenAI compatibility.` | 2026-08-06 | `Use X-Api-Key/SDK-compatible authentication contract.` |
| `minimax-intl-native` | `MiniMax International native media` | `minimax-intl` | `runtime` | `verified` | `provider-compatible` | `https://api.minimax.io/v1` | `MINIMAX_INTL_API_KEY` | `env` | `imaging,music` | `image-generation,music-generation` | `image-01 and music-3.0 only.` | 2026-08-06 | `Authorization: Bearer; native payloads.` |
