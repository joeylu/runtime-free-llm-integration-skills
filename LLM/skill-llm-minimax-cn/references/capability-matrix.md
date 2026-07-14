# MiniMax China Mainland Capability Matrix

Use this matrix to check the exact `Route Key` before building a request.

- `verified`: confirmed by official provider documentation.
- `unsupported`: explicitly not supported.
- `unknown`: not confirmed; do not guess.
- `n/a`: not applicable.

| Route Key | Model Type | API Model | API Surface | API Version | Endpoint Kind | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat::MiniMax-M3::chat-completions::v1::official` | `chat` | `MiniMax-M3` | `chat-completions` | `v1` | `official` | `verified` | `verified` | `mixed` | `adaptive` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `unknown` | `all-modes` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `2026-07-14` | `https://platform.minimaxi.com/docs/api-reference/text-chat-openai` | `MiniMax-M3 supports adaptive thinking by default, function tools, streaming, and text input; exact strict/parallel/tool-choice semantics remain fail-closed.` |
| `vision::MiniMax-M3::chat-completions::v1::official` | `vision` | `MiniMax-M3` | `chat-completions` | `v1` | `official` | `verified` | `verified` | `mixed` | `adaptive` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `unknown` | `all-modes` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `raw` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `2026-07-14` | `https://platform.minimaxi.com/docs/api-reference/text-chat-openai` | `MiniMax-M3 supports image and video content in messages; this row verifies image input only. Video requires an explicit typed input contract in the host project.` |
| `imaging::image-01::image-generation::v1::official` | `imaging` | `image-01` | `image-generation` | `v1` | `official` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `verified` | `verified` | `verified` | `n/a` | `2026-07-14` | `https://platform.minimaxi.com/docs/api-reference/image-generation-t2i` | `Text-to-image API verifies seed, n=1..9, aspect ratios, and width/height 512..2048 divisible by 8; width and height must be supplied together and aspect_ratio takes precedence.` |
| `music::music-2.6::music-generation::v1::official` | `music` | `music-2.6` | `music-generation` | `v1` | `official` | `verified` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `n/a` | `n/a` | `unknown` | `2026-07-14` | `https://platform.minimaxi.com/docs/api-reference/music-generation` | `Streaming is supported; stream=true requires hex output. Prompt is required for instrumental mode and for optimizer-driven lyric generation when lyrics are empty; otherwise prompt is optional. Lyrics are conditionally optional for instrumental mode or optimizer-driven generation.` |

## Resolution Rule

Resolve the connection profile, API surface, API version, and endpoint kind first. Do not copy a capability from another model or surface.
