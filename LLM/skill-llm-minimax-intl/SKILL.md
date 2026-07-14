---
name: skill-llm-minimax-intl
description: Runtime contract for MiniMax International direct-model integration. Use it to resolve exact MiniMax model IDs, OpenAI-compatible Chat Completions, multimodal M3 input, image generation, music generation, connection profiles, request fields, response mapping, pricing references, and logging. Model choice remains with the user or host project.
---

# Skill LLM MiniMax International

## Purpose

Define how an agent integrates a International MiniMax model already named by the user or host project. Keep this region separate because domains, credentials, availability, and pricing may differ.

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

1. `references/api-surface-scope.md`
2. `references/connection-profiles.md`
3. `references/request-urls.md`
4. `references/model-catalog.md`
5. `references/pricing-matrix.md`
6. `references/capability-matrix.md`
6. the transport for the requested kind
7. `references/logging-contract.md` when logging is implemented
8. `references/model-sync.md` only for an explicit update or verification task

Read `references/build-multimodal-http.md` only for endpoint references not represented by a shared request kind.

## Runtime Rules

- Use provider identifier `minimax-intl` and the official base URL recorded in the resolved profile.
- Send the exact model ID from `model-catalog.md`.
- Resolve connection profile, request kind, API surface, API version, endpoint kind, full route key, base URL, and request URL before capability lookup.
- Match capabilities by the exact full `RouteKey` row, including API version and endpoint kind.
- `chat` and `vision` use OpenAI-compatible `POST /v1/chat/completions` with `MiniMax-M3`.
- `imaging` uses `POST /v1/image_generation` with `image-01`.
- `music` uses `POST /v1/music_generation` with `music-2.6`.
- `MiniMax-M3` supports adaptive thinking, streaming, function tools, and image/video message input. This skill maps image input; video requires a separate typed host input contract.
- `max_completion_tokens` for `MiniMax-M3` has a documented recommended value of `131072` and maximum of `524288`.
- Treat `build` and `plan` as credential/profile names, not model policy. Enforce only the request-kind restrictions recorded in `connection-profiles.md`.
- Do not switch between `https://api.minimax.io/v1` and the other MiniMax region.
- Do not infer Anthropic-compatible behavior from the OpenAI-compatible rows.
- Reject requested fields marked `unsupported` or `unknown`; do not silently drop them.
- For music streaming, `stream=true` requires hex output.
- Video endpoints remain reference-only until the shared request and response contracts define `RequestKind = video`.

## Request Flow

1. Read the requested region, model, request kind, and profile.
2. Resolve the exact request URL row.
3. Resolve the exact catalog and capability rows.
4. Validate thinking, tools, media, stream, image, and music fields.
5. Apply the matching transport.
6. Normalize the provider response, errors, progress, and logs through the shared contracts.

## Request Kinds

- `chat`: text-first Chat Completions
- `vision`: image understanding through M3 message content
- `imaging`: image generation through `image-01`
- `music`: music generation through `music-2.6`

## Out of Scope

- the other MiniMax region
- Anthropic-compatible MiniMax surfaces
- first-class video integration before the shared schema defines it
- model ranking or permission policy
- non-MiniMax providers
