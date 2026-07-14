# MiniMax International Model Catalog

- `CoverageMode: curated-allowlist`
- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Every factual row is valid only through its own `Last Verified At` and `Evidence Refs`.
- New models are not made default automatically.

Read `../../_shared/model-catalog-schema.md` before using this file.

## Selector Rule

Use only Canonical Registry rows where `Local Selection = selected`, `Provider Lifecycle` is callable, `Verification State = verified`, and `Review Freshness = current`. Then resolve the exact profile, URL, API version, capability row, and pricing scope.

## Canonical Registry

| Request Kind | API Model | Display Name | Primary API Surface | Provider Lifecycle | Provider Shutdown At | Provider Earliest Retirement At | Local Selection | Selection Reason | Is Default | Verification State | Review Freshness | Last Verified At | Official Context Display | Exact Context Tokens | Official Max Input Display | Exact Max Input Tokens | Official Max Output Display | Exact Max Output Tokens | Recommended Max Output Tokens | Limit Unit Convention | Is Moving Alias | Alias Target At Verification | Alias Mode | Alias Target Verified At | Replacement Model | Evidence Refs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `MiniMax-M2.7` | `MiniMax M2.7` | `chat-completions` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `204,800` | `204800` | `unknown` | `unknown` | `204,800` | `204800` | `65536` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-text-chat-minimax-m2-7-1c8f5d565f` |
| `text-chat` | `MiniMax-M2.7-highspeed` | `MiniMax M2.7 Highspeed` | `chat-completions` | `stable` | `none` | `none` | `selected` | `selected latency-optimized alternative` | `no` | `verified` | `current` | `2026-07-14` | `204,800` | `204800` | `unknown` | `unknown` | `204,800` | `204800` | `65536` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-text-chat-minimax-m2-7-highspeed-e0ecde46f3` |
| `text-chat` | `MiniMax-M3` | `MiniMax M3` | `chat-completions` | `stable` | `none` | `none` | `not-selected` | `current flagship candidate added without changing local default` | `no` | `verified` | `current` | `2026-07-14` | `1,000,000` | `1000000` | `unknown` | `unknown` | `524,288` | `524288` | `131072` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-text-chat-minimax-m3-c67b84097f` |
| `multimodal-chat` | `MiniMax-M3` | `MiniMax M3` | `chat-completions` | `stable` | `none` | `none` | `not-selected` | `multimodal flagship candidate; no automatic exposure` | `no` | `verified` | `current` | `2026-07-14` | `1,000,000` | `1000000` | `unknown` | `unknown` | `524,288` | `524288` | `131072` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-multimodal-chat-minimax-m3-7c6b9ba899` |
| `image-generation` | `image-01` | `image-01` | `image-generation` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-image-generation-image-01-d8c85c6ce7` |
| `music-generation` | `music-2.6` | `Music 2.6` | `music-generation` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-music-generation-music-2-6-e499ca096d` |
| `text-chat` | `MiniMax-M2.5` | `MiniMax M2.5` | `chat-completions` | `stable` | `none` | `none` | `not-selected` | `legacy candidate retained for compatibility history` | `no` | `verified` | `current` | `2026-07-14` | `204,800` | `204800` | `unknown` | `unknown` | `204,800` | `204800` | `65536` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-text-chat-minimax-m2-5-54c9462d7c` |
| `image-generation` | `image-01-live` | `image-01-live` | `image-generation` | `stable` | `none` | `none` | `not-selected` | `candidate requires separate product and style-control decision` | `no` | `verified` | `current` | `2026-07-14` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-minimax-intl-model-catalog-image-generation-image-01-live-86f51910d5` |

## Legacy Compatibility View

This derived table preserves the original column contract during migration. It is not the source of truth for provider lifecycle or selection. New integrations must use the Canonical Registry above.

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `MiniMax-M2.7` | `MiniMax M2.7` | `MiniMax-M2.7` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-03-18` | `2026-01-14` | `204800` | `unknown` | `204800` | `international` | `per-million-tokens` | `USD 0.3` | `USD 1.2` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` |
| `chat` | `MiniMax-M2.7-highspeed` | `MiniMax M2.7 Highspeed` | `MiniMax-M2.7-highspeed` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-03-18` | `2026-01-14` | `204800` | `unknown` | `204800` | `international` | `per-million-tokens` | `USD 0.6` | `USD 2.4` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` |
| `chat` | `MiniMax-M3` | `MiniMax M3` | `MiniMax-M3` | `active` | `not-selected` | `no` | `verified` | `candidate` | `2026-06-01` | `2026-01-14` | `1000000` | `unknown` | `524288` | `international` | `per-million-tokens` | `USD 0.30 <=512K` | `USD 1.20 <=512K` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` |
| `vision` | `MiniMax-M3` | `MiniMax M3` | `MiniMax-M3` | `active` | `not-selected` | `no` | `verified` | `candidate` | `2026-06-01` | `2026-01-14` | `1000000` | `unknown` | `524288` | `international` | `per-million-tokens` | `USD 0.30 <=512K` | `USD 1.20 <=512K` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` |
| `imaging` | `image-01` | `image-01` | `image-01` | `active` | `selected` | `yes` | `verified` | `candidate` | `2025-02-15` | `2026-01-14` | `n/a` | `n/a` | `n/a` | `international` | `per-image` | `n/a` | `USD 0.0035` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/image-generation-t2i` |
| `music` | `music-2.6` | `Music 2.6` | `music-2.6` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-01` | `2026-01-14` | `n/a` | `n/a` | `n/a` | `international` | `per-song` | `n/a` | `USD 0.15 per song/up-to-5-minutes` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/music-generation` |
| `chat` | `MiniMax-M2.5` | `MiniMax M2.5` | `MiniMax-M2.5` | `active` | `not-selected` | `no` | `verified` | `candidate` | `2026-02-01` | `2026-01-14` | `204800` | `unknown` | `204800` | `international` | `unknown` | `unknown` | `unknown` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` |
| `imaging` | `image-01-live` | `image-01-live` | `image-01-live` | `active` | `not-selected` | `no` | `verified` | `candidate` | `2025-02-15` | `2026-01-14` | `n/a` | `n/a` | `n/a` | `international` | `per-image` | `n/a` | `USD 0.0035` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://platform.minimax.io/docs/api-reference/image-generation-t2i` |

## Evidence

Evidence sets and field-level claims live in `../../_evidence/evidence.json`. Pricing details live in `pricing-matrix.md`; capability and endpoint details live in their exact surface/version matrices.
