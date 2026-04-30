---
name: skill-llm-aliyun
description: Standardize Aliyun Bailian direct-model integration for chat, vision, imaging, and music across Unity, websites, apps, and backends. Use when Codex needs to choose an Aliyun model, build direct-model request/response flows, wire stream or non-stream transport, expose thinking and temperature controls, build model selectors, or present shared progress and error states. Do not use for Agent App orchestration, non-Aliyun providers, or prompt-only work with no integration change.
---

# Skill LLM Aliyun

## Mission

Own the provider-specific part of Aliyun Bailian direct-model integration while reusing the shared contracts under `../_shared`.

Keep this skill focused on:

- Aliyun model catalog
- Aliyun model sync workflow
- Aliyun capability verification
- Aliyun transport rules by model type
- Aliyun-specific logging additions

Do not make this skill own:

- Agent App flows
- business prompt content
- platform-specific UI layouts
- non-Aliyun providers

## Read Order

Read these shared files first:

1. `../_shared/model-catalog-schema.md`
2. `../_shared/capability-matrix-schema.md`
3. `../_shared/connection-profile-schema.md`
4. `../_shared/recency-window-policy.md`
5. `../_shared/request-envelope.md`
6. `../_shared/response-envelope.md`
7. `../_shared/error-contract.md`
8. `../_shared/progress-contract.md`
9. `../_shared/ui-binding.md`
10. `../_shared/sync-policy.md`
11. `../_shared/logging-fields.md`

Then read these Aliyun-specific files:

1. `references/connection-profiles.md`
2. `references/model-catalog.md`
3. `references/model-sync.md`
4. `references/capability-matrix.md`
5. One or more transport files that match the request:
   - `references/transport-chat.md`
   - `references/transport-vision.md`
   - `references/transport-imaging.md`
   - `references/transport-music.md`
6. `references/logging-contract.md` when logging is requested

## Hard Rules

- Treat this skill as `direct-model` only. Do not silently switch to Agent App.
- Resolve a provided connection profile before selecting the model. Do not silently fall back between profiles, API keys, or base URLs.
- Use the bundled Aliyun model catalog by default. Do not sync model metadata unless the user explicitly asks for sync or latest-model verification.
- When the user asks for sync, confirm one recency boundary first. Propose `6 months` by default and convert it into one absolute cutoff date before reviewing rows.
- Keep dropdown `label` and submitted `value` separate. Use `UI Label` for display and `API Model` for submission.
- Use official model IDs in the catalog. If the user gives a shorthand such as `qwen3.6-p`, normalize it to the official ID before writing.
- Keep provider-neutral request, response, progress, error, and UI contracts in `../_shared`. Do not clone those contracts inside this skill.
- Fail fast on unsupported or unverified combinations. Do not silently disable `thinking`, `stream`, `temperature`, `json_object`, `seed`, `size`, or `duration`.
- If a requested advanced capability is marked `unknown`, stop and tell the user to either sync the catalog or choose a verified path.
- For `stream`, treat the official Aliyun stream transport document plus the matching official model-family page as a valid evidence chain. Do not require a model-specific stream snippet when the family-level transport contract clearly applies.
- Resolve the effective thinking state before gating `temperature` or `json_object`. Do not silently flip a model away from its documented default thinking mode just to satisfy another option.
- For this skill, inherited `chat` or `vision` non-stream support may be used only as an explicitly documented base-path exception. Do not extend that exception to advanced options, and do not use it when the current capability row is `unknown` or missing.
- Distinguish `stream` transport from `non-stream` transport in both logic and UI.
- Do not fake progress percentages unless the provider exposes a stable job progress value.
- Use official Aliyun documentation only when syncing models or capabilities.

## Standard Workflow

1. Confirm that the task is Aliyun Bailian direct-model access.
2. Identify the request kind: `chat`, `vision`, `imaging`, or `music`.
3. Read `references/connection-profiles.md` and resolve `ConnectionProfileKey` when the host defines Aliyun profiles.
4. Read `references/model-catalog.md` and select only rows whose `Catalog Status` is `active` and `Selection Status` is `selected`.
5. Apply profile restrictions before choosing the final model and API surface.
6. Read `references/capability-matrix.md` and verify every requested option before wiring the request.
7. Read the matching transport file for the request kind.
8. Build the request with the shared request envelope from `../_shared/request-envelope.md`.
9. Map the provider response into the shared response envelope from `../_shared/response-envelope.md`.
10. If the user wants UI, apply `../_shared/ui-binding.md`, `../_shared/progress-contract.md`, and `../_shared/error-contract.md`.
11. If the user wants logging, apply `../_shared/logging-fields.md` and `references/logging-contract.md`.
12. Sync the model catalog only when the user explicitly asks for latest-model sync, and apply `../_shared/recency-window-policy.md` before reviewing rows.

## Request Kinds

Use these meanings consistently:

- `chat`: text-first conversation requests, with optional structured output when verified
- `vision`: text plus image understanding requests
- `imaging`: image generation or image-edit job requests
- `music`: music or audio generation job requests

Example:
`vision` means "send text plus one or more images and receive understanding output", not "generate a new image".

## Catalog and Capability Rules

- `references/model-catalog.md` is the default local source for model names, labels, and pricing notes.
- The active rows in `references/model-catalog.md` represent the locally selected options, not the full provider inventory.
- `references/capability-matrix.md` is the default local source for `non-stream`, `stream`, thinking mode/default, thinking-budget field support, temperature mode/defaults, `json_object` mode, `seed`, `image size`, `image count`, `duration`, and other options.
- For `stream`, use the official Aliyun stream transport doc together with the matching official model-family page when they clearly describe the same callable family.
- If a model exists in the catalog but a requested advanced capability is still `unknown`, stop before wiring that feature.
- Imaging and music rows may be empty or partially verified depending on the latest explicit sync. A selected imaging row verifies only the model choice; optional request fields still require capability-matrix verification.

## Transport Rules

- `chat` and `vision` may use `non-stream` transport when `Supports Non-Stream` is `verified` or `inherited`.
- `chat` and `vision` may use `stream` transport only when `Supports Stream` is `verified`.
- `imaging` and `music` are modeled as job-style flows by default unless the Aliyun catalog later verifies a stream path.
- Keep request assembly separate from UI update logic. UI should consume shared progress events rather than inspect raw provider payloads directly.
- Treat `thinking` as request intent first and provider-applied behavior second. Reflect both in the normalized response.

## Logging Rules

- Log normalized request and response summaries first.
- Add provider-specific raw payload snapshots only when the caller asks for debugging or trace retention.
- Include `request kind`, `model`, `stream/non-stream`, `thinking requested`, `thinking applied`, `usage`, `latency`, and `error code`.

## Do Not Use This Skill For

- Agent App orchestration
- OpenAI, Anthropic, Gemini, or other non-Aliyun providers
- platform-specific UI layout design
- prompt engineering tasks that do not change integration code or contracts
