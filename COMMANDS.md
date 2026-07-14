# Agent Commands

This file defines common natural-language commands for LLM agents using this repository.

These are not CLI commands, scripts, or executable program names. They are intent names that help an agent route user requests to the right repository workflow before acting.

## Routing Rules

- If the user asks to list current functions, available commands, help, or common workflows, read this file first and summarize the commands below.
- If the user enters a short command-like request such as `init`, `sync`, `implement`, or `audit`, try to match it to this file before inventing a new workflow.
- If a request matches more than one command, ask the user to choose instead of guessing.
- Commands in this file do not override provider `SKILL.md` hard rules, shared contracts, or fail-fast requirements.
- Update model metadata only for a `sync` request or an explicit verification request.
- Do not silently fall back between providers, regions, profiles, models, base URLs, request URLs, or API surfaces.

## Command Index

| Command | Common User Phrases | Purpose |
| --- | --- | --- |
| `list-commands` | `help`, `commands`, `list functions`, `available workflows`, `show commands` | List available agent workflows without executing them |
| `init` | `init`, `initialize`, `start integration`, `set up provider integration` | Prepare an LLM provider integration from this skill pack |
| `implement` | `implement`, `build`, `wire`, `integrate`, `apply to project` | Modify a host project to use the requested provider path |
| `sync` | `sync`, `latest`, `refresh`, `update models`, `latest models`, `re-verify` | Live-review official docs and update model/pricing/capability/request-URL data |
| `audit` | `audit`, `review`, `check`, `clean docs`, `verify consistency` | Review repository docs and skill structure for consistency |
| `add-provider` | `add provider`, `new provider`, `support another LLM provider` | Add a new provider skill using the existing shared contracts |
| `split-provider` | `split provider`, `separate regions`, `separate commercial entries`, `region separate` | Split one provider into separate regional or commercial provider skills |

## `list-commands`

Use when the user asks what this repo can do or asks to list common commands.

Read first:

```text
COMMANDS.md
```

Output:

- command name
- common phrases
- one-line purpose

Do not execute any command while listing commands.

## `init`

Use when the user wants to start an LLM provider integration.

Read first:

```text
README.md
QUICKSTART.md
COMMANDS.md
LLM/skill-llm-<provider>/SKILL.md
```

Required steps:

1. Identify provider, region, request kinds, host app surface, and whether the host project needs UI, backend calls, or both.
2. Choose the provider skill before resolving the requested model or connection profile.
3. Follow the provider `SKILL.md` read order.
4. Resolve the connection profile, request URL matrix, model catalog, pricing matrix, and capability matrix before proposing implementation.
5. Stop if provider, region, host app target, or requested capability is unclear.

Example:

```text
init Aliyun Bailian China Mainland chat + vision for a website settings page
```

## `implement`

Use when the user wants code or project files changed in a host project.

Read first:

```text
COMMANDS.md
LLM/skill-llm-<provider>/SKILL.md
LLM/_shared/request-envelope.md
LLM/_shared/response-envelope.md
LLM/_shared/error-contract.md
LLM/_shared/ui-binding.md
```

Required steps:

1. Confirm the request is implementation work, not model sync or prompt-only work.
2. Identify `RequestKind`, provider, region, `ConnectionProfileKey`, `ApiSurface`, `ApiVersion`, `EndpointKind`, `RouteKey`, `ResolvedBaseUrl`, `ResolvedRequestUrl`, and `API Model`.
3. Gate every option with `capability-matrix.md`.
4. Use `pricing-matrix.md` for billing or estimates.
5. Map requests, responses, errors, progress, and logging into shared contracts.
6. Stop before writing code if any required field is missing, unknown, unsupported, or region-mismatched.

Example:

```text
implement OpenAI chat and image generation settings UI using the documented model and surface rules
```

## `sync`

Use when the user explicitly asks for latest-model, pricing, capability, context-window, token-limit, or endpoint verification.

Read first:

```text
COMMANDS.md
LLM/_shared/sync-policy.md
LLM/skill-llm-<provider>/references/model-sync.md
```

Required steps:

1. Review official provider docs.
2. Update `model-catalog.md`, `pricing-matrix.md`, `request-urls.md`, and `capability-matrix.md` together when relevant.
3. Keep unverified fields as `unknown`.
4. Record the exact official source and absolute verification date on every changed verified route row.

Stop if official docs are inaccessible or a required field cannot be verified from official sources.

Example:

```text
sync Gemini model replacements and API changes from official documentation
```

## `audit`

Use when the user asks to review structure, clean docs, or check logical consistency.

Read first:

```text
COMMANDS.md
README.md
QUICKSTART.md
LLM/_shared/
LLM/skill-llm-*/SKILL.md
```

Required checks:

1. Verify provider folders match current supported providers.
2. Check that old provider names and stale paths are not referenced.
3. Check that each provider has required files: `SKILL.md`, `agents/openai.yaml`, and the expected `references/*.md`.
4. Check that profile API surfaces have matching `request-urls.md` rows.
5. Check that documented catalog rows have matching capability rows and pricing rows when pricing is published.
6. Check that logging fields match `LLM/_shared/logging-fields.md`.
7. Report structural and semantic inconsistencies as documentation findings; do not run or add repository-local validators, test harnesses, or project acceptance checks.

Example:

```text
audit this repo and make sure the docs are clean
```

## `add-provider`

Use when the user wants to add a new LLM provider.

Read first:

```text
COMMANDS.md
LLM/_shared/
LLM/skill-llm-openai/SKILL.md
LLM/skill-llm-deepseek/SKILL.md
LLM/skill-llm-gemini/SKILL.md
```

Required steps:

1. Choose a lowercase hyphenated provider skill name.
2. Create one provider folder under `LLM/skill-llm-<provider>/`.
3. Include `SKILL.md`, `agents/openai.yaml`, and provider references for connection profiles, request URLs, model catalog, pricing, capabilities, logging, sync, and transports.
4. Use shared schemas instead of cloning shared contracts.
5. Keep unknown capabilities blocked.

Stop if the provider's official docs, base URL, request URL shape, or pricing source cannot be identified.

Example:

```text
add-provider for ExampleAI direct-model chat and vision
```

## `split-provider`

Use when one vendor has separate regions, commercial entries, base URLs, request URLs, pricing, or capability surfaces that should not be treated as one provider.

Read first:

```text
COMMANDS.md
LLM/_shared/connection-profile-schema.md
LLM/_shared/request-url-matrix-schema.md
LLM/_shared/pricing-matrix-schema.md
LLM/skill-llm-<provider>/SKILL.md
```

Required steps:

1. Name each split provider explicitly, for example `aliyun-bailian-cn` and `aliyun-bailian-intl`.
2. Move region-specific base URLs, request URLs, pricing, model catalogs, and capability rows into the matching provider folder.
3. Remove or deprecate the old combined provider folder.
4. Update `README.md`, `QUICKSTART.md`, provider `SKILL.md` descriptions, and agent metadata.
5. Check that no old combined provider path remains referenced.

Example:

```text
split Aliyun Bailian into China Mainland and International providers
```
