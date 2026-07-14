# Model and Schema Migration — 2026-07-14

This release moves the provider pack to schema v2. The change is repository-wide and should be adopted as one unit.

## Main changes

- Catalog state is now split into provider lifecycle, local selection, and review freshness.
- Provider records are keyed by exact request kind, model, API surface, API version, and regional scope.
- Capability checks no longer flow from one compatible-looking surface or version to another.
- Role and tool-history requirements live in dedicated role-support matrices.
- Caller-defined tools and provider-hosted tools are separate contracts.
- Official-source facts are backed by field-level claims in `LLM/_evidence/evidence.json`.
- Pricing rows include serving, deployment, billing, tier, effective-window, and metered-side scope.

## Request-kind names

| Legacy input | Canonical name |
| --- | --- |
| `chat` | `text-chat` |
| `vision` | `multimodal-chat` |
| `imaging` | `image-generation` |
| `music` | `music-generation` |

Normalize legacy names once at the repository boundary. New provider matrices and transports use canonical names.

## Curated default updates

- OpenAI text and multimodal: `gpt-5.6-sol`
- OpenAI image generation: `gpt-image-2`
- Gemini text and multimodal: `gemini-3.5-flash`
- Gemini image generation: `gemini-3.1-flash-image`
- DeepSeek text: `deepseek-v4-flash`
- Aliyun Bailian China Mainland text and multimodal: `qwen3.7-plus`
- Alibaba Cloud Model Studio International text: `qwen3.7-max`
- MiniMax China Mainland and International text: `MiniMax-M2.7`
- MiniMax image generation: `image-01`
- MiniMax music generation: `music-2.6`

Older models remain only where the provider state and local compatibility view require them. A local replacement does not by itself claim provider deprecation.

## Upgrade checklist

1. Keep `LLM/_shared`, `LLM/_evidence`, and all selected provider folders together.
2. Update callers to resolve the exact API surface and version before capability lookup.
3. Normalize legacy request-kind names at the input boundary.
4. Recheck any code that assumed one generic role model or one generic `tools` field.
5. Run `python tools/validate_repo.py`.
6. Perform authenticated runtime tests in the target provider and region before production use.
