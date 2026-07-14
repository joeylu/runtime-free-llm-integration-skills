# MiniMax International Build Multimodal HTTP

Use this file when the user asks whether MiniMax International build mode can support image, music, or video generation.

## Profile Boundary

Only `ConnectionProfileKey = build` may use the multimodal HTTP entries below.

`ConnectionProfileKey = plan` is chat-only in this skill. Do not route plan-profile multimodal work to HTTP, CLI, MCP, chat, or hidden fallback paths.

## Build HTTP Links

| Capability | Shared RequestKind | API Surface | Build Request URL | Official Source | Current Skill Status |
| --- | --- | --- | --- | --- | --- |
| Image generation | `imaging` | `image-generation` | `https://api.minimax.io/v1/image_generation` | `https://platform.minimax.io/docs/api-reference/image-generation-t2i` | `model `image-01`` |
| Music generation | `music` | `music-generation` | `https://api.minimax.io/v1/music_generation` | `https://platform.minimax.io/docs/api-reference/music-generation` | `model `music-2.6`` |
| Video generation | `none` | `video-generation` | `https://api.minimax.io/v1/video_generation` | `https://platform.minimax.io/docs/guides/video-generation` | `reference-only; shared schema has no video request kind` |

## Video Rule

MiniMax build HTTP video exists, but this skill pack cannot implement it as a first-class request yet because the shared contracts currently define only `chat`, `vision`, `imaging`, and `music`.

If the host project requests MiniMax video generation, stop and ask the owner to approve a shared schema extension before writing implementation code.

## Do Not Infer

Do not infer video request/response shape from imaging or music. Do not send video through `RequestKind = imaging`, `RequestKind = music`, or `RequestKind = chat`.
