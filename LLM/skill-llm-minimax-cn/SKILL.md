---
name: skill-llm-minimax-cn
description: Standardize MiniMax China Mainland direct-model integration for chat plus build-profile HTTP image and music generation, with build-only video endpoint references. Use when Codex needs to choose China Mainland MiniMax models, resolve minimaxi.com base URLs and request URLs, separate build and plan profiles, wire chat/imaging/music transports, or gate MiniMax capabilities through shared fail-fast contracts. Plan profile is chat-only. Build profile supports chat, imaging, music, and documented video HTTP links, but video is reference-only until the shared request schema adds a video request kind. Do not use for MiniMax International, Anthropic-compatible MiniMax surfaces, Agent/App orchestration, non-MiniMax providers, or prompt-only work with no integration change.
---

# Skill LLM MiniMax China Mainland

## Mission

Own the provider-specific part of MiniMax China Mainland direct-model integration while reusing the shared contracts under `../_shared`.

Keep this skill focused on:

- MiniMax China Mainland chat, imaging, and music model catalog
- MiniMax China Mainland request URLs
- MiniMax China Mainland model sync workflow
- MiniMax China Mainland capability verification
- MiniMax OpenAI-compatible chat transport rules
- MiniMax build-profile HTTP imaging and music transport rules
- MiniMax build-profile video HTTP endpoint references
- MiniMax-specific logging additions

Do not make this skill own:

- MiniMax International access
- MiniMax Anthropic-compatible access
- plan-profile image, audio, or video generation
- first-class video generation before the shared request schema adds `RequestKind = video`
- business prompt content
- platform-specific UI layouts
- non-MiniMax providers

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

Then read these MiniMax China Mainland-specific files:

1. `references/connection-profiles.md`
2. `references/request-urls.md`
3. `references/model-catalog.md`
4. `references/pricing-matrix.md`
5. `references/model-sync.md`
6. `references/capability-matrix.md`
7. `references/transport-chat.md`
8. `references/transport-imaging.md` when `RequestKind = imaging`
9. `references/transport-music.md` when `RequestKind = music`
10. `references/transport-vision.md` only to confirm vision is blocked
11. `references/build-multimodal-http.md` when build-profile video links or multimodal endpoint references are requested
12. `references/logging-contract.md` when logging is requested

## Hard Rules

- Treat this skill as MiniMax China Mainland direct-model access for `chat`, plus build-profile `imaging` and `music`.
- Use provider identifier `minimax-cn`.
- Use MiniMax China Mainland official endpoints only.
- Use OpenAI-compatible MiniMax Chat Completions only for `RequestKind = chat`.
- Do not silently switch to MiniMax International, `api.minimax.io`, or Anthropic-compatible MiniMax surfaces.
- Resolve a provided connection profile before selecting the model. Do not silently fall back between `build`, `plan`, API keys, base URLs, request URLs, or regions.
- Treat `build` and `plan` as separate connection profiles. They currently share the official MiniMax China Mainland base URL, but they use different API key references and purpose boundaries.
- Keep `ConnectionProfileKey = plan` chat-only. Do not expose imaging, music, video, or CLI-backed Token Plan multimodal flows through this skill's plan profile.
- Allow `ConnectionProfileKey = build` to use verified HTTP rows for `chat`, `imaging`, and `music`.
- Treat MiniMax build video as documented provider capability but reference-only in this skill pack. Because `../_shared/request-envelope.md` does not define `RequestKind = video`, stop before first-class video implementation unless the owner approves a shared schema extension.
- Resolve the request URL from `references/request-urls.md` after selecting the API surface.
- Use the bundled China Mainland model catalog by default. Do not sync model metadata unless the user explicitly asks for sync or latest-model verification.
- When sync is explicitly requested, collect model rows, pricing, capabilities, context window, max input tokens, and max output tokens live from official MiniMax China Mainland docs by LLM review only. Do not use scripts, scrapers, SDK enum dumps, or automated catalog generators.
- When the user asks for sync, confirm one recency boundary first. Propose `6 months` by default and convert it into one absolute cutoff date before reviewing rows.
- Use `references/pricing-matrix.md` for China Mainland billing region, currency, metered side, and unit price. Do not reconstruct pricing from catalog notes.
- Use `API Model` as both the model dropdown display text and submitted value.
- Keep provider-neutral request, response, progress, error, and UI contracts in `../_shared`. Do not clone those contracts inside this skill.
- Fail fast on unsupported or unverified combinations. Do not silently disable `stream`, `thinking`, `ResponseFormat`, `Tools`, `Temperature`, or request URL resolution.
- If a requested advanced capability is marked `unknown`, stop and tell the user to either sync the catalog or choose a verified path.
- Do not add MiniMax Anthropic-compatible rows unless the owner explicitly asks for that surface.

