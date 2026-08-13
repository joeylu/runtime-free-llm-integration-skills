---
name: skill-llm-openai
description: Runtime contract for direct OpenAI API integration. Use it to resolve exact OpenAI model IDs, Responses or Chat Completions URLs, request fields, reasoning, tools, structured output, image input, Image API calls, streaming, response mapping, pricing references, and logging. Model choice remains with the user or host project.
---

# Skill LLM OpenAI

## Purpose

Define how an agent integrates a model already named by the user or host project. This skill does not recommend, approve, rank, or automatically replace models during ordinary implementation.

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

- Send the exact documented model ID. This skill currently maintains rules for `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, and `gpt-image-2`.
- Do not replace a requested model with another model or moving alias.
- Resolve connection profile, request kind, API surface, API version, endpoint kind, full route key, base URL, and request URL before capability lookup.
- Match capabilities by the exact full `RouteKey` row, including API version and endpoint kind.
- Prefer no surface implicitly: use the surface required by the project. Responses and Chat Completions have different payloads and continuation rules.
- Use `gpt-image-2` through the direct Image API rows. Responses hosted image generation is a separate tool flow whose main model is a GPT model.
- Reject requested fields marked `unsupported` or `unknown`; do not silently drop or translate them to another surface.
- Keep caller-defined functions in `Tools` and provider-hosted tools in `HostedTools`.
- Preserve response item IDs, call IDs, required linkage, encrypted reasoning items, and assistant `phase` when continuing a documented stateful flow.
- Never expose raw chain-of-thought. Map visible summaries to `ReasoningSummary` and opaque state to `ReasoningItems` or provider metadata.
- Store API-key references only. Never write secrets, authorization headers, MCP credentials, or signed URLs into these files or normal logs.
- Use `references/pricing-matrix.md` for estimates, including context bands and cache charges.

## Request Flow

1. Read the requested provider, region, model, and request kind from the host project or user.
2. Resolve the connection profile and exact request URL row.
3. Resolve the exact catalog and capability rows.
4. Validate every optional field before constructing the request.
5. Apply the matching transport.
6. Normalize the provider response, errors, progress, and logs through the shared contracts.

## OpenAI Field Mapping

- Responses `reasoning.effort` and Chat Completions `reasoning_effort` use the values recorded in the capability matrix.
- `TextVerbosity` maps to Responses `text.verbosity` or Chat Completions `verbosity` only where verified.
- Responses `reasoning.mode`, `reasoning.context`, and `previous_response_id` are Responses-only fields.
- Responses structured output maps through `text.format`; Chat Completions maps through `response_format`.
- `CacheKey` maps to `prompt_cache_key` where verified; explicit cache controls require the documented Responses mapping.

## Out of Scope

- ChatGPT consumer configuration
- Apps SDK or Agents SDK orchestration
- Realtime/audio integration
- fine-tuning
- model ranking or model permission policy
- non-OpenAI providers
