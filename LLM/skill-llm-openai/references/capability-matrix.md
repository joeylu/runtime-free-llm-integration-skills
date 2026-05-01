# OpenAI Capability Matrix

Use this file to verify whether a locally selected model-kind combination supports a requested feature.

Meanings:

- `verified`: confirmed from official OpenAI docs during the `2026-04-30` initial pass
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
| `chat` | `gpt-5.5` | `verified` | `verified` | `mixed` | `medium` | `n/a` | `n/a` | `all-modes` | `all-modes: 1.0` | `all-modes` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `none,low,medium,high,xhigh` | `verified` | `summary` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `official latest-model guide says gpt-5.5 defaults to medium reasoning effort and supports reasoning.effort; Responses API documents stream, temperature, text.format json_object/json_schema, tools, tool_choice, reasoning.summary, and parallel_tool_calls; function-calling docs verify strict mode` |
| `chat` | `gpt-5.4` | `verified` | `verified` | `mixed` | `none` | `n/a` | `n/a` | `all-modes` | `all-modes: 1.0` | `all-modes` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `none,low,medium,high,xhigh` | `verified` | `summary` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `model page lists reasoning.effort values none through xhigh and says none is default; Responses API documents stream, temperature, text.format json_object/json_schema, tools, tool_choice, reasoning.summary, and parallel_tool_calls; function-calling docs verify strict mode` |
| `chat` | `gpt-5.4-mini` | `verified` | `verified` | `unknown` | `unknown` | `n/a` | `n/a` | `all-modes` | `all-modes: 1.0` | `all-modes` | `all-modes` | `all-modes` | `verified` | `verified` | `unknown` | `unknown` | `verified` | `summary` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `model page verifies reasoning token support, streaming, function calling, structured outputs, and Responses; this pass did not find an explicit effort-value list for gpt-5.4-mini, so controllable thinking remains unknown` |

### Vision

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vision` | `gpt-5.5` | `verified` | `verified` | `mixed` | `medium` | `n/a` | `n/a` | `all-modes` | `all-modes: 1.0` | `all-modes` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `none,low,medium,high,xhigh` | `verified` | `summary` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `official models page says all latest OpenAI models support text and image input; latest-model guide says gpt-5.5 preserves more visual detail by default; Responses API capabilities are the same as chat for stream, structured outputs, tools, and reasoning` |
| `vision` | `gpt-5.4` | `verified` | `verified` | `mixed` | `none` | `n/a` | `n/a` | `all-modes` | `all-modes: 1.0` | `all-modes` | `all-modes` | `all-modes` | `verified` | `verified` | `verified` | `none,low,medium,high,xhigh` | `verified` | `summary` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `model page verifies text and image input, reasoning.effort values none through xhigh, streaming, function calling, and structured outputs; Responses API capabilities are the same as chat` |
| `vision` | `gpt-5.4-mini` | `verified` | `verified` | `unknown` | `unknown` | `n/a` | `n/a` | `all-modes` | `all-modes: 1.0` | `all-modes` | `all-modes` | `all-modes` | `verified` | `verified` | `unknown` | `unknown` | `verified` | `summary` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `model page verifies text and image input, reasoning token support, streaming, function calling, structured outputs, and Responses; this pass did not find an explicit effort-value list for gpt-5.4-mini, so controllable thinking remains unknown` |

### Imaging

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `gpt-image-2` | `verified` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `verified` | `unknown` | `verified` | `verified` | `n/a` | `image-generation docs verify the Image API path; docs verify stream with partial_images, edits with one or more image inputs, n for multiple images, and size options; seed was not verified; Responses image-generation hosted tool is not modeled as a selected local imaging path yet` |

### Music

No locally selected music capability rows yet.
