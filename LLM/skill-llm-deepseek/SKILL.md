---
name: skill-llm-deepseek
description: Standardize DeepSeek API direct-model integration for OpenAI-compatible chat, thinking mode, JSON output, streaming, request URLs, and tool calling. Use when Codex needs to choose a DeepSeek model, resolve a DeepSeek request URL, wire chat-completions request/response flows, expose thinking controls, JSON object output, function/tool calling, stream controls, model selectors, connection profiles, or shared progress and error states. Do not use for non-DeepSeek providers, Agent/App orchestration, or prompt-only work with no integration change.
---

# Skill LLM DeepSeek

## Mission

Own the provider-specific part of DeepSeek API direct-model integration while reusing the shared contracts under `../_shared`.

Keep this skill focused on:

- DeepSeek model catalog
- DeepSeek request URLs
- DeepSeek model sync workflow
- DeepSeek capability verification
- DeepSeek OpenAI-compatible transport rules
- DeepSeek-specific logging additions

Do not make this skill own:

- business prompt content
- platform-specific UI layouts
- non-DeepSeek providers

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

Then read these DeepSeek-specific files:

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

- Treat this skill as DeepSeek API direct-model work.
- Prefer DeepSeek's OpenAI-compatible Chat Completions API for selected chat models.
- Resolve the connection profile before selecting the model. Do not silently fall back between profiles, API keys, base URLs, or compatibility surfaces.
- Resolve the request URL from `references/request-urls.md` after selecting the API surface. Do not silently rewrite one request URL to another.
- Never store real API keys in this skill. Store only secret references such as environment variable names.
- Use the bundled DeepSeek model catalog by default. Do not sync model metadata unless the user explicitly asks for sync or latest-model verification.
- When sync is explicitly requested, collect model rows, pricing, capabilities, context window, max input tokens, and max output tokens live from official docs by LLM review only. Do not use scripts, scrapers, SDK enum dumps, or automated catalog generators.
- When the user asks for sync, confirm one recency boundary first. Propose `6 months` by default and convert it into one absolute cutoff date before reviewing rows.
- Use `references/pricing-matrix.md` for billing region, currency, context band, metered side, and unit price. Do not reconstruct tiered pricing from catalog notes.
- Use `API Model` as both the model dropdown display text and submitted value. Do not put prices in model option labels.
- Use official DeepSeek model IDs in the catalog.
- Keep provider-neutral request, response, progress, error, and UI contracts in `../_shared`. Do not clone those contracts inside this skill.
- Fail fast on unsupported or unverified combinations. Do not silently disable `stream`, `thinking`, `ResponseFormat`, `Tools`, `Temperature`, or strict tool schemas.
- If a requested advanced capability is marked `unknown`, stop and tell the user to sync the catalog or choose a verified path.
- Preserve DeepSeek `reasoning_content` in follow-up turns when the prior assistant message included tool calls; official docs say omitting it in that path can cause a 400 error.
- Treat strict tool schemas as a beta-surface feature unless the active profile explicitly allows the beta API surface.

## Standard Workflow

1. Confirm that the task is DeepSeek API direct-model access.
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

Current bundled DeepSeek coverage selects only `chat` rows.

## DeepSeek-Specific Concepts

- `ThinkingRequested` maps to DeepSeek `thinking.type = enabled | disabled`.
- `ReasoningEffort` maps to DeepSeek OpenAI-compatible `reasoning_effort = high | max` when thinking is enabled.
- `ThinkingContent` maps to DeepSeek `reasoning_content`.
- `ResponseFormat = json_object` maps to OpenAI-compatible `response_format.type = json_object`.
- `Tools` maps to OpenAI-compatible function tools.
- Strict tool schemas require the DeepSeek beta surface.

Example:
`ThinkingRequested = false` means send `thinking.type = disabled`.

Example:
If an assistant message has `tool_calls`, keep its `reasoning_content` when sending the next turn; without tool calls, DeepSeek says prior `reasoning_content` is ignored.

## Do Not Use This Skill For

- OpenAI, Gemini, Aliyun, Anthropic, or other non-DeepSeek providers
- DeepSeek website settings unrelated to API integration
- platform-specific UI layout design
- prompt engineering tasks that do not change integration code or contracts
