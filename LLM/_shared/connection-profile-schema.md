# Shared Connection Profile Schema v2

A connection profile is a named, non-secret provider/region boundary such as `build`, `plan`, or `runtime`.

## Canonical Key

`Provider + Profile Key`

## Canonical Columns

| Column | Meaning |
| --- | --- |
| `Profile Key` | Stable request-facing key |
| `Display Name` | Human-readable label |
| `Provider` | Exact repository provider key, including region split when present |
| `Purpose` | `build`, `plan`, `runtime`, `eval`, `admin`, or another explicit purpose |
| `Profile Status` | `active`, `disabled`, or `template` |
| `Endpoint Kind` | `official`, `openai-compatible`, `provider-compatible`, `gateway`, or `custom` |
| `Base URL` | Exact non-secret base URL or template |
| `API Key Ref` | Secret reference name, never the secret value |
| `API Key Source` | `env`, `secret-manager`, `user-setting`, `credential-store`, or `external` |
| `Default Text Model` | Default exact model for `text-chat`, or `none` |
| `Default Multimodal Model` | Default exact model for `multimodal-chat`, or `none` |
| `Default Image Model` | Default exact model for `image-generation`, or `none` |
| `Default Music Model` | Default exact model for `music-generation`, or `none` |
| `Allowed Request Kinds` | Comma-separated canonical request kinds, or `none` for a disabled/reference-only profile |
| `Default Route Map` | Semicolon-separated `request-kind=surface@version` entries, or `none` when no route is enabled |
| `Allowed Surface Versions` | Comma-separated exact `surface@version` entries, or `none` when the profile is disabled |
| `Model Allowlist` | `catalog-selected` or comma-separated exact model IDs |
| `Capability Restrictions` | Profile rules that only narrow provider capabilities |
| `Billing Region` | Exact billing region used for pricing lookup |
| `Deployment Scope` | Exact provider deployment scope |
| `Serving Region` | Exact serving region |
| `Last Verified At` | Absolute review date or `unverified` |
| `Evidence Refs` | evidence-set IDs from `LLM/_evidence/evidence.json` |
| `Notes` | Non-normative explanation |

## Resolution Order

1. Resolve `ConnectionProfileKey`.
2. Verify profile status and secret reference availability.
3. Normalize the request kind.
4. Select a model allowed by the catalog and profile.
5. Select one exact `surface@version` allowed by the profile.
6. Resolve the final request URL.
7. Read the exact capability row.
8. Resolve the exact pricing scope.
9. Build and send the request.

## Rules

- A profile may narrow capabilities; it may never expand them.
- `Base URL` is not a complete request URL.
- Never fall back to another profile, credential, base URL, region, surface, version, or model without a new explicit selection.
- Custom/gateway profiles do not inherit official-provider parity unless separately verified.
- Secrets must not appear in skill files, URL templates, evidence, logs, or metadata.

## Legacy Compatibility

Provider files may retain the original 19-column table as a clearly labeled derived view. New integrations must use Canonical Profiles. Legacy request-kind names are normalized only once at the shared request boundary.
