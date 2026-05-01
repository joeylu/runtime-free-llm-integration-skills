# Shared Connection Profile Schema

Use this file to keep provider connection profiles shaped the same way.

A connection profile is one named provider connection configuration, such as `build` or `plan`.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Profile Key` | stable profile key used by requests, such as `build` or `plan` |
| `Display Name` | short human-readable profile name |
| `Provider` | provider identifier such as `openai`, `aliyun-bailian-cn`, or `aliyun-bailian-intl` |
| `Purpose` | intended usage such as `build`, `plan`, `runtime`, `eval`, or `admin` |
| `Profile Status` | `active`, `disabled`, or `template` |
| `Endpoint Kind` | `official`, `openai-compatible`, `provider-compatible`, `gateway`, or `custom` |
| `Base URL` | exact base URL, SDK base URL, or a non-secret config ref |
| `API Key Ref` | secret reference name, never the secret value |
| `API Key Source` | `env`, `secret-manager`, `user-setting`, `credential-store`, or `external` |
| `Default Chat Model` | default `API Model` for `chat`, or `none` |
| `Default Vision Model` | default `API Model` for `vision`, or `none` |
| `Default Imaging Model` | default `API Model` for `imaging`, or `none` |
| `Default Music Model` | default `API Model` for `music`, or `none` |
| `Allowed Request Kinds` | comma-separated request kinds allowed by this profile |
| `Allowed API Surfaces` | provider surfaces allowed by this profile, such as `responses` or `image-api` |
| `Model Allowlist` | `catalog-selected` or comma-separated exact model IDs |
| `Capability Restrictions` | profile-level restrictions that can only narrow capabilities |
| `Last Verified At` | absolute verification date or `unverified` |
| `Notes` | short explanation |

## Rules

- Do not store real API keys, tokens, or refresh secrets in skill files.
- Resolve `ConnectionProfileKey` before selecting the final model.
- A profile can restrict request kinds, models, API surfaces, or features.
- A profile must not expand provider capabilities beyond the provider `capability-matrix.md`.
- A profile's `Base URL` is not enough to identify the HTTP request. Resolve the final request URL from the provider `request-urls.md` before sending.
- If the requested profile is missing, disabled, or lacks a required secret reference, stop with `config_error`.
- Do not silently fall back from one profile to another.
- Do not silently fall back from one base URL to another.
- Do not silently rewrite one request URL template to another.
- If `Endpoint Kind` is not the official provider endpoint, treat provider compatibility as a profile property that must be verified for the requested API surface.
- If a custom or gateway endpoint does not clearly support a requested field, stop instead of assuming official-provider parity.

## Example

`Profile Key = build` may use `API Key Ref = OPENAI_BUILD_API_KEY`, while `Profile Key = plan` may use `API Key Ref = OPENAI_PLAN_API_KEY`.

They can point to different base URLs, but both must still use model IDs and capabilities verified by the provider skill unless the profile explicitly documents narrower support.
