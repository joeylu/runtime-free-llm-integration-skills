# DeepSeek Model Catalog

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
| `text-chat` | `deepseek-v4-flash` | `DeepSeek V4 Flash` | `chat-completions` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `1M` | `unknown` | `unknown` | `unknown` | `384K` | `unknown` | `unknown` | `provider-unspecified` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-deepseek-model-catalog-text-chat-deepseek-v4-flash-3aa0f30ad4` |
| `text-chat` | `deepseek-v4-pro` | `DeepSeek V4 Pro` | `chat-completions` | `stable` | `none` | `none` | `selected` | `selected higher-capability alternative` | `no` | `verified` | `current` | `2026-07-14` | `1M` | `unknown` | `unknown` | `unknown` | `384K` | `unknown` | `unknown` | `provider-unspecified` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-deepseek-model-catalog-text-chat-deepseek-v4-pro-fc2d94853a` |
| `text-chat` | `deepseek-v3.2-exp` | `DeepSeek V3.2 Exp` | `chat-completions` | `unknown` | `none` | `none` | `not-selected` | `historical model confirmed in changelog; current availability not established by current model page` | `no` | `verified` | `current` | `2026-07-14` | `128K` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `provider-unspecified` | `no` | `none` | `n/a` | `n/a` | `none` | `evset-deepseek-model-catalog-text-chat-deepseek-v3-2-exp-ac518ed250` |
| `text-chat` | `deepseek-chat` | `deepseek-chat compatibility alias` | `chat-completions` | `scheduled-deprecated` | `2026-07-24T15:59:00Z` | `none` | `not-selected` | `temporary compatibility alias; provider announced shutdown` | `no` | `verified` | `current` | `2026-07-14` | `1M` | `unknown` | `unknown` | `unknown` | `384K` | `unknown` | `unknown` | `provider-unspecified` | `yes` | `deepseek-v4-flash` | `non-thinking` | `2026-07-14` | `deepseek-v4-flash` | `evset-deepseek-model-catalog-text-chat-deepseek-chat-bba01d19c3` |
| `text-chat` | `deepseek-reasoner` | `deepseek-reasoner compatibility alias` | `chat-completions` | `scheduled-deprecated` | `2026-07-24T15:59:00Z` | `none` | `not-selected` | `temporary compatibility alias; provider announced shutdown` | `no` | `verified` | `current` | `2026-07-14` | `1M` | `unknown` | `unknown` | `unknown` | `384K` | `unknown` | `unknown` | `provider-unspecified` | `yes` | `deepseek-v4-flash` | `thinking` | `2026-07-14` | `deepseek-v4-flash` | `evset-deepseek-model-catalog-text-chat-deepseek-reasoner-f37358ec4a` |

## Legacy Compatibility View

This derived table preserves the original column contract during migration. It is not the source of truth for provider lifecycle or selection. New integrations must use the Canonical Registry above.

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `deepseek-v4-flash` | `DeepSeek V4 Flash` | `deepseek-v4-flash` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-24` | `2026-01-14` | `unknown` | `unknown` | `unknown` | `global` | `per-million-tokens` | `cache hit USD 0.0028; cache miss USD 0.14` | `USD 0.28` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing/` |
| `chat` | `deepseek-v4-pro` | `DeepSeek V4 Pro` | `deepseek-v4-pro` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-24` | `2026-01-14` | `unknown` | `unknown` | `unknown` | `global` | `per-million-tokens` | `cache hit USD 0.003625; cache miss USD 0.435` | `USD 0.87` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing/` |
| `chat` | `deepseek-v3.2-exp` | `DeepSeek V3.2 Exp` | `deepseek-v3.2-exp` | `deprecated` | `not-selected` | `no` | `verified` | `candidate` | `2025-09-29` | `2026-01-14` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://api-docs.deepseek.com/updates/` |
| `chat` | `deepseek-chat` | `deepseek-chat compatibility alias` | `deepseek-chat` | `deprecated` | `not-selected` | `no` | `verified` | `candidate` | `2026-04-24` | `2026-01-14` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://api-docs.deepseek.com/updates/` |
| `chat` | `deepseek-reasoner` | `deepseek-reasoner compatibility alias` | `deepseek-reasoner` | `deprecated` | `not-selected` | `no` | `verified` | `candidate` | `2026-04-24` | `2026-01-14` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://api-docs.deepseek.com/updates/` |

## Evidence

Evidence sets and field-level claims live in `../../_evidence/evidence.json`. Pricing details live in `pricing-matrix.md`; capability and endpoint details live in their exact surface/version matrices.
