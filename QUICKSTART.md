# Quickstart

This repository is a runtime-free skill pack for helping coding agents build LLM provider integration.

Current concrete provider coverage:

- Aliyun Bailian / DashScope

The shared structure is designed for more providers later.

## 1. Keep the full structure

Keep the folder structure intact:

```text
_shared/
skill-llm-aliyun/
```

Do not copy only `skill-llm-aliyun/SKILL.md`.

The Aliyun skill depends on the shared contracts in `_shared`.

## 2. Give your coding agent a clear task

Example prompt:

```text
Read this repository as a skill pack.

First read skill-llm-aliyun/SKILL.md.
Follow its read order.
Use _shared for request, response, error, progress, UI, model catalog, and capability rules.

Build a website settings page where users can enter their Aliyun Bailian / DashScope API key, select a verified model, test the connection, and enable only verified capabilities.

Do not guess model IDs.
Do not enable unknown capabilities.
Do not silently fallback to another model, key, or provider.
```

## 3. Follow the skill read order

The provider skill is the entry point:

```text
skill-llm-aliyun/SKILL.md
```

It points the agent to the shared rules and provider references, including:

```text
_shared/model-catalog-schema.md
_shared/capability-matrix-schema.md
_shared/request-envelope.md
_shared/response-envelope.md
_shared/error-contract.md
_shared/progress-contract.md
_shared/ui-binding.md
_shared/sync-policy.md
skill-llm-aliyun/references/model-catalog.md
skill-llm-aliyun/references/capability-matrix.md
skill-llm-aliyun/references/transport-*.md
```

## 4. Choose the request kind before coding

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

## 5. Build model selectors from the catalog

Use:

```text
skill-llm-aliyun/references/model-catalog.md
```

Only expose rows where:

```text
Catalog Status = active
Selection Status = selected
```

Important:

```text
UI Label = what users see
API Model = what the request sends
```

Do not submit the UI label as the model ID.

## 6. Gate every feature with the capability matrix

Use:

```text
skill-llm-aliyun/references/capability-matrix.md
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

## 7. Use the shared contracts

All provider calls should map into the shared contracts:

```text
_shared/request-envelope.md
_shared/response-envelope.md
_shared/error-contract.md
_shared/progress-contract.md
```

This keeps the app logic provider-neutral.

Example:

```text
Provider image URLs should become ImageOutputs.
Do not hide them inside TextContent.
```

## 8. Follow the UI rules

Use:

```text
_shared/ui-binding.md
```

Basic UI behavior:

- always show a model selector
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

## 9. Model sync must be explicit

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

## 10. Fail fast

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
- hide provider errors

If a required fact is missing, stop and report what is missing.
