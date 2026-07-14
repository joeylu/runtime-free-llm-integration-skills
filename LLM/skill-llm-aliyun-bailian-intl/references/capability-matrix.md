# Aliyun Bailian International Capability Matrix

Use this matrix to check the exact `Route Key` before building a request.

- `verified`: confirmed by official provider documentation.
- `unsupported`: explicitly not supported.
- `unknown`: not confirmed; do not guess.
- `n/a`: not applicable.

| Route Key | Model Type | API Model | API Surface | API Version | Endpoint Kind | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Last Verified At | Source | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat::qwen3.7-max::chat-completions::v1::openai-compatible` | `chat` | `qwen3.7-max` | `chat-completions` | `v1` | `openai-compatible` | `verified` | `verified` | `mixed` | `on` | `verified` | `model maximum; exact value not exposed outside the console model card` | `all-modes` | `thinking: 0.6; non-thinking: 0.7` | `unsupported` | `unknown` | `all-modes` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `2026-07-14` | `https://www.alibabacloud.com/help/en/model-studio/text-generation ; https://www.alibabacloud.com/help/en/model-studio/deep-thinking` | `Chat Completions surface: non-stream and stream are verified; qwen3.7-max is mixed-thinking and defaults on; thinking_budget, preserve_thinking, temperature defaults, and raw reasoning_content are documented; structured output is explicitly unsupported; Function Calling is documented; thinking mode does not support forcing a specific tool; the alias resolves to the text-only 2026-05-20 snapshot` |
| `chat::qwen3.7-max::responses::v1::openai-compatible` | `chat` | `qwen3.7-max` | `responses` | `v1` | `openai-compatible` | `verified` | `verified` | `mixed` | `medium` | `unsupported` | `n/a` | `all-modes` | `range: [0,2); default not documented` | `unsupported` | `unsupported` | `all-modes` | `unsupported` | `unsupported` | `verified` | `none,minimal,low,medium,high` | `verified` | `summary` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `2026-07-14` | `https://www.alibabacloud.com/help/en/model-studio/text-generation ; https://www.alibabacloud.com/help/en/model-studio/compatibility-with-openai-responses-api` | `Responses: qwen3.7-max is in the Singapore supported-model list; non-stream and stream, custom functions, tool_choice, temperature, previous_response_id, store, and Session Cache are documented; response_format, strict schemas, and parallel-tool request control are not listed and are blocked; reasoning defaults to medium and is exposed as summary items; code_interpreter requires reasoning enabled for qwen3.7-max` |

## Resolution Rule

Resolve the connection profile, API surface, API version, and endpoint kind first. Do not copy a capability from another model or surface.
