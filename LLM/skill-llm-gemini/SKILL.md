---
name: skill-llm-gemini
description: Standardize Google Gemini API direct-model integration for chat, vision, Nano Banana image generation and editing, thinking levels, structured outputs, streaming, request URLs, and function calling. Use when Codex needs to choose a Gemini model, resolve a Gemini request URL, wire generateContent or streamGenerateContent flows, expose thinking controls, JSON schema output, tool/function calling, image input, image generation, connection profiles, model selectors, or shared progress and error states. Do not use for Vertex AI, non-Gemini Google Cloud APIs, non-Gemini providers, Agent/App orchestration, or prompt-only work with no integration change.
---

# Skill LLM Gemini

## Mission

Own the provider-specific part of Google Gemini API direct-model integration while reusing the shared contracts under `../_shared`.

Keep this skill focused on:

- Gemini Developer API model catalog
- Gemini Developer API request URLs
- Gemini model sync workflow
- Gemini capability verification
- Gemini transport rules by request kind
- Gemini-specific logging additions

Do not make this skill own:

- Vertex AI routing
- Google AI Studio UI behavior unrelated to API integration
- business prompt content
- platform-specific UI layouts
- non-Gemini providers

## Read Order

Read these shared files first:

1. `../_shared/model-catalog-schema.md`
2. `../_shared/pricing-matrix-schema.md`
3. `../_shared/capability-matrix-schema.md`
4. `../_shared/connection-profile-schema.md`
5. `../_shared/request-url-matrix-schema.md`
6. `../_shared/recency-window-policy.md`
7. `../_shared/request-envelope.md`
8. `../_shared/response-envelope.md`
9. `../_shared/error-contract.md`
10. `../_shared/progress-contract.md`
11. `../_shared/ui-binding.md`
12. `../_shared/sync-policy.md`
13. `../_shared/logging-fields.md`

Then read these Gemini-specific files:

1. `references/connection-profiles.md`
2. `references/request-urls.md`
3. `references/model-catalog.md`
4. `references/pricing-matrix.md`
5. `references/model-sync.md`
6. `references/capability-matrix.md`
7. One or more transport files that match the request:
   - `references/transport-chat.md`
   - `references/transport-vision.md`
   - `references/transport-imaging.md`
   - `references/transport-music.md`
8. `references/logging-contract.md` when logging is requested

## Hard Rules

- Treat this skill as Gemini Developer API direct-model work. Do not silently switch to Vertex AI.
- Use `generateContent` for non-stream chat, vision, and imaging flows.
- Use `streamGenerateContent` only when the capability matrix verifies streaming for the selected request kind.
- Resolve the connection profile before selecting the model. Do not silently fall back between `build`, `plan`, API keys, base URLs, or API surfaces.
- Resolve the request URL from `references/request-urls.md` after selecting the API surface. Do not silently rewrite one request URL to another.
- Never store real API keys in this skill. Store only secret references such as environment variable names.
- Use the bundled Gemini model catalog by default. Do not sync model metadata unless the user explicitly asks for sync or latest-model verification.
- When sync is explicitly requested, collect model rows, pricing, capabilities, context window, max input tokens, and max output tokens live from official docs by LLM review only. Do not use scripts, scrapers, SDK enum dumps, or automated catalog generators.
- When the user asks for sync, confirm one recency boundary first. Propose `6 months` by default and convert it into one absolute cutoff date before reviewing rows.
- Use `references/pricing-matrix.md` for billing region, currency, context band, metered side, and unit price. Do not reconstruct tiered pricing from catalog notes.
- Use `API Model` as both the model dropdown display text and submitted value. Do not put prices in model option labels.
- Use official Gemini model IDs in the catalog.
- Keep provider-neutral request, response, progress, error, and UI contracts in `../_shared`. Do not clone those contracts inside this skill.
- Fail fast on unsupported or unverified combinations. Do not silently disable `stream`, `thinkingLevel`, `ResponseFormat`, `Tools`, `Temperature`, `ImageSize`, `ImageCount`, or image inputs.
- If a requested advanced capability is marked `unknown`, stop and tell the user to sync the catalog or choose a verified path.
- Do not expose raw chain-of-thought. Gemini exposes thought summaries and thought signatures, not raw reasoning.
- Preserve Gemini thought signatures in provider metadata for follow-up turns when the response includes them; do not display them as reasoning text.
- Treat Nano Banana models as `RequestKind = imaging`, not `vision`.

