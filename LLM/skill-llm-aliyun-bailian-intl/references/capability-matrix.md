# Aliyun Bailian International Capability Matrix

Use this file to verify whether a locally selected International model-kind combination supports a requested feature.

Meanings:

- `verified`: confirmed from official Aliyun docs during the `2026-04-24` sync pass
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
| `chat` | `qwen3.6-max-preview` | `verified` | `verified` | `mixed` | `on` | `verified` | `128k` | `all-modes` | `thinking: 0.6; non-thinking: 0.7` | `non-thinking-only` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `stream verified by official Aliyun stream transport doc plus the official text-generation model page; deep-thinking page says qwen3.6 max preview is mixed-thinking and defaults on; qwen API ref documents enable_thinking and thinking_budget for Qwen3.6; structured-output doc scopes Qwen3.6 Max to non-thinking mode; raw reasoning is exposed as reasoning_content when thinking is enabled` |

### Vision

No locally selected International vision capability rows yet.

### Imaging

No locally selected International imaging capability rows yet.

### Music

No locally selected International music capability rows yet.
