---
name: skill-llm-minimax-intl
description: Runtime contract for MiniMax International direct-model integration. Use it to resolve exact retained model IDs, regional endpoints, OpenAI-compatible and Anthropic-compatible text surfaces, per-surface thinking defaults, multimodal input, tools, image generation/editing, Music 3.0, streaming, pricing, and response mapping. It constructs requests only and never executes them.
---

# Skill LLM MiniMax International

## Purpose

Build a validated MiniMax International request for a model already selected by the user or host project. This skill is not a model selector or execution layer.

## Read Order

Read shared schemas first, then:

1. `references/connection-profiles.md`
2. `references/request-urls.md`
3. `references/model-catalog.md`
4. `references/capability-matrix.md`
5. `references/model-parameters.md`
6. `references/api-surface-scope.md`
7. the matching transport
8. `references/pricing-matrix.md` only when cost matters
9. `references/model-sync.md` only during an explicit update

## Runtime Rules

- Provider identifier is `minimax-intl`; maintained IDs are exactly `MiniMax-M3`, `image-01`, and `music-3.0`.
- China Mainland and International endpoints, credentials, currencies, and prices are not interchangeable.
- Resolve the full route key before using any parameter.
- MiniMax-M3 OpenAI compatibility defaults thinking on; Anthropic compatibility defaults thinking off. Never normalize those defaults into one provider-wide rule.
- `reasoning_split` changes response layout only; it does not enable or disable thinking.
- Prefer `max_completion_tokens`; `max_tokens` is legacy on OpenAI compatibility.
- Fields ignored by the Anthropic compatibility layer are not supported controls. Reject them rather than assuming they work.
- Image and music payloads are native MiniMax contracts, not OpenAI/Anthropic messages.
- `unknown` is fail-closed. Do not infer support or absence from a generic schema or a single-model example.

## Request Kinds

- `chat`: text-first generation and tools
- `vision`: image/video understanding
- `imaging`: text-to-image or subject-reference image-to-image
- `music`: text/lyrics-to-music

## Out of Scope

Other MiniMax models, regional fallback, model ranking, automatic substitution, request execution, and implicit parameter translation between surfaces.
