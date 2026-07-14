---
name: skill-llm-gemini
description: Runtime contract for direct Gemini Developer API integration. Use it to resolve exact Gemini model IDs, Interactions or GenerateContent URLs, thinking controls, tools, structured output, multimodal input, image generation/editing, state, streaming, caching, response mapping, pricing references, and logging. Model choice remains with the user or host project.
---

# Skill LLM Gemini

## Purpose

Define how an agent integrates a Gemini model already named by the user or host project. This skill does not make model recommendations and does not cover Vertex AI.

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

Read `references/hosted-tools.md` when provider-hosted tools are requested.

## Runtime Rules

- Send the exact documented model ID from `model-catalog.md`.
- Resolve connection profile, request kind, API surface, API version, endpoint kind, full route key, base URL, and request URL before capability lookup.
- Match capabilities by the exact full `RouteKey` row, including API version and endpoint kind.
- Interactions `v1`, Interactions `v1beta`, `generate-content`, and `stream-generate-content` are separate surfaces. Do not migrate or fall back between them silently.
- Use stable Interactions `v1` when the project requests Interactions without an explicit beta requirement. Keep `v1beta` explicit.
- Reject model IDs documented as shut down. Do not rewrite them to another model.
- For Gemini 3.x text rows in this skill, caller overrides for `temperature`, `top_p`, and `top_k` are blocked where the capability matrix records provider-default-only behavior.
- Map verified thinking levels through `ReasoningEffort`; do not combine them with legacy `thinking_budget`.
- Preserve thought signatures and function-call identity exactly when replay is required. Do not display signatures or raw model thoughts.
- Keep caller-defined `Tools` separate from `HostedTools`.
- Interactions custom safety settings and explicit caching are unsupported in the documented rows. GenerateContent explicit caching requires an existing cache resource and its exact transport mapping.
- A continued Interaction must resend tools, system instruction, and generation configuration when needed; the continuation ID does not preserve them.
- When `store=false`, do not treat the returned Interaction ID as reusable state.
- Reject requested fields marked `unsupported` or `unknown`.

## Request Flow

1. Read the requested model, request kind, and API surface.
2. Resolve the connection profile and exact request URL row.
3. Resolve the exact catalog and capability rows.
4. Validate thinking, tools, structured output, media input, cache, state, and stream fields.
5. Apply the matching transport and hosted-tool rules.
6. Normalize the response, errors, progress, and logs through the shared contracts.

## Gemini Field Mapping

- Interactions `ContinuationId` maps to `previous_interaction_id`; `StoreResponse` maps to `store`; streaming uses `stream: true` on the same endpoint.
- GenerateContent multi-turn state replays the complete content history, including required thought signatures and function-call identity.
- Thinking-level values and defaults are model-specific and come from the capability matrix.
- Structured-output payloads differ between Interactions and GenerateContent.
- Interactions reasoning summaries map through `generation_config.thinking_summaries` only where verified.
- `vision` means image understanding through typed media parts. Audio, video, and PDF require their own typed host inputs and must not be disguised as `Inputs.Images`.
- `imaging` means image generation or editing. Reference images are imaging inputs; `Inputs.ImageCount` is an output-count field and requires separate verification.

## Out of Scope

- Vertex AI endpoints, service accounts, regions, or provisioned throughput
- Gemini consumer application settings
- automatic model discovery during ordinary implementation
- raw chain-of-thought display
- model ranking or permission policy
