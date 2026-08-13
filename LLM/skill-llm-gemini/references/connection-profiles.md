# Gemini Connection Profiles

| Profile Key | Display Name | Provider | Purpose | Profile Status | Endpoint Kind | Base URL | API Key Ref | API Key Source | Request Kinds | API Surfaces | Capability Restrictions | Last Verified At | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `gemini-developer-api` | `Gemini Developer API` | `gemini` | `runtime` | `verified` | `official` | `https://generativelanguage.googleapis.com` | `GEMINI_API_KEY` | `env` | `chat,vision,imaging` | `interactions,generate-content,stream-generate-content` | `Developer API only; Vertex AI is excluded.` | 2026-08-06 | `Send x-goog-api-key; do not place secrets in logs.` |
