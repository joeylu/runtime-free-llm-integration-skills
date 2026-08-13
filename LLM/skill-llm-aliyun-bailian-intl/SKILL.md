---
name: skill-llm-aliyun-bailian-intl
description: Runtime contract for Aliyun Bailian International (Singapore) direct-model integration. Use it to resolve the retained model, Singapore workspace endpoints, API surfaces, per-surface parameters, thinking, tools, structured output, multimodal input, streaming, response mapping, pricing, and logging. It constructs requests only and never executes them.
---

# Skill LLM Aliyun Bailian International

## Purpose

Build a validated Singapore-region Aliyun Bailian request for `qwen3.8-max`. This skill is an integration contract, not a model selector or execution layer.

## Read Order

Read the shared schemas first, then:

1. `references/connection-profiles.md`
2. `references/workspace-configuration.md`
3. `references/request-urls.md`
4. `references/model-catalog.md`
5. `references/capability-matrix.md`
6. `references/model-parameters.md`
7. the matching transport
8. `references/pricing-matrix.md` only when cost matters
9. `references/logging-contract.md` when logging is implemented
10. `references/model-sync.md` only during an explicit update

## Runtime Rules

- Provider identifier is `aliyun-bailian-intl` and the maintained allowlist is exactly `qwen3.8-max`.
- Singapore and China Mainland are separate providers. Never copy endpoints, prices, availability, or rate limits across regions.
- Resolve an explicit connection profile and every declared connection input before URL construction. Workspace profiles require `ALIYUN_BAILIAN_INTL_WORKSPACE_ID`; shared profiles do not. Never switch profiles implicitly.
- Resolve request kind, exact model, API surface, API version, and endpoint kind before capability lookup.
- A generic provider parameter list is not model evidence. Use a field only when the exact model/surface row or an official model example confirms it.
- `unknown` is fail-closed. Reject the field and report the missing evidence; do not reinterpret silence as `unsupported`.
- Chat Completions/DashScope use `reasoning_effort`; Responses uses `reasoning.effort`. Never send `reasoning_effort` together with `thinking_budget`.
- Responses, Chat Completions, and DashScope multimodal generation are distinct payload contracts.
- For a workspace-specific direct-model profile, the workspace ID is encoded in the hostname; a shared profile has no workspace placeholder. Do not add `X-DashScope-WorkSpace` to these routes unless a separate application-API contract explicitly requires it.
- Preserve required reasoning and tool-call history; never expose hidden reasoning.
- Reject unsupported or unknown fields rather than dropping or renaming them.

## Request Kinds

- `chat`: text-first generation or agent turns
- `vision`: image or video understanding

## Out of Scope

China Mainland routes, imaging, Agent App orchestration, model ranking, substitution, execution, and unlisted models.
