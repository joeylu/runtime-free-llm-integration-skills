# runtime-free-llm-integration-skills

This repository gives coding agents a reliable set of rules for building direct LLM provider integrations.

It is not an SDK, proxy, gateway, or runtime service. Your application still calls each provider directly. The skill pack simply helps the agent choose the right model, endpoint, API surface, capability, role, and price without guessing.

## Why use it?

LLM APIs often look similar, but the details are not interchangeable. A model may exist in one region but not another, support tools on one API surface but not another, or use a different price and endpoint.

This pack keeps those boundaries explicit:

- unknown stays unknown;
- unsupported features stay disabled;
- failed requests stay failed;
- no silent model, region, endpoint, or API fallback.

## Supported providers

- OpenAI API
- Gemini Developer API
- DeepSeek API
- Aliyun Bailian / Model Studio China Mainland
- Alibaba Cloud Model Studio International
- MiniMax China Mainland
- MiniMax International

China Mainland and International services are separate providers in this repository. Their keys, endpoints, models, and prices must not be mixed.

## How to use it

1. Keep the whole `LLM/` folder together.
2. Pick one provider and region.
3. Ask your coding agent to read `COMMANDS.md` and that provider's `SKILL.md`.
4. Describe what you want to build.

For example:

```text
Read COMMANDS.md and LLM/skill-llm-openai/SKILL.md.
Build a settings page for OpenAI text and image generation.
Use only selected models and verified capabilities. Do not silently fall back.
```

For a model-data refresh:

```text
Sync the Aliyun Bailian China Mainland skill from official documentation,
then audit the repository and run the validator.
```

See [QUICKSTART.md](QUICKSTART.md) for a few more ready-to-use prompts.

## What's inside?

```text
LLM/_shared/                 shared request, response, error, and schema rules
LLM/_evidence/               reviewed official-source evidence
LLM/skill-llm-<provider>/    provider-specific rules and reference tables
tools/validate_repo.py       local consistency checker
```

Each provider skill includes its own model catalog, connection profiles, request URLs, capabilities, roles, pricing, and transport notes.

The catalog is a curated allowlist, not a complete live registry. Finding a newer model does not automatically make it selected or default.

## A few useful terms

New integrations use request kinds such as:

- `text-chat`
- `multimodal-chat`
- `image-generation`
- `music-generation`

Older names such as `chat`, `vision`, `imaging`, and `music` are kept only for compatibility at the input boundary.

## Validation

After changing repository data, run:

```bash
python tools/validate_repo.py
```

This checks the local files, evidence links, tables, routes, and cross-file rules. It does not replace live API testing or a fresh review of provider documentation.

For the details behind this update, see [CHANGELOG.md](CHANGELOG.md), [MODEL-MIGRATION-2026-07-14.md](MODEL-MIGRATION-2026-07-14.md), and [VALIDATION-2026-07-14.md](VALIDATION-2026-07-14.md).
