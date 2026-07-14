---
name: skill-llm-aliyun-bailian-intl
description: Standardize Alibaba Cloud Model Studio International direct-model integration through exact model, region, deployment scope, surface, version, URL, capability, role, pricing, transport, alias, and evidence contracts. Do not use China Mainland endpoints or prices.
---

# Skill LLM Alibaba Cloud Model Studio International

## Mission

Own the provider-specific layer for **Alibaba Cloud Model Studio International direct-model access only** while reusing the shared contracts under `../_shared`.

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

- Use provider identifier `aliyun-bailian-intl`.
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

This skill exposes the canonical request kinds selected by the catalog and profile; unpopulated kinds remain blocked.

A request kind is implemented only when the selected catalog row, profile, URL, capability, role, pricing policy, and transport all agree. The mere existence of an official endpoint does not make it selectable here.

## Provider-Specific Rules

- Never mix International and China Mainland endpoints, API keys, availability, serving regions, or prices.
- Resolve billing region, deployment scope, and serving region before choosing a price. The word `international` alone is not a billable region.
- Treat `qwen3.7-max` as a moving alias and verify its target date before production use; prefer an accepted fixed snapshot when deterministic behavior is required.
- A scheduled provider deprecation is not a shutdown. Keep the published deadline and replacement visible while the row remains selectable only by explicit policy.

## Out of Scope

- Aliyun China Mainland access
- Agent App orchestration
- non-Aliyun providers
- prompt-only work that does not change integration code or contracts
