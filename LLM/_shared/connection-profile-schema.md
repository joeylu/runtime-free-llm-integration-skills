# Shared Connection Profile Schema

A connection profile supplies endpoint and credential references for one provider connection. The request supplies the model.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Profile Key` | stable request-facing profile key |
| `Display Name` | short human-readable name |
| `Provider` | provider identifier |
| `Purpose` | intended connection purpose such as `build`, `plan`, or `runtime` |
| `Profile Status` | `active`, `disabled`, or `template` |
| `Endpoint Kind` | `official`, `openai-compatible`, `provider-compatible`, `gateway`, or `custom` |
| `Base URL` | exact base URL, SDK base URL, non-secret configuration reference, or URL template containing declared non-secret placeholders |
| `API Key Ref` | secret reference name, never the secret value |
| `API Key Source` | `env`, `secret-manager`, `user-setting`, `credential-store`, or `external` |
| `Request Kinds` | request kinds exposed by this endpoint configuration |
| `API Surfaces` | API surfaces exposed by this endpoint configuration |
| `Capability Restrictions` | endpoint- or credential-specific restrictions |
| `Last Verified At` | absolute verification date or `unverified` |
| `Notes` | short connection note |

## Optional Placeholder Columns

Use these columns only when `Base URL` contains placeholders such as `{WorkspaceId}`.

| Column | Meaning |
| --- | --- |
| `Non-Secret Config Refs` | stable references used to resolve URL placeholders; never actual user values |
| `Non-Secret Config Sources` | allowed sources such as `env`, `user-setting`, `config-file`, or `external` |
| `Placeholder Bindings` | exact mapping from every URL placeholder to a config reference, or `n/a` |

## Rules

- Store secret references only; never store secret values.
- Resolve `ConnectionProfileKey` before the final request URL.
- Resolve the model from the request and the provider catalog, not from the connection profile.
- A profile may narrow endpoint capabilities but cannot expand a model capability.
- Stop on a missing, disabled, unresolved, or incompatible profile.
- Every placeholder in `Base URL` must have an explicit provider-specific configuration reference, allowed source, value contract, and binding rule.
- An unresolved placeholder is `config_error`. Never guess a value, substitute an empty string, or silently select another profile.
- Non-secret endpoint identifiers such as workspace IDs are configuration, not credentials; keep them separate from API keys.
- Never silently fall back to another profile, base URL, region, API surface, credential, or billing plan.
- Re-verify advanced fields when a profile points to a gateway or custom endpoint.
