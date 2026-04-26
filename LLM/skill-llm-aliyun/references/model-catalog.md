# Aliyun Model Catalog

Use this file as the local Aliyun model catalog for direct-model work.

Selection context for the current local catalog:

- sync date: `2026-04-24`
- recency boundary: `6 months`
- recency cutoff date: `2025-10-24`
- only rows with `Catalog Status = active` and `Selection Status = selected` are valid local options

Meanings:

- `Catalog Status`: local availability flag used by this skill
- `Selection Status`: whether the row was chosen into the local model set
- `Recency Classification`: whether the row is inside the last confirmed sync boundary

## Dropdown Rule

When building a model selector:

- display `UI Label`
- submit `API Model`
- filter out rows whose `Catalog Status` is not `active`
- filter out rows whose `Selection Status` is not `selected`

## Active Chat Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.6-max-preview` | `Qwen36MaxPreview` | `Qwen36MaxPreview_default_tiered` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-20` | `2025-10-24` | `international` | `per-million-tokens` | `0<Token<=128K: 9.742; 128K<Token<=256K: 14.988` | `0<Token<=128K: 58.455; 128K<Token<=256K: 89.93` | `official help-center pricing currently exposes the exact qwen3.6-max-preview row under international pricing` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing/ ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `chat` | `qwen3.6-flash` | `Qwen36Flash` | `Qwen36Flash_in1.2rmb_out7.2rmb_tiered` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-16` | `2025-10-24` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 1.2; 256K<Token<=1M: 4.8` | `0<Token<=256K: 7.2; 256K<Token<=1M: 28.8` | `batch is supported; pricing is tiered by input range` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `chat` | `qwen3.6-plus` | `Qwen36Plus` | `Qwen36Plus_in2rmb_out12rmb_tiered` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-02` | `2025-10-24` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 2; 256K<Token<=1M: 8` | `0<Token<=256K: 12; 256K<Token<=1M: 48` | `batch is not supported on the current text-generation page; pricing is tiered by input range` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing/ ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `chat` | `glm-5.1` | `GLM51` | `GLM51_in6rmb_out24rmb_tiered` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-14` | `2025-10-24` | `china-mainland` | `per-million-tokens` | `0<Token<=32K: 6; 32K<Token<=200K: 8` | `0<Token<=32K: 24; 32K<Token<=200K: 28` | `pricing is tiered by input range` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |
| `chat` | `kimi-k2.6` | `KimiK26` | `KimiK26_price_pending` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-21` | `2025-10-24` | `china-mainland` | `per-million-tokens` | `unknown` | `unknown` | `official Kimi help-center docs confirm capability and region, but point pricing to the Bailian console instead of publishing a help-center price row as of 2026-04-24` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; capability: https://help.aliyun.com/zh/model-studio/kimi-api` |

## Active Vision Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vision` | `qwen3.6-plus` | `Qwen36Plus` | `Qwen36Plus_default_in2rmb_out12rmb_tiered` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-02` | `2025-10-24` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 2; 256K<Token<=1M: 8` | `0<Token<=256K: 12; 256K<Token<=1M: 48` | `vision requests consume model token pricing; pricing is tiered by input range` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing/ ; capability: https://help.aliyun.com/zh/model-studio/vision-model` |
| `vision` | `qwen3.6-flash` | `Qwen36Flash` | `Qwen36Flash_in1.2rmb_out7.2rmb_tiered` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-16` | `2025-10-24` | `china-mainland` | `per-million-tokens` | `0<Token<=256K: 1.2; 256K<Token<=1M: 4.8` | `0<Token<=256K: 7.2; 256K<Token<=1M: 28.8` | `vision requests consume model token pricing; pricing is tiered by input range` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing ; capability: https://help.aliyun.com/zh/model-studio/vision-model` |
| `vision` | `kimi-k2.6` | `KimiK26` | `KimiK26_price_pending` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-21` | `2025-10-24` | `china-mainland` | `per-million-tokens` | `unknown` | `unknown` | `official help-center docs confirm multimodal support but send pricing to the Bailian console instead of exposing a help-center price row as of 2026-04-24` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; capability: https://help.aliyun.com/zh/model-studio/kimi-api` |

