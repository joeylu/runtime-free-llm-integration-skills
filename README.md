# runtime-free-llm-integration-skills

Logic-only skills for agents that reason about direct LLM API integrations. Each provider skill records exact model IDs, endpoints, request fields, capabilities, limits, response mapping, pricing references, and provider-specific contract constraints.

## Scope

When a project uses a documented model, the agent must follow the provider's official API contract and the exact model-and-surface rules in this repository. Model choice belongs to the host project or the user.

Core behavior:

- use exact provider model IDs, regions, API surfaces, API versions, endpoint kinds, and request URLs;
- resolve a feature against the exact full route key before proposing or applying it;
- keep unsupported and unknown behavior explicit;
- never silently switch provider, region, model, credential, URL, API surface, API version, or endpoint kind;
- normalize provider request, response, error, progress, and logging semantics through the shared contracts.

## Logic-only boundary

This repository is a normative documentation layer. It defines decisions, constraints, mappings, and fail-fast conditions for an agent, but it does not perform project development or project acceptance work.

It intentionally does not include:

- executable validators or repository-local checking utilities;
- repository linters, test harnesses, regression fixtures, or CI jobs;
- URL reachability checkers or automated evidence verification;
- installers, project scaffolding, code generators, or deployment scripts;
- claims that a host project has been compiled, tested, integrated, or accepted.

Terms such as `validation_error`, JSON Schema validation, strict tool schema, and fail-fast gating describe provider or contract semantics. They do not imply that this repository ships an executable validation system.

A host agent may use these documents while working in another project, but any implementation, testing, installation, deployment, and acceptance process belongs to that host project and remains outside this repository's scope.

## Providers

- OpenAI API
- Aliyun Bailian / DashScope China Mainland
- Aliyun Bailian / DashScope International
- DeepSeek API
- Gemini Developer API
- MiniMax China Mainland API
- MiniMax International API
- ElevenLabs API

Regional skills remain separate because base URLs, availability, pricing, and behavior can differ.

## Model Updates

1. When a documented model has a clear newer replacement, replace the old model and update its catalog, capability, pricing, URL, transport, and example references together.
2. When a new model has no documented predecessor in this repository, ask the user before adding it.
3. For providers with regional skills, verify the replacement independently in each region during the same update.
4. Keep old identifiers only in a dated migration note.

See `LLM/_shared/sync-policy.md`.

## Structure

```text
LLM/_shared/
router/skill-llm-router/
LLM/skill-llm-openai/
LLM/skill-llm-aliyun-bailian-cn/
LLM/skill-llm-aliyun-bailian-intl/
LLM/skill-llm-deepseek/
LLM/skill-llm-gemini/
LLM/skill-llm-minimax-cn/
LLM/skill-llm-minimax-intl/
LLM/skill-llm-elevenlabs/
```

Each provider skill contains connection profiles, request URLs, a maintained model catalog, capability and pricing matrices, transport rules, examples, logging rules, and update sources.

## Host discovery and distribution

Skill discovery, copying, linking, plugin packaging, installation, and workspace policy are responsibilities of the host agent environment. This repository defines no installer and assumes no specific installation workflow.

Provider skills are explicit-only. The router skill is the sole logical entry point that may be configured for implicit routing. A host environment must preserve that invocation boundary when it distributes or registers these skills.

## Review model

Review this repository as documentation:

- confirm that wording is unambiguous and that shared and provider-specific boundaries do not conflict;
- compare model, endpoint, capability, pricing, and example claims with official provider documentation;
- preserve `unknown` when official evidence is unavailable;
- record official sources and absolute review dates on verified data rows;
- report inconsistencies as documentation findings rather than treating the repository as an executable test suite.
