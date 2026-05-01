# Gemini Capability Matrix

Use this file to verify whether a locally selected model-kind combination supports a requested feature.

Meanings:

- `verified`: confirmed from official Gemini docs during the `2026-05-01` initial pass
- `unsupported`: explicitly listed as unsupported in the official docs
- `unknown`: not yet verified, so risky features must stop
- `n/a`: not applicable to that request kind

## Fail-Fast Rule

If a requested option is `unknown` or `unsupported`, stop before implementation.

Only the locally selected active rows from `model-catalog.md` are tracked here.

## Current Matrix

### Chat

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `gemini-3-flash-preview` | `verified` | `verified` | `always-on` | `high` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `minimal,low,medium,high` | `verified` | `summary` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `model page verifies function calling, structured outputs, thinking, and text output; text-generation docs verify generateContent and streamGenerateContent; thinking docs say Gemini 3 Flash cannot fully disable thinking, supports minimal/low/medium/high, defaults high, and can return thought summaries; function-calling docs verify schema-adherent modes and parallel function calling` |
| `chat` | `gemini-3.1-pro-preview` | `verified` | `verified` | `always-on` | `high` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `low,medium,high` | `verified` | `summary` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `model page verifies function calling, structured outputs, thinking, and text output; text-generation docs verify generateContent and streamGenerateContent; thinking docs say Gemini 3.1 Pro cannot disable thinking, supports low/medium/high, defaults high, and can return thought summaries; function-calling docs verify schema-adherent modes and parallel function calling` |

### Vision

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vision` | `gemini-3-flash-preview` | `verified` | `verified` | `always-on` | `high` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `minimal,low,medium,high` | `verified` | `summary` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `model page verifies text, image, video, audio, and PDF inputs plus function calling, structured outputs, and thinking; text-generation docs verify image inputs and streaming; multi-image input limit was not verified as a normalized provider limit` |
| `vision` | `gemini-3.1-pro-preview` | `verified` | `verified` | `always-on` | `high` | `unsupported` | `n/a` | `all-modes` | `all-modes: 1.0` | `unknown` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `low,medium,high` | `verified` | `summary` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `model page verifies text, image, video, audio, and PDF inputs plus function calling, structured outputs, and thinking; text-generation docs verify image inputs and streaming; multi-image input limit was not verified as a normalized provider limit` |

### Imaging

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `gemini-3.1-flash-image-preview` | `verified` | `unknown` | `always-on` | `minimal` | `unsupported` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `unsupported` | `n/a` | `n/a` | `verified` | `minimal,high` | `verified` | `summary` | `verified` | `unknown` | `verified` | `unknown` | `n/a` | `model page verifies Nano Banana 2 image generation, image/text inputs, image/text outputs, thinking, search grounding, and no function calling; image-generation docs say Gemini 3 image thinking is enabled by default and cannot be disabled, Gemini 3.1 Flash Image supports thinkingLevel minimal/high with default minimal, reference images, imageConfig.imageSize, and up to 14 reference images; stream and output image count were not verified` |
| `imaging` | `gemini-3-pro-image-preview` | `verified` | `unknown` | `always-on` | `unknown` | `unsupported` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `unsupported` | `n/a` | `n/a` | `unknown` | `unknown` | `verified` | `summary` | `verified` | `unknown` | `verified` | `unknown` | `n/a` | `model page verifies Nano Banana Pro image generation, image/text inputs, image/text outputs, thinking, search grounding, structured outputs, and no function calling; image-generation docs verify Gemini 3 image models use thinking by default, support reference images, and imageConfig.imageSize; exact thinkingLevel values and stream/output image count were not verified for this model` |
| `imaging` | `gemini-2.5-flash-image` | `verified` | `unknown` | `unsupported` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `unsupported` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `none` | `verified` | `unknown` | `verified` | `unknown` | `n/a` | `model page verifies Nano Banana image generation, image/text inputs, image/text outputs, structured outputs, and explicitly says thinking and function calling are not supported; image-generation docs verify image editing/reference image input and aspectRatio, but stream and output image count were not verified` |

### Music

No locally selected music capability rows yet.
