# Aliyun Bailian China Mainland Capability Matrix

Use this file to verify whether a locally selected China Mainland model-kind combination supports a requested feature.

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
| `chat` | `qwen3.6-plus` | `verified` | `verified` | `mixed` | `on` | `verified` | `80k` | `all-modes` | `thinking: 0.6; non-thinking: 0.7` | `non-thinking-only` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `stream verified by both the official stream doc and official qwen3.6-plus stream=true examples; deep-thinking page says qwen3.6 plus is mixed-thinking and defaults on; qwen API ref documents enable_thinking and thinking_budget for Qwen3.6; structured-output doc scopes Qwen3.6 Plus to non-thinking mode; raw reasoning is exposed as reasoning_content when thinking is enabled` |
| `chat` | `qwen3.6-flash` | `verified` | `verified` | `mixed` | `on` | `verified` | `128k` | `all-modes` | `thinking: 0.6; non-thinking: 0.7` | `non-thinking-only` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `stream verified by official Aliyun stream transport doc plus the official text-generation model page listing qwen3.6-flash in the same Qwen text family; deep-thinking page says qwen3.6 flash is mixed-thinking and defaults on; qwen API ref documents enable_thinking and thinking_budget for Qwen3.6; structured-output doc scopes Qwen3.6 Flash to non-thinking mode; raw reasoning is exposed as reasoning_content when thinking is enabled` |
| `chat` | `glm-5.1` | `verified` | `verified` | `mixed` | `on` | `unknown` | `128k max listed on text-generation page; request field not documented` | `all-modes` | `all-modes: 1.0` | `non-thinking-only` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `glm page gives explicit stream=true and enable_thinking=true examples; deep-thinking page says glm-5.1 is mixed-thinking and defaults on; glm parameter-default table gives temperature 1.0; glm feature table says structured output is only supported in non-thinking mode` |
| `chat` | `kimi-k2.6` | `verified` | `unknown` | `mixed` | `off` | `unknown` | `80k max listed on text-generation page; request field not documented` | `all-modes` | `thinking: 1.0; non-thinking: 0.6` | `unsupported` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `deep-thinking page and Kimi page say kimi-k2.6 is a mixed-thinking model that defaults off; Kimi parameter-default table gives separate temperature defaults; Kimi feature table says structured output is unsupported; no official kimi-k2.6 stream example was verified in this pass` |

### Vision

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vision` | `qwen3.6-plus` | `verified` | `verified` | `mixed` | `on` | `verified` | `80k` | `all-modes` | `thinking: 0.6; non-thinking: 0.7` | `non-thinking-only` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `raw` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `vision doc gives explicit qwen3.6-plus stream=true, enable_thinking, and thinking_budget=81920 examples; vision doc says qwen3.6 defaults thinking on; model feature table says structured output is supported only in non-thinking mode; vision-model page lists up to 256 input images; raw reasoning is exposed as reasoning_content when thinking is enabled` |
| `vision` | `qwen3.6-flash` | `verified` | `verified` | `mixed` | `on` | `verified` | `128k` | `all-modes` | `thinking: 0.6; non-thinking: 0.7` | `non-thinking-only` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `raw` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `stream verified by the official multimodal stream transport plus the official vision-model page placing qwen3.6-flash in the same Qwen3.6 vision family; vision doc says qwen3.6 defaults thinking on and supports thinking_budget; text-generation model page lists qwen3.6-flash budget 128k; vision feature table says structured output is non-thinking-only; vision-model page lists up to 256 input images; raw reasoning is exposed as reasoning_content when thinking is enabled` |
| `vision` | `kimi-k2.6` | `verified` | `unknown` | `mixed` | `off` | `unknown` | `80k max listed on text-generation page; request field not documented on the Kimi page` | `all-modes` | `thinking: 1.0; non-thinking: 0.6` | `unsupported` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `unknown` | `unknown` | `verified` | `n/a` | `n/a` | `n/a` | `n/a` | `Kimi page says kimi-k2.6 supports text, image, and video input; it documents enable_thinking with default off and includes single-image and multi-image examples; parameter-default table gives separate temperature defaults; feature table says structured output is unsupported; no official stream example for kimi-k2.6 multimodal was verified in this pass` |

### Imaging

| Model Type | API Model | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `z-image-turbo` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `base generation path verified; pricing depends on prompt_extend` |
| `imaging` | `qwen-image-2.0` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `generation and edit model; base path verified` |
| `imaging` | `qwen-image-2.0-pro` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `generation and edit model; base path verified` |
| `imaging` | `wan2.7-image-pro` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `supports generation, grouped generation, edit, and multi-image reference according to the release page; request parameters still need per-field verification` |
| `imaging` | `wan2.7-image` | `verified` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `supports generation, grouped generation, edit, and multi-image reference according to the release page; request parameters still need per-field verification` |

### Music

No locally selected music capability rows yet.
