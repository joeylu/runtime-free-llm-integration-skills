# Evidence Manifest Schema v2

The canonical manifest is `LLM/_evidence/evidence.json`.

The manifest separates compact row references from field-level claims:

- a table row references one or more `evidence_set_id` values in `Evidence Refs`;
- each evidence set identifies one exact repository record and lists its `claim_ids`;
- each claim covers exactly one canonical field and one reviewed value.

This keeps Markdown tables readable without collapsing many facts into one unverifiable record claim.

## Top-Level Shape

| Field | Meaning |
| --- | --- |
| `schema_version` | Must be `2` |
| `generated_at` | Manifest review/build date |
| `coverage_mode` | Repository coverage mode |
| `evidence_sets` | Row-to-claim mappings |
| `claims` | Field-level evidence claims |

## Evidence Set

| Field | Meaning |
| --- | --- |
| `evidence_set_id` | Stable unique row evidence ID |
| `provider` | Repository provider key |
| `document_path` | Repository-relative canonical document path |
| `record_key` | Exact canonical table key as an object |
| `claim_ids` | Non-empty list of field-level claim IDs |

An evidence set must match exactly one canonical table row. It must not combine rows from different providers, documents, surfaces, versions, price scopes, or models.

## Field Claim

| Field | Meaning |
| --- | --- |
| `claim_id` | Stable unique ID |
| `provider` | Repository provider key |
| `document_path` | Repository-relative document containing the reviewed value |
| `record_key` | Exact canonical table key |
| `model` | Exact model ID or `n/a` |
| `request_kind` | Canonical request kind or `n/a` |
| `surface` | Exact API surface or `n/a` |
| `api_version` | Exact version or `n/a` |
| `field` | Exactly one canonical factual field |
| `value` | Reviewed scalar value for that field |
| `source_url` | Official HTTPS URL |
| `source_type` | `endpoint-reference`, `model-card`, `pricing`, `lifecycle`, `release-notes`, `example`, `official-index`, or `derived` |
| `source_locator` | Heading, parameter, table row, model entry, or another reproducible locator |
| `verified_at` | Review date |
| `effective_at` | Official fact start date/time or `unknown` |
| `expires_at` | Official end date/time, `none`, or `unknown` |
| `reviewer` | Review actor/version |
| `conflict_state` | `none`, `open`, or `resolved` |
| `depends_on` | Claim IDs required to reproduce a derived value |
| `derivation` | `none` or a deterministic derivation description |
| `notes` | Optional non-normative explanation |

## Rules

- A claim may not use a record object or a multi-field value. `field` and `value` are scalar and field-specific.
- A URL alone is not evidence; include a precise locator and reviewed value.
- `source_type = derived` requires non-empty `depends_on` and a deterministic `derivation`.
- A derived claim may only depend on existing claims from the same provider and must not hide a provider-unit assumption.
- Every table evidence reference must resolve to an evidence set, and every evidence set claim must resolve to a field claim.
- The field claims in a set must reproduce the corresponding externally sourced values in the table row.
- Open conflicts fail closed. A `resolved` conflict must retain the resolution note and the evidence used.
- Repository validation checks manifest shape, official-host allowlists, references, dates, dependency graphs, and cross-file consistency. It does not re-fetch remote pages; official synchronization is a separate reviewed workflow.
