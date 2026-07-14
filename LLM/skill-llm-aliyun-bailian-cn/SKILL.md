---
name: skill-llm-aliyun-bailian-cn
description: Runtime contract for Aliyun Bailian China Mainland direct-model integration. Use it to resolve exact model IDs, regional connection profiles, OpenAI-compatible or DashScope-native URLs, thinking, tools, structured output, multimodal input, image generation, streaming, response mapping, pricing references, and logging. Model choice remains with the user or host project.
---

# Skill LLM Aliyun Bailian China Mainland

## Purpose

Define how an agent integrates a China Mainland Aliyun Bailian model already named by the user or host project. Keep China Mainland and International as separate skills because official availability, endpoints, snapshots, prices, and capabilities can differ.

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

Then read:

1. `references/connection-profiles.md`
2. `references/request-urls.md`
3. `references/model-catalog.md`
4. `references/pricing-matrix.md`
5. `references/capability-matrix.md`
6. the transport for the requested kind
7. `references/logging-contract.md` when logging is implemented
8. `references/model-sync.md` only for an explicit update or verification task

## Runtime Rules

- Use provider identifier `aliyun-bailian-cn`.
- Send the exact model ID from this region's `model-catalog.md`.
- Do not copy a model, price, URL, snapshot rule, or capability from the other region unless that region's official documentation verifies it.
- Resolve connection profile, request kind, API surface, API version, endpoint kind, full route key, base URL, and request URL before capability lookup.
- Match capabilities by the exact full `RouteKey` row, including API version and endpoint kind.
- OpenAI-compatible Responses, OpenAI-compatible Chat Completions, and DashScope-native APIs are separate surfaces with separate payloads.
- Do not silently switch region, workspace endpoint, model, snapshot, surface, URL, or credential.
- Apply thinking, reasoning-effort, structured-output, function-calling, image-input, and stream rules from the exact capability row and transport.
- Treat model-owner names such as Qwen, GLM, Kimi, or MiniMax as model facts; the callable provider remains Aliyun Bailian for this skill.
- Reject requested fields marked `unsupported` or `unknown`; do not silently omit them.
- Use `pricing-matrix.md` for the exact regional billing facts. Keep unpublished prices as `unknown`.
- Store API-key references only and redact resolved URLs before logging when they contain sensitive query values.

## Request Flow

1. Read the requested region, model, request kind, and API surface.
2. Resolve the regional connection profile and exact request URL row.
3. Resolve the exact catalog and capability rows.
4. Validate every optional field and regional restriction.
5. Apply the matching transport.
6. Normalize response, errors, progress, and logs through the shared contracts.

## Request Kinds

- `chat`: text-first generation or agent turns
- `vision`: image understanding
- `imaging`: image generation or editing
- `music` (extension target only; no maintained model/verified route): music generation when a documented row exists

## Out of Scope

- the other Aliyun region
- Agent App orchestration
- cross-region availability assumptions
- model ranking or permission policy
- non-Aliyun providers
