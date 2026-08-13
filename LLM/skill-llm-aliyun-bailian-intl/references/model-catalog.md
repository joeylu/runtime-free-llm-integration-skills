# Aliyun Bailian International Model Catalog

Singapore International deployment only.

| Model Type | Operation | Input Modalities | Output Modalities | Flow Kind | API Model | Status | Identifier Kind | Resolves To | Effective From | Deprecates At | Retires At | Replacement Model | Region Scope | Context Window Tokens | Max Input Tokens | Max Output Tokens | Notes | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `text-generation` | `text` | `text` | `chat` | `qwen3.8-max` | `active` | `opaque-provider-id` | `n/a` | `2026-08-03` | `unknown` | `unknown` | `n/a` | `international-singapore` | `1000000` | `983616` | `131072` | `Conservative max input uses thinking-mode limit; non-thinking max is 991808; max reasoning chain 262144.` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/qwen3-8-max` |
| `vision` | `multimodal-understanding` | `text,image,video` | `text` | `vision` | `qwen3.8-max` | `active` | `opaque-provider-id` | `n/a` | `2026-08-03` | `unknown` | `unknown` | `n/a` | `international-singapore` | `1000000` | `983616` | `131072` | `Native image and video understanding; Responses maintained for image input only.` | 2026-08-06 | `https://help.aliyun.com/zh/model-studio/qwen3-8-max` |

## Resolution Rule

Only `qwen3.8-max` is maintained in this skill.
