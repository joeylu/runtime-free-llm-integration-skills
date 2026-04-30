# Aliyun Connection Profiles

Use this file when the host project defines named Aliyun Bailian / DashScope connection profiles.

This skill does not bundle active Aliyun profile rows yet because API key references and base URLs are project-owned.

## Rules

- Follow `../_shared/connection-profile-schema.md`.
- Store only secret references such as environment variable names. Do not store real API keys.
- Resolve `ConnectionProfileKey` before selecting the final model and API surface.
- Do not silently fall back from one profile, API key, or base URL to another.
- A profile may narrow allowed models, request kinds, API surfaces, or features.
- A profile must not expand a model capability from `unknown` or `unsupported` to usable.
- If a profile points to a gateway or OpenAI-compatible endpoint, verify that the endpoint supports the requested Aliyun API surface before wiring advanced fields.

## Local Profiles

No bundled Aliyun connection profile rows yet.

If a project needs Aliyun profiles, add rows using the shared schema and project-owned secret references.

Example:
Use `API Key Ref = ALIYUN_BUILD_API_KEY` as a reference name only. Do not put the key value in this file.
