# Quickstart

This repository is a runtime-free skill pack for helping coding agents build LLM provider integration.

Current concrete provider coverage:

- OpenAI API
- Aliyun Bailian / DashScope
- DeepSeek API
- Gemini Developer API

The shared structure is designed for more providers later.

## 1. Keep the full structure

Keep the folder structure intact:

```text
LLM/_shared/
LLM/skill-llm-openai/
LLM/skill-llm-aliyun/
LLM/skill-llm-deepseek/
LLM/skill-llm-gemini/
```

Do not copy only one provider `SKILL.md`.

Each provider skill depends on the shared contracts in `LLM/_shared`.

## 2. Give your coding agent a clear task

Example prompt:

```text
Read this repository as a skill pack.

First read the provider entry point, such as LLM/skill-llm-openai/SKILL.md, LLM/skill-llm-aliyun/SKILL.md, LLM/skill-llm-deepseek/SKILL.md, or LLM/skill-llm-gemini/SKILL.md.
Follow its read order.
Use LLM/_shared for request, response, error, progress, UI, model catalog, pricing matrix, and capability rules.

Build a website settings page where users can enter their OpenAI, Aliyun Bailian / DashScope, DeepSeek, or Gemini API key, select a verified model, test the connection, and enable only verified capabilities.

Do not guess model IDs.
Do not enable unknown capabilities.
Do not silently fallback to another model, key, or provider.
```

## 3. Follow the skill read order

The provider skill is the entry point:

```text
LLM/skill-llm-openai/SKILL.md
LLM/skill-llm-aliyun/SKILL.md
LLM/skill-llm-deepseek/SKILL.md
LLM/skill-llm-gemini/SKILL.md
```

It points the agent to the shared rules and provider references, including:

```text
LLM/_shared/model-catalog-schema.md
LLM/_shared/pricing-matrix-schema.md
LLM/_shared/capability-matrix-schema.md
LLM/_shared/connection-profile-schema.md
LLM/_shared/request-envelope.md
LLM/_shared/response-envelope.md
LLM/_shared/error-contract.md
LLM/_shared/progress-contract.md
LLM/_shared/ui-binding.md
LLM/_shared/sync-policy.md
LLM/skill-llm-aliyun/references/connection-profiles.md
LLM/skill-llm-aliyun/references/model-catalog.md
LLM/skill-llm-aliyun/references/pricing-matrix.md
LLM/skill-llm-aliyun/references/capability-matrix.md
LLM/skill-llm-aliyun/references/transport-*.md
LLM/skill-llm-openai/references/connection-profiles.md
LLM/skill-llm-openai/references/model-catalog.md
LLM/skill-llm-openai/references/pricing-matrix.md
LLM/skill-llm-openai/references/capability-matrix.md
LLM/skill-llm-openai/references/transport-*.md
LLM/skill-llm-deepseek/references/connection-profiles.md
LLM/skill-llm-deepseek/references/model-catalog.md
LLM/skill-llm-deepseek/references/pricing-matrix.md
LLM/skill-llm-deepseek/references/capability-matrix.md
LLM/skill-llm-deepseek/references/transport-*.md
LLM/skill-llm-gemini/references/connection-profiles.md
LLM/skill-llm-gemini/references/model-catalog.md
LLM/skill-llm-gemini/references/pricing-matrix.md
LLM/skill-llm-gemini/references/capability-matrix.md
LLM/skill-llm-gemini/references/transport-*.md
```

## 4. Resolve the connection profile

If a provider has multiple profiles, resolve the profile before model selection.

Example:

```text
ConnectionProfileKey = build uses OPENAI_BUILD_API_KEY or GEMINI_BUILD_API_KEY.
ConnectionProfileKey = plan uses OPENAI_PLAN_API_KEY or GEMINI_PLAN_API_KEY.
```

Do not silently switch profiles, API keys, or base URLs.

## 5. Choose the request kind before coding

Before writing implementation code, the agent must identify the request kind.

| Request kind | Meaning |
|---|---|
| `chat` | text conversation |
| `vision` | image understanding |
| `imaging` | image generation or image edit job |
| `music` | music or audio generation job |

Example:

```text
If the user wants to understand an uploaded image, use vision.
Do not fake it as chat.
```

## 6. Build model selectors from the catalog

Use:

```text
LLM/skill-llm-<provider>/references/model-catalog.md
```

Only expose rows where:

```text
Catalog Status = active
Selection Status = selected
```

Important:

```text
API Model = what users see
API Model = what the request sends
```

Do not put prices or aliases into model option labels.

## 7. Use the pricing matrix for billing

Use:

```text
LLM/skill-llm-<provider>/references/pricing-matrix.md
```

Use it for any billing, price display, or estimate UI.

Do not reconstruct region, currency, context band, or unit price from `model-catalog.md` notes.

## 8. Gate every feature with the capability matrix

Use:

```text
LLM/skill-llm-<provider>/references/capability-matrix.md
```

If a requested feature is:

```text
unknown
unsupported
missing
```

stop before implementation or request sending.

Do not guess.

Example:

```text
If Supports Stream = unknown, do not add a stream toggle.
```

## 9. Use the shared contracts

All provider calls should map into the shared contracts:

```text
LLM/_shared/request-envelope.md
LLM/_shared/response-envelope.md
LLM/_shared/error-contract.md
LLM/_shared/progress-contract.md
```

This keeps the app logic provider-neutral.

Example:

```text
Provider image URLs should become ImageOutputs.
Do not hide them inside TextContent.
```

## 10. Follow the UI rules

Use:

```text
LLM/_shared/ui-binding.md
```

Basic UI behavior:

- always show a model selector
- show a connection profile selector when multiple active profiles exist
- show stream only when verified
- show thinking only when supported
- show image inputs only for valid vision or verified imaging flows
- show errors using the shared error contract
- do not fake progress percentages

For debug or admin UI, prefer disabled controls with a clear reason.

Example:

```text
Stream disabled: Supports Stream is unknown for kimi-k2.6.
```

## 11. Model sync must be explicit

Do not sync models automatically.

Only sync when the user explicitly asks for:

```text
latest models
sync
refresh
official verification
```

Before syncing, confirm a recency boundary.

Default:

```text
6 months
```

Then convert it into an absolute cutoff date.

If official docs do not clearly confirm a field, keep it as `unknown`.

Model metadata collection, including context window, max input tokens, max output tokens, pricing, and capabilities, must be done live by the LLM from official docs during each sync.

Do not use scripts, scrapers, SDK enum dumps, generated parsers, or automated catalog generators to collect sync values.

## 12. Fail fast

The most important rule:

```text
Unknown means unknown.
Unsupported means unsupported.
Failed means failed.
```

Do not:

- guess model IDs
- guess capabilities
- silently drop unsupported parameters
- silently switch request kinds
- silently fallback to another model
- silently fallback to another API key
- silently fallback to another connection profile or base URL
- hide provider errors

If a required fact is missing, stop and report what is missing.
