# Quickstart

This repository is a runtime-free skill pack for helping coding agents build fail-fast LLM provider integrations.

## 1. Start With Commands

For common workflows, ask your coding agent to read:

```text
COMMANDS.md
```

Example:

```text
List the available commands for this skill pack.
```

Use command-style requests when you already know what you want:

```text
init OpenAI chat integration
sync Gemini models
implement Aliyun Bailian China Mainland chat and vision
audit this repo for stale provider references
```

## 2. Current Providers

- OpenAI API
- Aliyun Bailian / DashScope China Mainland
- Aliyun Bailian / DashScope International / Singapore
- DeepSeek API
- Gemini Developer API
- MiniMax China Mainland API
- MiniMax International API

## 3. Keep The Structure

Keep the full folder structure intact:

```text
LLM/_shared/
LLM/skill-llm-openai/
LLM/skill-llm-aliyun-bailian-cn/
LLM/skill-llm-aliyun-bailian-intl/
LLM/skill-llm-deepseek/
LLM/skill-llm-gemini/
LLM/skill-llm-minimax-cn/
LLM/skill-llm-minimax-intl/
```

Do not copy only one provider `SKILL.md`; provider skills depend on shared contracts in `LLM/_shared`.

## 4. Give A Clear Task

Example:

```text
Read COMMANDS.md first.
Then use LLM/skill-llm-openai/SKILL.md and follow its read order.
Build a website settings page where users can enter an OpenAI API key, select a verified model, test the connection, and enable only verified capabilities.
```

For Aliyun Bailian, choose the regional provider first:

```text
Use Aliyun Bailian China Mainland and Aliyun Bailian International as separate providers.
Do not switch between their base URLs or request URLs automatically.
```

For MiniMax, choose the regional provider first:

```text
Use MiniMax China Mainland and MiniMax International as separate providers.
Do not switch between minimaxi.com and minimax.io base URLs automatically.
Use MiniMax plan profile for chat only.
Use MiniMax build profile for chat, image generation, and music generation; video links are reference-only until shared contracts add RequestKind=video.
```

## 5. Core Rules

- Use `model-catalog.md` for selectable model IDs.
- Use `pricing-matrix.md` for billing, estimates, and price display.
- Use `request-urls.md` to resolve the final request URL before sending a provider request.
- Use `capability-matrix.md` to gate every feature.
- Sync model metadata only when explicitly requested.
- Keep unknown values as `unknown`.
- Do not silently fall back between providers, regions, profiles, models, base URLs, request URLs, or API surfaces.

The key rule:

```text
Unknown means unknown.
Unsupported means unsupported.
Failed means failed.
```
