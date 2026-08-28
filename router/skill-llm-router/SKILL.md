---
name: skill-llm-router
description: Route direct LLM integration work to exactly one provider and region skill when the user names a provider, region, or exact maintained model. Do not recommend models, infer regions, or silently choose among ambiguous provider entries.
---

# Skill LLM Router

## Purpose

Select exactly one provider skill before implementation. This router is the only skill in this pack allowed to trigger implicitly.

## Routing Rules

1. If the user names a provider and region, select that exact provider skill.
2. If the user names an exact model but not a provider, search each maintained provider skill's `references/model-catalog.md` file.
3. If one exact provider-region match exists, select it.
4. If the same model exists in multiple regional skills, require an explicit region or connection profile; do not guess.
5. If no exact catalog match exists, stop. Do not recommend a substitute or moving alias.
6. After selection, load only the chosen provider `SKILL.md` and its stated shared/provider references.
7. Never rewrite provider, region, model, API surface, API version, endpoint kind, profile, or route key.

## Provider Map

- OpenAI: `LLM/skill-llm-openai/SKILL.md`
- Aliyun Bailian China Mainland: `LLM/skill-llm-aliyun-bailian-cn/SKILL.md`
- Aliyun Bailian International: `LLM/skill-llm-aliyun-bailian-intl/SKILL.md`
- DeepSeek: `LLM/skill-llm-deepseek/SKILL.md`
- Gemini Developer API: `LLM/skill-llm-gemini/SKILL.md`
- MiniMax China Mainland: `LLM/skill-llm-minimax-cn/SKILL.md`
- MiniMax International: `LLM/skill-llm-minimax-intl/SKILL.md`
- ElevenLabs: `LLM/skill-llm-elevenlabs/SKILL.md`

## Out of Scope

- model ranking or recommendation
- provider fallback
- region inference from language, IP address, currency, or user location
- adding new models during ordinary implementation
