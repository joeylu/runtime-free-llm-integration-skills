# MiniMax International Build Multimodal HTTP

Use this reference when the task asks whether the MiniMax `intl` build profile has official image, music, or video HTTP endpoints.

## Profile Boundary

Only `ConnectionProfileKey = build` may use the entries below. `plan` remains `text-chat` only. Do not route a disallowed request through another profile, CLI, MCP, chat surface, or hidden fallback.

## Endpoint Reference

| Capability | Canonical Request Kind | API Surface | Request URL | Official Source | Skill Status |
| --- | --- | --- | --- | --- | --- |
| Image generation | `image-generation` | `image-generation` | `https://api.minimax.io/v1/image_generation` | `https://platform.minimax.io/docs/api-reference/image-generation-t2i` | `selected through image-01` |
| Music generation | `music-generation` | `music-generation` | `https://api.minimax.io/v1/music_generation` | `https://platform.minimax.io/docs/api-reference/music-generation` | `selected through music-2.6` |
| Video generation | `video-generation` | `video-generation` | `https://api.minimax.io/v1/video_generation` | `https://platform.minimax.io/docs/guides/video-generation` | `reference-only; not selected or implemented` |

## Video Gate

The shared schema now defines `video-generation`, but that alone does not implement MiniMax video. This provider skill intentionally has no selected video catalog row, profile route, request-URL row, capability row, pricing row, role row, or transport contract.

A video request therefore fails before construction. Add all required provider rows and reviewed evidence in one explicit extension; do not infer video request or response shape from image or music endpoints.
