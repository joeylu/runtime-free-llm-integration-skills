# DeepSeek Capability Matrix

Use this file to verify whether a locally selected model-kind combination supports a requested feature.

Meanings:

- `verified`: confirmed from official DeepSeek docs during the `2026-05-01` initial pass
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
| `chat` | `deepseek-v4-flash` | `verified` | `verified` | `mixed` | `on` | `unsupported` | `n/a` | `non-thinking-only` | `unknown` | `all-modes` | `unknown` | `all-modes` | `verified` | `unknown` | `verified` | `none,low,medium,high,xhigh,max` | `n/a` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `pricing page lists JSON Output and Tool Calls for V4 Flash; thinking-mode docs say thinking.type defaults enabled, reasoning_effort supports high/max with compatibility mappings low/medium->high and xhigh->max, and reasoning_content is returned; strict function calling is beta-surface only` |
| `chat` | `deepseek-v4-pro` | `verified` | `verified` | `mixed` | `on` | `unsupported` | `n/a` | `non-thinking-only` | `unknown` | `all-modes` | `unknown` | `all-modes` | `verified` | `unknown` | `verified` | `none,low,medium,high,xhigh,max` | `n/a` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `pricing page lists JSON Output and Tool Calls for V4 Pro; thinking-mode docs say thinking.type defaults enabled, reasoning_effort supports high/max with compatibility mappings low/medium->high and xhigh->max, and reasoning_content is returned; strict function calling is beta-surface only` |

### Vision

No locally selected DeepSeek vision capability rows yet.

### Imaging

No locally selected DeepSeek imaging capability rows yet.

### Music

No locally selected DeepSeek music capability rows yet.
