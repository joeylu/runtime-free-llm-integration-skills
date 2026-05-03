# MiniMax China Mainland Capability Matrix

Use this file to verify whether a locally selected China Mainland model-kind combination supports a requested feature.

Meanings:

- `verified`: confirmed from official MiniMax China Mainland docs during the `2026-05-03` add-provider pass
- `unsupported`: explicitly listed as unsupported in the official docs
- `unknown`: not yet verified, so risky features must stop
- `n/a`: not applicable to that request kind

## Fail-Fast Rule

If a requested option is `unknown` or `unsupported`, stop before implementation.

Only locally selected active rows from `model-catalog.md` are tracked here.

## Current Matrix

### Chat

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `MiniMax-M2.7` | `verified` | `verified` | `always-on` | `on` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `OpenAI-compatible docs verify non-stream and stream through the stream parameter; API overview and response examples expose M2.7 thinking output in content using think tags; OpenAI-compatible docs list temperature default 1; no disable-thinking, reasoning-effort, JSON, or tool/function schema support was selected in this pass` |
| `chat` | `MiniMax-M2.7-highspeed` | `verified` | `verified` | `always-on` | `on` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `OpenAI-compatible docs verify non-stream and stream through the stream parameter; API overview and response examples expose M2.7 thinking output in content using think tags; OpenAI-compatible docs list temperature default 1; no disable-thinking, reasoning-effort, JSON, or tool/function schema support was selected in this pass` |

### Vision

No locally selected MiniMax China Mainland vision capability rows yet.

### Imaging

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `image-01` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `verified` | `unknown` | `verified` | `n/a` | `Official text-to-image docs verify POST /v1/image_generation with model image-01, prompt, seed, and n. Use ProviderOptions.aspect_ratio and ProviderOptions.prompt_optimizer only when explicitly requested; do not map Inputs.ImageSize to aspect_ratio without owner approval.` |

### Music

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `music` | `music-2.6` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `n/a` | `n/a` | `unknown` | `Official Music Generation docs verify POST /v1/music_generation with model music-2.6, prompt, lyrics, and audio_setting. This skill requires Inputs.Lyrics for music-2.6; do not enable stream, duration, or seed unless a later sync verifies them.` |
