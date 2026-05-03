# MiniMax China Mainland Request URLs

Use this file to resolve the final request URL after the connection profile and API surface are selected.

Read `../../_shared/request-url-matrix-schema.md` first.

## Current Matrix

| Request Kind | Model Scope | API Surface | Endpoint Kind | HTTP Method | Base URL | Request Path Template | Request URL Template | Stream Variant | Request URL Status | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `catalog-selected` | `chat-completions` | `official` | `POST` | `{Profile.Base URL}` | `/chat/completions` | `{Profile.Base URL}/chat/completions` | `body-param` | `verified` | `2026-05-03` | `https://platform.minimaxi.com/docs/api-reference/text-chat-openai` | `China Mainland OpenAI-compatible chat path; template profile base URL is https://api.minimaxi.com/v1` |
| `vision` | `catalog-selected` | `chat-completions` | `official` | `POST` | `{Profile.Base URL}` | `unknown` | `unknown` | `n/a` | `unknown` | `unverified` | `no selected MiniMax China Mainland vision rows` | `keep blocked until a vision model sync verifies the exact model and endpoint behavior` |
| `imaging` | `image-01` | `image-generation` | `official` | `POST` | `{Profile.Base URL}` | `/image_generation` | `{Profile.Base URL}/image_generation` | `n/a` | `verified` | `2026-05-03` | `https://platform.minimaxi.com/docs/api-reference/image-generation-t2i` | `build profile only; plan profile must block this request kind` |
| `music` | `music-2.6` | `music-generation` | `official` | `POST` | `{Profile.Base URL}` | `/music_generation` | `{Profile.Base URL}/music_generation` | `n/a` | `verified` | `2026-05-03` | `https://platform.minimaxi.com/docs/api-reference/music-generation` | `build profile only; plan profile must block this request kind` |

## Build-Only Video Reference

MiniMax China Mainland build-profile HTTP video generation is documented at `https://platform.minimaxi.com/docs/guides/video-generation` and uses `POST {Profile.Base URL}/video_generation`.

Do not add this as a current matrix row because `../../_shared/request-url-matrix-schema.md` only allows `chat`, `vision`, `imaging`, and `music`. Stop before first-class video implementation unless the owner extends the shared schemas.

## Rules

- Use only China Mainland base URLs in this skill.
- Do not fall back to `https://api.minimax.io`.
- Do not route through MiniMax Anthropic-compatible endpoints unless a separate explicit surface is added.
- Resolve the profile first so `{Profile.Base URL}` matches the selected endpoint kind.
- Do not put API keys in request URL templates.
- Enforce profile restrictions after resolving the row: `plan` allows only `chat`; `build` allows `chat`, `imaging`, and `music`.
