# OpenAI Model Catalog

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
| `text-chat` | `gpt-5.6-sol` | `GPT-5.6 Sol` | `responses` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `1,050,000` | `1050000` | `unknown` | `unknown` | `128,000` | `128000` | `unknown` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-openai-model-catalog-text-chat-gpt-5-6-sol-f573efdecf` |
| `text-chat` | `gpt-5.6-terra` | `GPT-5.6 Terra` | `responses` | `stable` | `none` | `none` | `selected` | `selected cost/quality alternative` | `no` | `verified` | `current` | `2026-07-14` | `1,050,000` | `1050000` | `unknown` | `unknown` | `128,000` | `128000` | `unknown` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-openai-model-catalog-text-chat-gpt-5-6-terra-26f0f6fffd` |
| `text-chat` | `gpt-5.6-luna` | `GPT-5.6 Luna` | `responses` | `stable` | `none` | `none` | `selected` | `selected high-volume alternative` | `no` | `verified` | `current` | `2026-07-14` | `1,050,000` | `1050000` | `unknown` | `unknown` | `128,000` | `128000` | `unknown` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-openai-model-catalog-text-chat-gpt-5-6-luna-a9964eb864` |
| `multimodal-chat` | `gpt-5.6-sol` | `GPT-5.6 Sol` | `responses` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `1,050,000` | `1050000` | `unknown` | `unknown` | `128,000` | `128000` | `unknown` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-openai-model-catalog-multimodal-chat-gpt-5-6-sol-d543afcbdc` |
| `multimodal-chat` | `gpt-5.6-terra` | `GPT-5.6 Terra` | `responses` | `stable` | `none` | `none` | `selected` | `selected cost/quality alternative` | `no` | `verified` | `current` | `2026-07-14` | `1,050,000` | `1050000` | `unknown` | `unknown` | `128,000` | `128000` | `unknown` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-openai-model-catalog-multimodal-chat-gpt-5-6-terra-76d0dd153e` |
| `multimodal-chat` | `gpt-5.6-luna` | `GPT-5.6 Luna` | `responses` | `stable` | `none` | `none` | `selected` | `selected high-volume alternative` | `no` | `verified` | `current` | `2026-07-14` | `1,050,000` | `1050000` | `unknown` | `unknown` | `128,000` | `128000` | `unknown` | `exact-integer` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-openai-model-catalog-multimodal-chat-gpt-5-6-luna-26a4bfa364` |
| `image-generation` | `gpt-image-2` | `GPT Image 2` | `image-api-generations` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-openai-model-catalog-image-generation-gpt-image-2-a63a82cc14` |

## Legacy Compatibility View

This derived table preserves the original column contract during migration. It is not the source of truth for provider lifecycle or selection. New integrations must use the Canonical Registry above.

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `gpt-5.6-sol` | `GPT-5.6 Sol` | `gpt-5.6-sol` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-07-09` | `2026-01-14` | `1050000` | `unknown` | `128000` | `global` | `per-million-tokens` | `USD 5.00` | `USD 30.00` | `Short-context compatibility summary; use pricing-matrix.md for long-context and cache bands` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-sol` |
| `chat` | `gpt-5.6-terra` | `GPT-5.6 Terra` | `gpt-5.6-terra` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-07-09` | `2026-01-14` | `1050000` | `unknown` | `128000` | `global` | `per-million-tokens` | `USD 2.50` | `USD 15.00` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-terra` |
| `chat` | `gpt-5.6-luna` | `GPT-5.6 Luna` | `gpt-5.6-luna` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-07-09` | `2026-01-14` | `1050000` | `unknown` | `128000` | `global` | `per-million-tokens` | `USD 1.00` | `USD 6.00` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-luna` |
| `vision` | `gpt-5.6-sol` | `GPT-5.6 Sol` | `gpt-5.6-sol` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-07-09` | `2026-01-14` | `1050000` | `unknown` | `128000` | `global` | `per-million-tokens` | `USD 5.00` | `USD 30.00` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-sol` |
| `vision` | `gpt-5.6-terra` | `GPT-5.6 Terra` | `gpt-5.6-terra` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-07-09` | `2026-01-14` | `1050000` | `unknown` | `128000` | `global` | `per-million-tokens` | `USD 2.50` | `USD 15.00` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-terra` |
| `vision` | `gpt-5.6-luna` | `GPT-5.6 Luna` | `gpt-5.6-luna` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-07-09` | `2026-01-14` | `1050000` | `unknown` | `128000` | `global` | `per-million-tokens` | `USD 1.00` | `USD 6.00` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-5.6-luna` |
| `imaging` | `gpt-image-2` | `GPT Image 2` | `gpt-image-2` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-21` | `2026-01-14` | `n/a` | `n/a` | `n/a` | `global` | `per-million-tokens` | `text USD 5.00; image USD 8.00` | `image USD 30.00` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://developers.openai.com/api/docs/models/gpt-image-2` |

## Evidence

Evidence sets and field-level claims live in `../../_evidence/evidence.json`. Pricing details live in `pricing-matrix.md`; capability and endpoint details live in their exact surface/version matrices.
