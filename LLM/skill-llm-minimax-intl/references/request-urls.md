# MiniMax International Request URLs

- Key: `Request Kind + Model Scope + API Surface + API Version + Endpoint Kind`

Read `../../_shared/request-url-matrix-schema.md` first. Resolve a connection profile before substituting `{Profile.Base URL}`. Never silently change surface, version, or endpoint.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `documented-models` | `chat-completions` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` | `International OpenAI-compatible chat path; template profile base URL is https://api.minimax.io/v1` |
| `vision` | `MiniMax-M3` | `chat-completions` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` | `MiniMax-M3 image input uses the OpenAI-compatible Chat Completions endpoint` |
| `imaging` | `image-01` | `image-generation` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/image_generation` | `{Profile.Base URL}/image_generation` | `n/a` | `verified` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/image-generation-t2i` | `build profile only; plan profile must block this request kind` |
| `music` | `music-2.6` | `music-generation` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/music_generation` | `{Profile.Base URL}/music_generation` | `n/a` | `verified` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/music-generation` | `build profile only; plan profile must block this request kind` |

## Rules

- Use only `verified` rows for sending.
- Treat `unknown` paths as hard stops.
- Do not put secrets or signed user data in a logged resolved URL.
