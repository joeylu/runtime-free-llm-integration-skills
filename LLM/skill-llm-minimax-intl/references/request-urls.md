# MiniMax International Request URLs

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Key: `Request Kind + Model Scope + API Surface + API Version + Endpoint Kind`

Read `../../_shared/request-url-matrix-schema.md` first. Resolve a connection profile before substituting `{Profile.Base URL}`. No row authorizes silent surface or version fallback.

## Current Matrix

| Request Kind | Model Scope | API Surface | API Version | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `all-reviewed` | `chat-completions` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-07-14` | `evset-minimax-intl-request-urls-text-chat-all-reviewed-chat-completions-v1-1ee355b3f0` | `International OpenAI-compatible chat path; template profile base URL is https://api.minimax.io/v1` |
| `multimodal-chat` | `all-reviewed` | `chat-completions` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `evset-minimax-intl-request-urls-multimodal-chat-all-reviewed-chat-completions-v1-fd66241325` | `keep blocked until a vision model sync verifies the exact model and endpoint behavior` |
| `image-generation` | `image-01` | `image-generation` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/image_generation` | `{Profile.Base URL}/image_generation` | `n/a` | `verified` | `2026-07-14` | `evset-minimax-intl-request-urls-image-generation-image-01-image-generation-v1-dded324bbe` | `build profile only; plan profile must block this request kind` |
| `music-generation` | `music-2.6` | `music-generation` | `v1` | `official` | `POST` | `{Profile.Base URL}` | `/music_generation` | `{Profile.Base URL}/music_generation` | `n/a` | `verified` | `2026-07-14` | `evset-minimax-intl-request-urls-music-generation-music-2-6-music-generation-v1-b413c3a57a` | `build profile only; plan profile must block this request kind` |

## Rules

- Use only `verified` rows for sending.
- Treat `unknown` paths as hard stops.
- Do not put secrets or signed user data in a logged resolved URL.
- Claim details and official source locators are in `../../_evidence/evidence.json`.
