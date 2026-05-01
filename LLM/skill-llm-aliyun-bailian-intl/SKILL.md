---
name: skill-llm-aliyun-bailian-intl
description: Standardize Aliyun Bailian International/Singapore direct-model integration for chat, vision, imaging, and music across Unity, websites, apps, and backends. Use when Codex needs to choose an international Aliyun Bailian model, resolve the international base URL and request URL, build direct-model request/response flows, wire stream or non-stream transport, expose thinking and temperature controls, build model selectors, or present shared progress and error states. Do not use for Aliyun Bailian China Mainland, Agent App orchestration, non-Aliyun providers, or prompt-only work with no integration change.
---

# Skill LLM Aliyun Bailian International

## Mission

Own the provider-specific part of Aliyun Bailian International/Singapore direct-model integration while reusing the shared contracts under `../_shared`.

Keep this skill focused on:

- Aliyun Bailian International model catalog
- Aliyun Bailian International request URLs
- Aliyun Bailian International model sync workflow
- Aliyun Bailian International capability verification
- Aliyun transport rules by model type
- Aliyun-specific logging additions

Do not make this skill own:

- Aliyun Bailian China Mainland access
- Agent App flows
- business prompt content
- platform-specific UI layouts
- non-Aliyun providers

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

Then read these Aliyun International-specific files:

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

- Treat this skill as Aliyun Bailian International/Singapore `direct-model` only. Do not silently switch to China Mainland or Agent App.
- Use provider identifier `aliyun-bailian-intl`.
- Resolve a provided connection profile before selecting the model. Do not silently fall back between profiles, API keys, base URLs, request URLs, or regions.
- Resolve the request URL from `references/request-urls.md` after selecting the API surface.
- Use the bundled International model catalog by default. Do not sync model metadata unless the user explicitly asks for sync or latest-model verification.
- When sync is explicitly requested, collect model rows, pricing, capabilities, context window, max input tokens, and max output tokens live from official Alibaba Cloud International docs by LLM review only. Do not use scripts, scrapers, SDK enum dumps, or automated catalog generators.
- When the user asks for sync, confirm one recency boundary first. Propose `6 months` by default and convert it into one absolute cutoff date before reviewing rows.
- Use `references/pricing-matrix.md` for International billing region, currency, context band, metered side, and unit price. Do not reconstruct tiered pricing from catalog notes.
- Use `API Model` as both the model dropdown display text and submitted value. Do not put prices in model option labels.
- Use official model IDs in the catalog.
- Keep provider-neutral request, response, progress, error, and UI contracts in `../_shared`. Do not clone those contracts inside this skill.
- Fail fast on unsupported or unverified combinations. Do not silently disable `thinking`, `stream`, `temperature`, `json_object`, `seed`, `size`, or `duration`.
- If a requested advanced capability is marked `unknown`, stop and tell the user to either sync the catalog or choose a verified path.
- Distinguish `stream` transport from `non-stream` transport in both logic and UI.
- Do not fake progress percentages unless the provider exposes a stable job progress value.

## Standard Workflow

1. Confirm that the task is Aliyun Bailian International/Singapore direct-model access.
2. Identify the request kind: `chat`, `vision`, `imaging`, or `music`.
3. Read `references/connection-profiles.md` and resolve `ConnectionProfileKey` when the host defines Aliyun profiles.
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

- `chat`: text-first conversation requests, with optional structured output when verified
- `vision`: text plus image understanding requests
- `imaging`: image generation or image-edit job requests
- `music`: music or audio generation job requests

Example:
`vision` means "send text plus one or more images and receive understanding output", not "generate a new image".

## Catalog and Capability Rules

- `references/model-catalog.md` is the default local source for International model names, labels, and pricing notes.
- `references/pricing-matrix.md` is the structured source for International region, currency, context-band, and unit-price rows.
- The active rows in `references/model-catalog.md` represent the locally selected options, not the full provider inventory.
- `references/capability-matrix.md` is the default local source for `non-stream`, `stream`, thinking mode/default, thinking-budget field support, temperature mode/defaults, `json_object` mode, `seed`, `image size`, `image count`, `duration`, and other options.
- If a model exists in the catalog but a requested advanced capability is still `unknown`, stop before wiring that feature.
- Imaging and music rows may be empty or partially verified depending on the latest explicit sync. A selected imaging row verifies only the model choice; optional request fields still require capability-matrix verification.

## Transport Rules

- `chat` and `vision` may use `non-stream` transport when `Supports Non-Stream` is `verified` or `inherited`.
- `chat` and `vision` may use `stream` transport only when `Supports Stream = verified`.
- `imaging` uses the request URL row's selected native surface; use job-style progress only for async rows such as `dashscope-native-async`.
- `music` remains blocked until catalog, request URL, and capability rows are all verified.
- Keep request assembly separate from UI update logic. UI should consume shared progress events rather than inspect raw provider payloads directly.
- Treat `thinking` as request intent first and provider-applied behavior second. Reflect both in the normalized response.

## Do Not Use This Skill For

- Aliyun Bailian China Mainland access
- Agent App orchestration
- OpenAI, Anthropic, Gemini, DeepSeek, or other non-Aliyun providers
- platform-specific UI layout design
- prompt engineering tasks that do not change integration code or contracts
