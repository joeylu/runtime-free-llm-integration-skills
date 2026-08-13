---
name: skill-llm-aliyun-bailian-cn
description: Runtime contract for Aliyun Bailian China Mainland direct-model integration. Use it to resolve exact retained model IDs, workspace endpoints, API surfaces, per-model parameters, thinking, tools, structured output, multimodal input, image generation/editing, streaming, response mapping, pricing, and logging. It defines request construction only and never executes the request.
---

# Skill LLM Aliyun Bailian China Mainland

## Purpose

Build a validated China Mainland Aliyun Bailian request for a model already selected by the user or host project. This skill is an integration contract, not a model selector and not an execution layer.

## Read Order

Read shared contracts first:

1. `../_shared/route-key-schema.md`
2. `../_shared/model-catalog-schema.md`
3. `../_shared/pricing-matrix-schema.md`
4. `../_shared/capability-matrix-schema.md`
5. `../_shared/connection-profile-schema.md`
6. `../_shared/request-url-matrix-schema.md`
7. `../_shared/request-envelope.md`
8. `../_shared/response-envelope.md`
9. `../_shared/error-contract.md`
10. `../_shared/progress-contract.md`
11. `../_shared/ui-binding.md`
12. `../_shared/sync-policy.md`
13. `../_shared/logging-fields.md`

Then read only what the request needs:

1. `references/connection-profiles.md`
2. `references/workspace-configuration.md`
3. `references/request-urls.md`
4. `references/model-catalog.md`
5. `references/capability-matrix.md`
6. `references/model-parameters.md` for optional fields or feature claims
7. the matching transport
8. `references/pricing-matrix.md` only when cost is relevant
9. `references/logging-contract.md` when logging is implemented
10. `references/model-sync.md` only for an explicit update task

## Runtime Rules

- Provider identifier is `aliyun-bailian-cn`.
- The maintained model allowlist is exactly the catalog in this folder. Do not silently retain, discover, or substitute another model.
- China Mainland and International are separate providers. Never copy an endpoint, price, availability statement, or rate limit across regions.
- Resolve an explicit connection profile and every declared connection input before URL construction. Workspace profiles require `ALIYUN_BAILIAN_CN_WORKSPACE_ID`; shared profiles do not. Never switch profiles implicitly.
- Resolve the full route key before reading capabilities: request kind, exact model ID, API surface, API version, and endpoint kind.
- A generic provider parameter table is not sufficient evidence. A field is usable only when the exact model/surface row or an official example confirms it.
- `unknown` is fail-closed: reject the field and report which official fact is missing. Do not convert documentation silence into `unsupported`.
- `qwen3.8-max` reasoning controls are surface-specific. Chat Completions and DashScope use `reasoning_effort`; Responses uses `reasoning.effort`. Never send both `reasoning_effort` and `thinking_budget`.
- OpenAI-compatible Responses, OpenAI-compatible Chat Completions, and DashScope-native multimodal generation are separate payload contracts.
- Qwen-Image 3.0 and Wan 2.7 are separate image families. Never copy Qwen-Image fields such as `prompt_extend` to Wan, or Wan fields such as `enable_sequential`, `thinking_mode`, `color_palette`, and `bbox_list` to Qwen-Image.
- `qwen-image-3.0` has verified synchronous and asynchronous HTTP routes. For `qwen-image-3.0-pro`, synchronous use is verified but asynchronous availability is `unknown` because Alibaba Cloud's model-specific API reference and error-code reference conflict; reject the Pro async route until the provider resolves the contradiction.
- For a workspace-specific direct-model profile, the workspace ID is encoded in the hostname; a shared profile has no workspace placeholder. Do not add `X-DashScope-WorkSpace` to these routes unless a separate application-API contract explicitly requires it.
- Preserve required reasoning/tool-call history exactly. Never expose raw hidden reasoning to the user.
- Reject fields marked `unsupported` or `unknown`; do not silently drop or rename them.

## Request Flow

1. Accept the exact requested model and operation.
2. Resolve the regional profile and request URL.
3. Resolve the exact catalog and capability row.
4. Validate every requested field against `references/model-parameters.md`.
5. Apply the matching transport without cross-surface translation.
6. Normalize response, errors, progress, and logs through shared contracts.

## Request Kinds

- `chat`: text-first generation or agent turns
- `vision`: image or video understanding
- `imaging`: image generation or editing

## Out of Scope

- International Aliyun endpoints
- Agent App orchestration
- model ranking or automatic replacement
- request execution
- unlisted models