## Active Imaging Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `z-image-turbo` | `ZImageTurbo` | `ZImageTurbo_default_out0.1rmb_or0.2rmb_per_image` | `active` | `selected` | `yes` | `verified` | `candidate` | `2025-12-22` | `2025-10-24` | `china-mainland` | `per-image` | `n/a` | `prompt_extend=false: 0.1; prompt_extend=true: 0.2` | `prompt rewriting changes output price` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/image-generation/` |
| `imaging` | `qwen-image-2.0` | `QwenImage20` | `QwenImage20_out0.2rmb_per_image` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-03-03` | `2025-10-24` | `china-mainland` | `per-image` | `n/a` | `0.2` | `image generation and edit model; output-only billing` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/qwen-image-api` |
| `imaging` | `qwen-image-2.0-pro` | `QwenImage20Pro` | `QwenImage20Pro_out0.5rmb_per_image` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-03-03` | `2025-10-24` | `china-mainland` | `per-image` | `n/a` | `0.5` | `image generation and edit model; output-only billing` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing-for-model-studio ; capability: https://help.aliyun.com/zh/model-studio/qwen-image-api` |
| `imaging` | `wan2.7-image-pro` | `Wan27ImagePro` | `Wan27ImagePro_out0.5rmb_per_image` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-01` | `2025-10-24` | `china-mainland` | `per-image` | `n/a` | `0.5` | `output-only billing` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing` |
| `imaging` | `wan2.7-image` | `Wan27Image` | `Wan27Image_out0.2rmb_per_image` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-01` | `2025-10-24` | `china-mainland` | `per-image` | `n/a` | `0.2` | `output-only billing` | `2026-04-24` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/model-pricing` |

## Active Music Models

No locally selected music rows yet.

## Candidate Review Notes Not Selected In This Local Pass

These rows were seen during the `2026-04-24` review and were not promoted into the local selected set. This section is a review-note list, not a catalog table, and these rows must not be used by model selectors or request builders.

If any not-selected row needs to become a retained catalog row later, move it into a full schema table with `Catalog Status = deprecated`, `Selection Status = not-selected`, explicit recency fields, price fields, verification state, and source.

| Model Type | API Model | Reason |
| --- | --- | --- |
| `chat` | `qwen3.5-plus-2026-04-20` | `candidate-not-selected` |
| `chat` | `qwen3.6-27b` | `candidate-not-selected` |
| `chat` | `qwen3.5-plus` | `candidate-not-selected` |
| `chat` | `qwen3.5-flash` | `candidate-not-selected` |
| `chat` | `qwen3.5-122b-a10b` | `candidate-not-selected` |
| `chat` | `qwen3.5-27b` | `candidate-not-selected` |
| `chat` | `qwen3.5-35b-a3b` | `candidate-not-selected` |
| `chat` | `glm-5` | `candidate-not-selected` |
| `chat` | `qwen3.5-plus-2026-02-15` | `candidate-not-selected` |
| `chat` | `qwen3.5-397b-a17b` | `candidate-not-selected` |
| `chat` | `qwen3-max-2026-01-23` | `candidate-not-selected` |
| `chat` | `qwen3-next-80b-a3b-thinking` | `candidate-not-selected` |
| `chat` | `qwen3-next-80b-a3b-instruct` | `candidate-not-selected` |
| `chat` | `deepseek-v3.2` | `candidate-not-selected` |
| `chat` | `glm-4.7` | `candidate-not-selected` |
| `chat` | `kimi-k2-thinking` | `candidate-not-selected` |
| `vision` | `qwen3.6-plus-2026-04-02` | `candidate-not-selected` |
| `vision` | `qwen3.6-flash-2026-04-16` | `candidate-not-selected` |
| `vision` | `qwen3.5-plus` | `candidate-not-selected` |
| `vision` | `qwen3.5-flash` | `candidate-not-selected` |
| `vision` | `qwen3-vl-flash-2026-01-22` | `candidate-not-selected` |
| `vision` | `qwen-vl-ocr` | `candidate-not-selected` |
| `vision` | `qwen-vl-ocr-2025-11-20` | `candidate-not-selected` |
| `vision` | `qwen3-vl-plus-2025-12-19` | `candidate-not-selected` |
| `imaging` | `qwen-image-2.0-pro-2026-04-22` | `candidate-not-selected` |
| `imaging` | `qwen-image-2.0-2026-03-03` | `candidate-not-selected` |
| `imaging` | `qwen-image-2.0-pro-2026-03-03` | `candidate-not-selected` |
| `imaging` | `qwen-image-max` | `candidate-not-selected` |
| `imaging` | `qwen-image-max-2025-12-30` | `candidate-not-selected` |
| `imaging` | `qwen-image-edit-plus` | `candidate-not-selected` |
| `imaging` | `qwen-image-edit-plus-2025-10-30` | `candidate-not-selected` |

## Pre-Sync Placeholder Rows Excluded

The old inherited placeholder rows from the pre-sync draft are not treated as official catalog rows in this file. Do not treat the old placeholder names or prices as authoritative anymore.

If a downstream implementation depends on one of those placeholder names, stop and ask for an explicit migration decision instead of silently mapping it to a reviewed model.
