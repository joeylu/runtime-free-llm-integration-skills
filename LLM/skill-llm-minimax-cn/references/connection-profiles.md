# MiniMax China Mainland Connection Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Request Kinds | API Surfaces | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `minimax-cn-openai` | `MiniMax China Mainland OpenAI-compatible` | `minimax-cn` | `runtime` | `verified` | `openai-compatible` | `https://api.minimaxi.com/v1` | `MINIMAX_CN_API_KEY` | `env` | `chat,vision` | `chat-completions` | `MiniMax-M3 only.` | 2026-08-06 | `Authorization: Bearer; do not reuse Anthropic header shape.` |
| `minimax-cn-anthropic` | `MiniMax China Mainland Anthropic-compatible` | `minimax-cn` | `runtime` | `verified` | `provider-compatible` | `https://api.minimaxi.com/anthropic` | `MINIMAX_CN_API_KEY` | `env` | `chat,vision` | `anthropic-messages` | `MiniMax-M3 only; defaults differ from OpenAI compatibility.` | 2026-08-06 | `Use X-Api-Key/SDK-compatible authentication contract.` |
| `minimax-cn-native` | `MiniMax China Mainland native media` | `minimax-cn` | `runtime` | `verified` | `provider-compatible` | `https://api.minimaxi.com/v1` | `MINIMAX_CN_API_KEY` | `env` | `imaging,music` | `image-generation,music-generation` | `image-01 and music-3.0 only.` | 2026-08-06 | `Authorization: Bearer; native payloads.` |
