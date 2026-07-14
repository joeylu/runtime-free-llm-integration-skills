# Aliyun Bailian International / Singapore Model Catalog

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
| `text-chat` | `qwen3.7-max` | `Qwen 3.7 Max` | `responses` | `stable` | `none` | `none` | `selected` | `curated primary or alternative` | `yes` | `verified` | `current` | `2026-07-14` | `1M` | `1000000` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `decimal` | `yes` | `qwen3.7-max-2026-05-20` | `provider-default` | `2026-07-14` | `production deployments should consider a fixed snapshot` | `evset-aliyun-bailian-intl-model-catalog-text-chat-qwen3-7-max-b45be0a631` |
| `text-chat` | `qwen3.6-max-preview` | `Qwen 3.6 Max Preview` | `chat-completions` | `scheduled-deprecated` | `2026-10-10T00:00:00` | `none` | `not-selected` | `provider scheduled deprecation; migrate before deadline` | `no` | `verified` | `current` | `2026-07-14` | `256K` | `256000` | `unknown` | `unknown` | `65,536` | `65536` | `unknown` | `decimal` | `no` | `none` | `n/a` | `n/a` | `qwen3.7-max` | `evset-aliyun-bailian-intl-model-catalog-text-chat-qwen3-6-max-preview-14192161f4` |

## Legacy Compatibility View

This derived table preserves the original column contract during migration. It is not the source of truth for provider lifecycle or selection. New integrations must use the Canonical Registry above.

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.7-max` | `Qwen 3.7 Max` | `qwen3.7-max` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-05-21` | `2026-01-14` | `1000000` | `unknown` | `unknown` | `singapore` | `per-million-tokens` | `USD 2.50` | `USD 7.50` | `Singapore serving region; International deployment scope; use pricing-matrix.md for exact scope and current discount status` | `2026-07-14` | `https://www.alibabacloud.com/help/en/model-studio/model-pricing` |
| `chat` | `qwen3.6-max-preview` | `Qwen 3.6 Max Preview` | `qwen3.6-max-preview` | `deprecated` | `not-selected` | `no` | `verified` | `candidate` | `2026-04-20` | `2026-01-14` | `256000` | `unknown` | `65536` | `singapore` | `per-million-tokens` | `USD 1.30 <=128K; USD 2.00 >128K` | `USD 7.80 <=128K; USD 12.00 >128K` | `Use pricing-matrix.md; compatibility summary only` | `2026-07-14` | `https://www.alibabacloud.com/help/en/model-studio/model-depreciation` |

## Evidence

Evidence sets and field-level claims live in `../../_evidence/evidence.json`. Pricing details live in `pricing-matrix.md`; capability and endpoint details live in their exact surface/version matrices.
