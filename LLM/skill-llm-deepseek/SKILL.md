---
name: skill-llm-deepseek
description: Runtime contract for the direct DeepSeek API. Use it to resolve exact DeepSeek model IDs, Chat Completions and beta request URLs, thinking controls, reasoning history, JSON output, caller tools, strict function schemas, streaming, response mapping, pricing references, and logging. Model choice remains with the user or host project.
---

# Skill LLM DeepSeek

## Purpose

Define how an agent integrates a DeepSeek model already named by the user or host project.

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

- Send the exact model ID from `references/model-catalog.md`.
- Resolve connection profile, request kind, API surface, API version, endpoint kind, full route key, base URL, and request URL before capability lookup.
- Match capabilities by the exact full `RouteKey` row, including API version and endpoint kind.
- The normal Chat Completions surface and the beta strict-function surface are separate rows. Strict function schemas require the documented beta endpoint.
- Thinking mode returns `reasoning_content` alongside `content`.
- During tool-call continuation in thinking mode, preserve prior assistant `reasoning_content`, preserve tool-call identity, and keep assistant `content` non-null.
- DeepSeek V4 thinking mode rejects `tool_choice`; do not send it when effective thinking is enabled.
- Use the exact documented thinking and `reasoning_effort` fields. Do not invent OpenAI Responses fields for DeepSeek.
- Reject requested fields marked `unsupported` or `unknown`.
- Do not silently switch models, surfaces, URLs, or providers.
- Store API-key references only and redact authorization data from logs.

## Request Flow

1. Read the requested model, request kind, and surface.
2. Resolve the connection profile and exact request URL row.
3. Resolve the exact catalog and capability rows.
4. Determine effective thinking before validating tool and structured-output fields.
5. Apply the Chat Completions transport, including history-preservation rules.
6. Normalize response, errors, progress, and logs through the shared contracts.

## Out of Scope

- vision, imaging, or music without documented rows
- non-official DeepSeek gateways unless their compatibility is re-verified
- model ranking or permission policy
- non-DeepSeek providers
