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
| `Base URL` | exact base URL, SDK base URL, or non-secret configuration reference |
| `API Key Ref` | secret reference name, never the secret value |
| `API Key Source` | `env`, `secret-manager`, `user-setting`, `credential-store`, or `external` |
| `Request Kinds` | request kinds exposed by this endpoint configuration |
| `API Surfaces` | API surfaces exposed by this endpoint configuration |
| `Capability Restrictions` | endpoint- or credential-specific restrictions |
| `Last Verified At` | absolute verification date or `unverified` |
| `Notes` | short connection note |

## Rules

- Store secret references only.
- Resolve `ConnectionProfileKey` before the final request URL.
- Resolve the model from the request and the provider catalog, not from the connection profile.
- A profile may narrow endpoint capabilities but cannot expand a model capability.
- Stop on a missing, disabled, unresolved, or incompatible profile.
- Never silently fall back to another profile, base URL, region, or API surface.
- Re-verify advanced fields when a profile points to a gateway or custom endpoint.