## Standard Workflow

1. Confirm that the task is MiniMax China Mainland direct-model access.
2. Set `RequestKind` to `chat`, `imaging`, or `music`. Stop on `video` until the shared schema adds that request kind.
3. Read `references/connection-profiles.md` and resolve `ConnectionProfileKey` when the host defines MiniMax profiles.
4. Read `references/model-catalog.md` and select only rows whose `Catalog Status` is `active` and `Selection Status` is `selected`.
5. Read `references/pricing-matrix.md` when billing, estimates, or price display are needed.
6. Apply profile restrictions before choosing the final model and API surface.
7. Read `references/request-urls.md` and resolve the exact request URL template for the selected API surface.
8. Read `references/capability-matrix.md` and verify every requested option before wiring the request.
9. Read the matching transport file: `transport-chat.md`, `transport-imaging.md`, or `transport-music.md`.
10. Build the request with the shared request envelope from `../_shared/request-envelope.md`.
11. Map the provider response into the shared response envelope from `../_shared/response-envelope.md`.
12. If the user wants UI, apply `../_shared/ui-binding.md`, `../_shared/progress-contract.md`, and `../_shared/error-contract.md`.
13. If the user wants logging, apply `../_shared/logging-fields.md` and `references/logging-contract.md`.
14. Sync the model catalog only when the user explicitly asks for latest-model sync, and apply `../_shared/recency-window-policy.md` before reviewing rows.

## Request Kinds

- `chat`: text-first conversation requests through MiniMax OpenAI-compatible Chat Completions
- `imaging`: build-profile text-to-image requests through MiniMax official Image Generation
- `music`: build-profile song generation requests through MiniMax official Music Generation

Current bundled MiniMax China Mainland coverage selects `chat`, build-profile `imaging`, and build-profile `music` rows.

`video` is not a shared request kind yet. Use `references/build-multimodal-http.md` for build-profile video endpoint links, then stop before implementation unless the owner extends the shared request and response contracts.

## MiniMax-Specific Concepts

- `ApiSurface = chat-completions` maps to MiniMax OpenAI-compatible `POST /v1/chat/completions`.
- `ApiSurface = image-generation` maps to MiniMax official `POST /v1/image_generation`.
- `ApiSurface = music-generation` maps to MiniMax official `POST /v1/music_generation`.
- MiniMax M2.7 chat models may return thinking content in OpenAI-compatible `content` using `<think>...</think>` tags. Normalize that text into `ThinkingContent` when present, and keep the final answer in `TextContent`.
- `ResponseFormat`, caller-defined `Tools`, strict tool schemas, and parallel tool calls are not selected in this first pass unless the capability matrix marks the exact option verified.
- `ConnectionProfileKey` selects the key/base-URL profile, for example `build` or `plan`.

Examples:
`ConnectionProfileKey = build` uses `MINIMAX_CN_BUILD_API_KEY`, while `ConnectionProfileKey = plan` uses `MINIMAX_CN_PLAN_API_KEY`. Both currently use `https://api.minimaxi.com/v1`, but the implementation must still resolve the selected profile instead of assuming the URL or key.

`ConnectionProfileKey = plan` with `RequestKind = imaging` must fail before request construction. `ConnectionProfileKey = build` with `RequestKind = imaging` may use `image-01` only after resolving the verified image request URL and capability row.

## Do Not Use This Skill For

- MiniMax International access
- MiniMax Anthropic-compatible API access
- MiniMax plan-profile image, audio, or video generation
- first-class MiniMax video implementation before `RequestKind = video` exists in shared contracts
- OpenAI, Gemini, DeepSeek, Aliyun, Anthropic, or other non-MiniMax providers
- platform-specific UI layout design
- prompt engineering tasks that do not change integration code or contracts
