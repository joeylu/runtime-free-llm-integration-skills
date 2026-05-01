---
name: skill-llm-openai
description: Standardize OpenAI API direct-model integration for chat, vision, image generation, structured outputs, reasoning effort, streaming, request URLs, and tool calling. Use when Codex needs to choose an OpenAI model, resolve an OpenAI request URL, wire Responses API or Chat Completions compatible request/response flows, expose reasoning effort, JSON object, JSON schema, tool/function calling, stream controls, model selectors, or shared progress and error states. Do not use for ChatGPT consumer-app settings, Apps SDK orchestration, Agents SDK orchestration, non-OpenAI providers, or prompt-only work with no integration change.
---

# Skill LLM OpenAI

## Mission

Own the provider-specific part of OpenAI API direct-model integration while reusing the shared contracts under `../_shared`.

Keep this skill focused on:

- OpenAI model catalog
- OpenAI request URLs
- OpenAI model sync workflow
- OpenAI capability verification
- OpenAI transport rules by request kind
- OpenAI-specific logging additions

Do not make this skill own:

- ChatGPT consumer app settings
- Apps SDK flows
- Agents SDK orchestration
- business prompt content
- platform-specific UI layouts
- non-OpenAI providers

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

Then read these OpenAI-specific files:

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

- Treat this skill as OpenAI API direct-model work. Do not silently switch to Apps SDK or Agents SDK orchestration.
- Prefer the Responses API for reasoning, tool-calling, structured outputs, image input, or multi-turn state.
- Use the Image API for the bundled `gpt-image-2` imaging path. Do not wire the Responses image-generation hosted tool until the capability matrix explicitly models that hosted-tool path.
- Use Chat Completions only when the host project explicitly needs Chat Completions compatibility and the requested options are verified for that surface.
- Resolve the connection profile before selecting the model. Do not silently fall back between `build`, `plan`, or any other profile.
- Resolve the request URL from `references/request-urls.md` after selecting the API surface. Do not silently rewrite one request URL to another.
- Never store real API keys in this skill. Store only secret references such as environment variable names.
- Use the bundled OpenAI model catalog by default. Do not sync model metadata unless the user explicitly asks for sync or latest-model verification.
- When sync is explicitly requested, collect model rows, pricing, capabilities, context window, max input tokens, and max output tokens live from official docs by LLM review only. Do not use scripts, scrapers, SDK enum dumps, or automated catalog generators.
- When the user asks for sync, confirm one recency boundary first. Propose `6 months` by default and convert it into one absolute cutoff date before reviewing rows.
- Use `references/pricing-matrix.md` for billing region, currency, context band, metered side, and unit price. Do not reconstruct tiered pricing from catalog notes.
- Use `API Model` as both the model dropdown display text and submitted value. Do not put prices in model option labels.
- Use official OpenAI model IDs in the catalog.
- Keep provider-neutral request, response, progress, error, and UI contracts in `../_shared`. Do not clone those contracts inside this skill.
- Fail fast on unsupported or unverified combinations. Do not silently disable `stream`, `ReasoningEffort`, `ResponseFormat`, `Tools`, `Temperature`, `ImageSize`, `ImageCount`, or image edit inputs.
- If a requested advanced capability is marked `unknown`, stop and tell the user to sync the catalog or choose a verified path.
- Do not expose raw chain-of-thought unless official docs explicitly expose raw reasoning text for the chosen model and API surface.
- For current OpenAI reasoning models, prefer `ReasoningSummary` and normalized usage over raw `ThinkingContent`.
- Distinguish caller-defined function tools from OpenAI-hosted tools such as web search, file search, code interpreter, computer use, and image generation.

## Standard Workflow

1. Confirm that the task is OpenAI API direct-model access.
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
`vision` means "send text plus one or more images and receive understanding output", not "generate a new image".

## OpenAI-Specific Concepts

- `ReasoningEffort` maps to OpenAI `reasoning.effort`.
- `ReasoningSummary` maps to OpenAI `reasoning.summary`.
- `ResponseFormat = json_schema` maps to Responses `text.format.type = json_schema` or Chat Completions `response_format.type = json_schema`.
- `ResponseFormat = json_object` maps to Responses `text.format.type = json_object` or Chat Completions `response_format.type = json_object`.
- `Tools` maps to caller-defined OpenAI `function` tools unless the request explicitly asks for OpenAI-hosted tools.
- `ConnectionProfileKey` selects the key/base-URL profile, for example `build` or `plan`.

Example:
`ReasoningEffort = none` means effective thinking is false. `ReasoningEffort = medium` means effective thinking is true.

Example:
`ConnectionProfileKey = build` can use `OPENAI_BUILD_API_KEY`, while `ConnectionProfileKey = plan` can use `OPENAI_PLAN_API_KEY`.

## Do Not Use This Skill For

- ChatGPT consumer app settings
- ChatGPT Apps SDK components
- Agents SDK orchestration design
- Anthropic, Gemini, DeepSeek, Aliyun, or other non-OpenAI providers
- prompt engineering tasks that do not change integration code or contracts
