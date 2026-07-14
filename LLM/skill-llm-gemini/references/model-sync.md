# Gemini Developer API Model and Metadata Sync

Use this workflow when the task requires current model, endpoint, capability, lifecycle, alias, role, or pricing verification for **Google Gemini Developer API**.

Read these shared contracts first:

- `../../_shared/sync-policy.md`
- `../../_shared/recency-window-policy.md`
- `../../_shared/model-catalog-schema.md`
- `../../_shared/capability-matrix-schema.md`
- `../../_shared/request-url-matrix-schema.md`
- `../../_shared/pricing-matrix-schema.md`
- `../../_shared/evidence-manifest-schema.md`
- `../../_shared/role-support-matrix-schema.md`

## Coverage Contract

`model-catalog.md` uses `CoverageMode: curated-allowlist`.

- A provider model may be official and stable while `Local Selection = not-selected`.
- Discovering a newer model never changes another model's provider lifecycle.
- A new candidate is not made selected or default automatically.
- A discovery lookback, when used, narrows research effort only. It never marks a provider model deprecated, shutdown, removed, or uncallable.

## Official Sources

Use official Google AI for Developers documentation only.

Preferred entry points:

- Models: `https://ai.google.dev/gemini-api/docs/models`
- Interactions API: `https://ai.google.dev/api/interactions-api`
- API versions: `https://ai.google.dev/gemini-api/docs/api-versions`
- Deprecations: `https://ai.google.dev/gemini-api/docs/deprecations`
- Changelog: `https://ai.google.dev/gemini-api/docs/changelog`
- Pricing: `https://ai.google.dev/gemini-api/docs/pricing`

Do not use Vertex AI documentation unless the task explicitly targets a separate Vertex skill, consumer Gemini behavior, third-party wrappers, forum posts, or screenshots as factual proof.

## Source Precedence

For a specific claim, prefer the narrowest applicable official source in this order:

1. exact endpoint/API reference for request fields, required combinations, enums, and errors;
2. exact model card or exact model table row for ID, modalities, limits, and stability label;
3. exact pricing table for currency, unit, region, deployment scope, service tier, and effective window;
4. lifecycle/deprecation notice for scheduled shutdown, removal, and replacement;
5. release notes or changelog for release dates, alias transitions, and historical status;
6. official examples or migration guides for recommended flows and compatibility details.

When equally authoritative sources conflict, record both claims with `conflict_state = open`, set the affected repository value to `unknown` or `conflicted`, and fail closed. Do not choose silently.

## Reproducible Collection

Automated extraction, comparison, normalization, and table generation are allowed when they operate only on official sources and preserve source URLs and locators. Every changed fact still requires LLM or human review before `Verification State = verified`.

Do not infer facts from SDK enums, model-name similarity, example defaults, observed errors, or a sibling model. Automation may copy and compare evidence; it may not manufacture evidence.

## Sync Procedure

1. Define the provider, region `global`, request kinds, surfaces, API versions, and pricing scopes in the task.
2. Use the default six-month discovery lookback only when no other research window is supplied. Convert it to an absolute date and record it as discovery metadata, not lifecycle state.
3. Inspect official current indexes plus the exact pages needed for every changed field.
4. Create or update claim records in `../../_evidence/evidence.json` first. Each claim must include a stable ID, exact field, reviewed value, official URL, reproducible locator, and review date.
5. Update `model-catalog.md`. Keep `Provider Lifecycle`, `Local Selection`, and `Review Freshness` independent. Preserve official display units and leave exact token integers `unknown` when the provider does not define the unit convention.
6. Update `request-urls.md` by exact `Request Kind + Model Scope + API Surface + API Version`. One row may not combine surfaces or versions.
7. Update `capability-matrix.md` by exact `Request Kind + API Model + API Surface + API Version`. Separate model support from surface support and mode-dependent constraints.
8. Update `pricing-matrix.md` by exact billing region, deployment scope, serving region, service tier, metered item, and effective window. Expired promotional rows remain historical and are never used for current estimates.
9. Update `role-support-matrix.md` for exact accepted roles, required assistant/tool history, and any explicit normalization. OpenAI compatibility never proves role compatibility by itself.
10. Update `connection-profiles.md` only after catalog, URL, capability, role, and price scopes agree. Profiles may narrow capabilities but never expand them.
11. Keep newly discovered mainstream models as `not-selected` candidates with a reason unless the repository owner explicitly selects them. Do not replace an existing default merely because a newer model exists.
12. Preserve unavailable historical rows with accurate lifecycle and shutdown evidence when they are useful for migration. Do not leave them selectable.
13. Run `python tools/validate_repo.py` and resolve every error. Treat warnings as review items, not proof that remote facts are current.

## Field Rules

- A fact is `verified` only when its evidence identifies the exact provider scope and the exact model/surface/version or explicitly applies to that whole protocol family.
- Use `unknown` when an official source does not expose the value clearly.
- Never derive max input from context minus max output.
- Never convert an ambiguous `K` or `M` display into a binary or decimal integer without an official convention.
- Never apply one region's price to another region or deployment scope.
- Moving aliases require `Alias Target At Verification` and `Alias Target Verified At`; production profiles should prefer a fixed snapshot when the provider offers one and the project accepts it.
- Scheduled deprecation requires a provider date/time and a replacement or explicit `unknown`.
- Price promotions require effective and expiry timestamps. Once expired, they cannot be `current`.

## Output Contract

A completed sync leaves the changed provider with:

- an internally consistent curated catalog;
- exact surface/version URL and capability rows;
- exact regional pricing scope where pricing is claimed;
- a role-support matrix;
- claim-level official evidence;
- no silent fallback, inferred capability, inferred lifecycle, or inferred price;
- no automatic model selection or default change without repository-owner intent.