## Standard Workflow

1. Confirm that the task is Gemini Developer API direct-model access.
2. Identify the request kind: `chat`, `vision`, `imaging`, or `music`.
3. Read `references/connection-profiles.md` and resolve `ConnectionProfileKey` when the host has multiple profiles.
4. Read `references/model-catalog.md` and select only rows whose `Catalog Status` is `active` and `Selection Status` is `selected`.
5. Read `references/pricing-matrix.md` when billing, estimates, or price display are needed.
6. Apply profile restrictions before choosing the final model and API surface.
7. Read `references/request-urls.md` and resolve the exact request URL template for the selected surface.
8. Read `references/capability-matrix.md` and verify every requested option before wiring the request.
9. Read the matching transport file for the request kind.
10. Build the request with the shared request envelope from `../_shared/request-envelope.md`.
11. Map the provider response into the shared response envelope from `../_shared/response-envelope.md`.
12. If the user wants UI, apply `../_shared/ui-binding.md`, `../_shared/progress-contract.md`, and `../_shared/error-contract.md`.
13. If the user wants logging, apply `../_shared/logging-fields.md` and `references/logging-contract.md`.
14. Sync the model catalog only when the user explicitly asks for latest-model sync, and apply `../_shared/recency-window-policy.md` before reviewing rows.

## Request Kinds

Use these meanings consistently:

- `chat`: text-first conversation requests
- `vision`: text plus image understanding requests
- `imaging`: image generation or image edit requests
- `music`: music or audio generation requests

Example:
Nano Banana 2 image generation uses `RequestKind = imaging` and `Model = gemini-3.1-flash-image-preview`.

## Gemini-Specific Concepts

- `ReasoningEffort` maps to Gemini `generationConfig.thinkingConfig.thinkingLevel` for verified Gemini 3 rows.
- `ReasoningSummary` maps to Gemini `includeThoughts = true`, which returns thought summaries, not raw chain-of-thought.
- Gemini thought signatures are continuation metadata; store them as `ReasoningItems` or `ProviderMeta`, not `ThinkingContent`.
- `ResponseFormat = json_schema` maps to `generationConfig.responseMimeType = application/json` plus `generationConfig.responseJsonSchema`.
- Bare `ResponseFormat = json_object` is not locally verified for selected Gemini rows; prefer `json_schema`.
- `Tools` maps to Gemini `functionDeclarations` unless the request explicitly asks for Gemini hosted tools such as Google Search, URL Context, Code Execution, or File Search.
- `Inputs.ReferenceImages` maps to additional image parts for imaging models only when `Supports Image Input = verified`.
- `Inputs.ImageSize` maps to Gemini image `imageConfig.imageSize` for Gemini 3 image models, or to `imageConfig.aspectRatio` when only aspect ratio is verified.
- `ConnectionProfileKey` selects the key/base-URL profile, for example `build` or `plan`.

Example:
`ReasoningEffort = minimal` for `gemini-3.1-flash-image-preview` still means thinking can happen; Gemini docs say minimal does not mean thinking is off.

## Do Not Use This Skill For

- Vertex AI model routing or regional endpoint setup
- Google AI Studio consumer UI settings
- OpenAI, DeepSeek, Aliyun, Anthropic, or other non-Gemini providers
- platform-specific UI layout design
- prompt engineering tasks that do not change integration code or contracts
