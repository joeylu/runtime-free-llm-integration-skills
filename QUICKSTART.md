# Quickstart

## 1. Keep the pack together

Do not copy only one `SKILL.md`. Provider skills also use their `references/` folder, shared rules, and the evidence file.

Keep these folders together:

```text
LLM/_shared/
LLM/_evidence/
LLM/skill-llm-*/
```

## 2. Pick a provider and region

Be explicit. For example:

```text
Use Aliyun Bailian China Mainland. Do not use International endpoints or prices.
```

```text
Use MiniMax International with the build profile.
```

```text
Use Gemini Interactions v1. Do not fall back to v1beta or generateContent.
```

## 3. Tell the agent what to build

This is enough for most tasks:

```text
Read COMMANDS.md and LLM/skill-llm-openai/SKILL.md.
Build a settings page for OpenAI text and image generation.
Use selected models and verified capabilities only.
Show connection errors clearly and do not silently fall back.
```

The agent should resolve the provider, profile, model, API surface, URL, capabilities, roles, and price before it writes request code.

## 4. Refresh model data when needed

Ask for a sync when you need current models, prices, limits, or capabilities:

```text
Sync the MiniMax International skill from official sources, then audit it.
Keep newly found models as candidates unless they are already selected by policy.
Run the repository validator when finished.
```

Provider data changes over time, so do not treat an old local snapshot as live truth.

## 5. Validate repository changes

```bash
python tools/validate_repo.py
```

A passing result means the local files agree with each other. It does not prove that an API key works or that provider documentation has not changed since the recorded review date.
