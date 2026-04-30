# runtime-free-llm-integration-skills

Runtime-free skills for coding agents to build fail-fast LLM provider integration, starting with OpenAI and Aliyun Bailian / DashScope.

## What problem does this solve?

Many projects want to let users connect their own LLM provider by entering an API key, choosing a model, and enabling features like chat, vision, or image generation.

The hard part is not just calling an API.

The hard part is making sure the coding agent does not:

- guess model IDs
- mix provider names
- enable unsupported features
- silently fall back to another model or key
- hide connection errors
- build confusing provider/model UI

This repository provides a lightweight skill-based map for building that integration correctly.

## Core idea

This is not an LLM gateway, proxy, SDK, or runtime.

It does not force your application traffic through a bridge like LiteLLM or Portkey.

Instead, it gives coding agents a set of provider integration rules so they can build native LLM connection logic directly inside your project.

The authoring logic is simple:

> Unknown means unknown.  
> Unsupported means disabled.  
> Failed means failed.  
> Do not guess, do not hide, do not fallback silently.

## Current provider coverage

The current version includes these concrete provider skills:

- OpenAI API
- Aliyun Bailian / DashScope

The shared structure is designed so more LLM providers can be added later.

## What is included?

- shared request / response / error contracts
- provider model catalog pattern
- connection profile pattern for separate API keys and base URLs
- capability matrix rules
- model selection UI guidance
- provider configuration UI guidance
- fail-fast validation rules
- transport rules for different model modes
- OpenAI API provider skill
- Aliyun Bailian / DashScope provider skill

## Who is this for?

This repository is for developers who use coding agents such as Codex, Claude Code, Cursor, or similar tools to build LLM provider integration into their own apps.

Typical use case:

> "Build a website settings page where users can enter their own LLM API key, select a provider model, test the connection, and enable only verified capabilities."

## What this is not

This is not:

- a runtime service
- an API proxy
- a hosted gateway
- a full model registry
- a universal LLM SDK
- a fallback router

If you want a runtime bridge, use a gateway or SDK.

If you want a lightweight integration map for coding agents, this repository is for that.

## Basic usage

Copy or reference the relevant skill folder in your coding-agent workflow.

Start from:

```text
LLM/_shared/
LLM/skill-llm-openai/
LLM/skill-llm-aliyun/
```
