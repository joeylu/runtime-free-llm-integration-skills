# Aliyun Bailian China Mainland Model Catalog

Use this file as the local Aliyun Bailian China Mainland model catalog for direct-model work.

Selection context for the current local catalog:

- sync date: `2026-05-01`
- recency boundary: `6 months`
- recency cutoff date: `2025-11-01`
- only rows with `Catalog Status = active` and `Selection Status = selected` are valid local options
- price region: `china-mainland`

International rows are owned by `../skill-llm-aliyun-bailian-intl` and must not be used by this skill.

## Dropdown Rule

When building a model selector:

- display `API Model`
- submit `API Model`
- keep `UI Label` equal to `API Model` if the column is present
- filter out rows whose `Catalog Status` is not `active`
- filter out rows whose `Selection Status` is not `selected`

## Pricing Rule

Use `pricing-matrix.md` for billing region, currency, context band, metered side, and unit price.

The catalog price columns are compatibility summaries only. Do not parse `Input Price`, `Output Price`, or `Pricing Note` to reconstruct tiered billing.

## Active Chat Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.6-plus` | `Qwen36Plus` | `qwen3.6-plus` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-02` | `2025-11-01` | `1000000` | `thinking: 983616; non-thinking: 991808` | `65536` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 2; 256K<Token<=1M: 8` | `0<Token<=256K: 12; 256K<Token<=1M: 48` | `batch is not supported on the current text-generation page; pricing is tiered by input range` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; spec: https://help.aliyun.com/zh/model-studio/models ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `chat` | `qwen3.6-flash` | `Qwen36Flash` | `qwen3.6-flash` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-16` | `2025-11-01` | `1000000` | `unknown` | `65536` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 1.2; 256K<Token<=1M: 4.8` | `0<Token<=256K: 7.2; 256K<Token<=1M: 28.8` | `batch is supported; pricing is tiered by input range` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `chat` | `glm-5.1` | `GLM51` | `glm-5.1` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-14` | `2025-11-01` | `202752` | `unknown` | `131072` | `china-mainland` | `per-million-tokens` | `0<Token<=32K: 6; 32K<Token<=200K: 8` | `0<Token<=32K: 24; 32K<Token<=200K: 28` | `pricing is tiered by input range` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `chat` | `kimi-k2.6` | `KimiK26` | `kimi-k2.6` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-21` | `2025-11-01` | `262144` | `unknown` | `98304` | `china-mainland` | `per-million-tokens` | `unknown` | `unknown` | `official Kimi help-center docs confirm capability and region, but point pricing to the Bailian console instead of publishing a help-center price row as of 2026-04-24` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model ; Kimi API: https://help.aliyun.com/zh/model-studio/kimi-api` |

## Active Vision Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vision` | `qwen3.6-plus` | `Qwen36Plus` | `qwen3.6-plus` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-02` | `2025-11-01` | `1000000` | `thinking: 983616; non-thinking: 991808` | `65536` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 2; 256K<Token<=1M: 8` | `0<Token<=256K: 12; 256K<Token<=1M: 48` | `vision requests consume model token pricing; pricing is tiered by input range` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; spec: https://help.aliyun.com/zh/model-studio/models ; capability: https://help.aliyun.com/zh/model-studio/vision-model` |
| `vision` | `qwen3.6-flash` | `Qwen36Flash` | `qwen3.6-flash` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-16` | `2025-11-01` | `1000000` | `unknown` | `65536` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 1.2; 256K<Token<=1M: 4.8` | `0<Token<=256K: 7.2; 256K<Token<=1M: 28.8` | `vision requests consume model token pricing; pricing is tiered by input range` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing ; capability: https://help.aliyun.com/zh/model-studio/vision-model ; text limits: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `vision` | `kimi-k2.6` | `KimiK26` | `kimi-k2.6` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-21` | `2025-11-01` | `262144` | `unknown` | `98304` | `china-mainland` | `per-million-tokens` | `unknown` | `unknown` | `official help-center docs confirm multimodal support but send pricing to the Bailian console instead of exposing a help-center price row as of 2026-04-24` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; capability: https://help.aliyun.com/zh/model-studio/kimi-api ; text limits: https://help.aliyun.com/zh/model-studio/text-generation-model` |

## Active Imaging Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `z-image-turbo` | `ZImageTurbo` | `z-image-turbo` | `active` | `selected` | `yes` | `verified` | `candidate` | `2025-12-22` | `2025-11-01` | `n/a` | `n/a` | `n/a` | `china-mainland` | `per-image` | `n/a` | `prompt_extend=false: 0.1; prompt_extend=true: 0.2` | `prompt rewriting changes output price` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/image-generation/` |
| `imaging` | `qwen-image-2.0` | `QwenImage20` | `qwen-image-2.0` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-03-03` | `2025-11-01` | `n/a` | `n/a` | `n/a` | `china-mainland` | `per-image` | `n/a` | `0.2` | `image generation and edit model; output-only billing` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/qwen-image-api` |
| `imaging` | `qwen-image-2.0-pro` | `QwenImage20Pro` | `qwen-image-2.0-pro` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-03-03` | `2025-11-01` | `n/a` | `n/a` | `n/a` | `china-mainland` | `per-image` | `n/a` | `0.5` | `image generation and edit model; output-only billing` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/qwen-image-api` |
| `imaging` | `wan2.7-image-pro` | `Wan27ImagePro` | `wan2.7-image-pro` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-01` | `2025-11-01` | `n/a` | `n/a` | `n/a` | `china-mainland` | `per-image` | `n/a` | `0.5` | `output-only billing` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing` |
| `imaging` | `wan2.7-image` | `Wan27Image` | `wan2.7-image` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-01` | `2025-11-01` | `n/a` | `n/a` | `n/a` | `china-mainland` | `per-image` | `n/a` | `0.2` | `output-only billing` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing` |

## Active Music Models

No locally selected music rows yet.
