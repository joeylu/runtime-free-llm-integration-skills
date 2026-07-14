---
name: skill-llm-deepseek
description: Standardize direct DeepSeek API integration through exact Chat Completions or beta surface contracts, thinking-mode constraints, role handling, pricing, transport, and evidence. Do not use for non-DeepSeek providers or generic OpenAI-compatible assumptions.
---

# Skill LLM DeepSeek

## Mission

Own the provider-specific layer for **DeepSeek direct API only** while reusing the shared contracts under `../_shared`.

This skill is a curated, fail-fast integration contract. It is not a complete live provider inventory and it does not prove remote runtime availability without an authenticated request.

## Read Order

Read the shared contracts first:

1. `../_shared/model-catalog-schema.md`
2. `../_shared/capability-matrix-schema.md`
3. `../_shared/request-url-matrix-schema.md`
4. `../_shared/pricing-matrix-schema.md`
5. `../_shared/connection-profile-schema.md`
6. `../_shared/role-support-matrix-schema.md`
7. `../_shared/evidence-manifest-schema.md`
8. `../_shared/request-envelope.md`
9. `../_shared/response-envelope.md`
10. `../_shared/error-contract.md`
11. `../_shared/progress-contract.md`
12. `../_shared/ui-binding.md`
13. `../_shared/logging-fields.md`
14. `../_shared/sync-policy.md`
15. `../_shared/recency-window-policy.md`

Then read the provider files:

1. `references/connection-profiles.md`
2. `references/model-catalog.md`
3. `references/request-urls.md`
4. `references/capability-matrix.md`
5. `references/role-support-matrix.md`
6. `references/pricing-matrix.md`
7. the matching `references/transport-*.md` file
8. references/logging-contract.md when logging is requested
9. references/model-sync.md only for explicit current-data sync

## Core Boundary Rules

- Use provider identifier `deepseek`.
- Resolve `ConnectionProfileKey` before model, surface, API version, URL, capability, role, or price selection.
- Select only catalog rows that satisfy the shared selector rule: locally selected, provider-callable, verified, and current.
- Resolve one exact `Request Kind + API Model + API Surface + API Version` capability row. A comma-separated surface or version is invalid.
- Resolve one exact request URL row. Never construct a URL by guessing or silently retry another surface, version, profile, key, region, or provider.
- Validate input roles and tool history against `references/role-support-matrix.md`. OpenAI compatibility does not imply complete role compatibility.
- Use `references/pricing-matrix.md` only after billing region, deployment scope, serving region, service tier, and effective window match the request.
- Treat `Provider Lifecycle`, `Local Selection`, and `Review Freshness` as independent. Do not infer lifecycle from age, replacement, or local preference.
- Keep caller-defined `Tools` separate from provider-hosted `HostedTools`.
- Reject unsupported, unknown, stale, conflicted, or out-of-scope options before sending. Never disable or rewrite a requested feature silently.
- Use the bundled reviewed data by default. Perform a live official-source sync only when the task asks for current verification or the required evidence is stale/missing.
- A sync may use reproducible automated extraction from official sources, but every changed fact requires reviewed claim-level evidence before it becomes verified.
- Store secret references only. Do not place API keys, signed URLs, or authorization headers in skill files or normal logs.

## Standard Workflow

1. Confirm this provider and region boundary.
2. Normalize the caller's legacy request-kind alias once, then use only canonical request kinds.
3. Resolve the connection profile and its allowed kinds, surfaces, versions, models, and regional scope.
4. Select a catalog row using the shared selector rule; never auto-select a newer candidate.
5. Resolve the exact route from `request-urls.md`.
6. Resolve the exact capability and role rows; validate every caller field and every required history field.
7. Resolve pricing only when the exact billing scope is present.
8. Build the shared request envelope and map it through the matching provider transport.
9. Send with the requested stream semantics; do not change surface or model after an error.
10. Normalize output through the shared response envelope, error, progress, UI, and logging contracts.
11. For current-data changes, update evidence first and run `python tools/validate_repo.py` after all dependent matrices are updated.

## Supported Request-Kind Boundary

This skill exposes `text-chat` for selected models; all other canonical kinds remain blocked unless fully added.

A request kind is implemented only when the selected catalog row, profile, URL, capability, role, pricing policy, and transport all agree. The mere existence of an official endpoint does not make it selectable here.

## Provider-Specific Rules

- Treat `chat-completions@provider-default` and `beta@beta` as separate surfaces. Strict tool schemas are allowed only on the exact beta row.
- When effective thinking is enabled, reject `ToolChoice`; do not silently omit a caller-supplied value.
- For thinking-mode tool history, preserve `reasoning_content` and a non-null assistant `content` exactly as required by the transport.
- The `developer` role is unsupported. Apply only the explicit normalization policy from `references/role-support-matrix.md`; never change instruction precedence silently.
- Treat `deepseek-chat` and `deepseek-reasoner` as scheduled-deprecated aliases with their encoded target, mode, and shutdown deadline; never use them as defaults.

## Out of Scope

- non-DeepSeek providers
- image, music, video, speech, or realtime implementation without complete selected contracts
- generic OpenAI compatibility assumptions
- prompt-only work that does not change integration code or contracts
