# Shared Model Catalog Schema v2

Use this schema for every provider `model-catalog.md`.

The catalog is a **curated allowlist**, not a complete live inventory, unless a provider file explicitly declares `CoverageMode: complete-inventory`.

## Canonical Registry

Every provider catalog must contain a `Canonical Registry` table. Its key is:

`Request Kind + API Model`

| Column | Meaning |
| --- | --- |
| `Request Kind` | Canonical kind: `text-chat`, `multimodal-chat`, `image-generation`, `speech-generation`, `transcription`, `realtime-audio`, `music-generation`, or `video-generation` |
| `API Model` | Exact provider model identifier sent on the wire |
| `Display Name` | Human-readable name; never use it as the wire value |
| `Primary API Surface` | Preferred exact surface for new integrations; capability lookup still uses a surface-specific row |
| `Provider Lifecycle` | `stable`, `preview`, `scheduled-deprecated`, `deprecated`, `shutdown`, `removed`, or `unknown` |
| `Provider Shutdown At` | Exact provider-announced shutdown timestamp/date, or `none` / `unknown`; never store an earliest-possible retirement date here |
| `Provider Earliest Retirement At` | Provider-published earliest possible retirement date, or `none` / `unknown`; this does not by itself mean the exact shutdown time is known |
| `Local Selection` | `selected`, `not-selected`, or `unreviewed` |
| `Selection Reason` | Required for every non-selected row and recommended for selected alternatives |
| `Is Default` | `yes` or `no`; exactly one selected default per implemented request kind |
| `Verification State` | `verified`, `inherited`, `conflicted`, or `unknown` |
| `Review Freshness` | `current`, `stale`, or `unreviewed`; this never changes provider lifecycle |
| `Last Verified At` | Exact review date, or `unverified` |
| `Official Context Display` | Provider wording such as `1M`, `384K`, `198K`, or `n/a` |
| `Exact Context Tokens` | Exact integer only when the provider defines one; otherwise `unknown` / `n/a` |
| `Official Max Input Display` | Provider wording, or `unknown` / `n/a` |
| `Exact Max Input Tokens` | Exact integer or mode-qualified integers only when official docs define them |
| `Official Max Output Display` | Provider wording, or `unknown` / `n/a` |
| `Exact Max Output Tokens` | Exact maximum integer only when official docs define it; never substitute a sample/default value |
| `Recommended Max Output Tokens` | Official recommendation when distinct from the maximum, or `unknown` / `n/a` |
| `Limit Unit Convention` | `exact-integer`, `decimal`, `binary`, `provider-unspecified`, or `n/a` |
| `Is Moving Alias` | `yes` or `no` |
| `Alias Target At Verification` | Exact target at the review date, or `none` / `unknown` |
| `Alias Mode` | Fixed behavior such as `thinking`, `non-thinking`, `provider-default`, or `n/a` |
| `Alias Target Verified At` | Review date for the target, or `n/a` / `unverified` |
| `Replacement Model` | Provider-recommended replacement or local migration target, or `none` / `unknown` |
| `Evidence Refs` | Comma-separated evidence-set IDs from `LLM/_evidence/evidence.json` |

## Orthogonal State Rule

These fields are independent:

1. `Provider Lifecycle` describes only the provider's published service state.
2. `Local Selection` describes only this repository's allowlist choice.
3. `Review Freshness` describes only whether the evidence has been reviewed recently enough for the repository policy.

Never infer one from another. In particular:

- a stable model may be `not-selected`;
- a preview model may be `selected` when the project explicitly accepts preview risk;
- a stale review does not make a model deprecated;
- an earliest-possible retirement date does not become an exact shutdown timestamp;
- a newer model does not make an older model provider-deprecated;
- a model outside a discovery window may remain provider-stable and selectable when intentionally retained.

## Selector Rule

A model is selectable only when all of the following are true:

- `Local Selection = selected`;
- `Provider Lifecycle` is `stable`, `preview`, or `scheduled-deprecated`;
- `Verification State = verified`;
- `Review Freshness = current`;
- the selected profile, request URL, capability row, and required price scope are also valid.

A `scheduled-deprecated` row may remain selectable only with an explicit deadline or earliest-retirement warning and a migration target. Never select `deprecated`, `shutdown`, `removed`, `unknown`, `conflicted`, `stale`, or `unreviewed` rows by default.

## Limits Rule

- Preserve the provider's displayed value in every `Official ... Display` field.
- Fill an exact integer only when an official source states the integer or explicitly defines the unit convention.
- If the provider writes `K`/`M` without defining the convention, keep the exact field `unknown` and set `Limit Unit Convention = provider-unspecified`.
- `Recommended Max Output Tokens` and `Exact Max Output Tokens` are different facts.
- Do not derive limits from pricing tiers, SDK enums, example payloads, observed errors, or sibling models.

## Coverage Rule

Every catalog must declare one of:

- `CoverageMode: curated-allowlist`: missing official models are allowed; every discovered but intentionally excluded mainstream candidate needs a `Selection Reason`.
- `CoverageMode: complete-inventory`: the sync process must compare against the provider's official inventory and report omissions.

This repository defaults to `curated-allowlist`.

## Legacy Compatibility View

Existing integrations may continue to read the old 21-column table while migrating. That table is a derived compatibility view and must be labeled as such.

Legacy mappings:

- `Catalog Status = active` does **not** mean locally selected; derive it only from a callable provider lifecycle.
- `Selection Status` mirrors `Local Selection`.
- `Recency Classification` is discovery metadata only and must never drive provider lifecycle.
- `Context Window Tokens`, `Max Input Tokens`, and `Max Output Tokens` mirror exact canonical fields and remain `unknown` when the provider only publishes an ambiguous display value.

New code must read the Canonical Registry.
