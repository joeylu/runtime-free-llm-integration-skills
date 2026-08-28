---
name: skill-llm-minimax-cn
description: Runtime contract for MiniMax China Mainland direct-model integration. Use it to resolve exact retained model IDs, regional endpoints, OpenAI-compatible and Anthropic-compatible text surfaces, per-surface thinking defaults, multimodal input, tools, MiniMax-H3 video workflows, image generation/editing, Music 3.0, streaming, pricing, and response mapping. It constructs requests only and never executes them.
---

# Skill LLM MiniMax China Mainland

## Purpose

Build a validated MiniMax China Mainland request for a model already selected by the user or host project. This skill is not a model selector or execution layer.

## Read Order

Read shared schemas first, then:

1. `references/connection-profiles.md`
2. `references/request-urls.md`
3. `references/model-catalog.md`
4. `references/capability-matrix.md`
5. `references/model-parameters.md`
6. `references/api-surface-scope.md`
7. the matching transport, including `references/transport-video.md` for `MiniMax-H3`
8. `references/pricing-matrix.md` only when cost matters
9. `references/model-sync.md` only during an explicit update

## Runtime Rules

- Provider identifier is `minimax-cn`; maintained IDs are exactly `MiniMax-M3`, `MiniMax-H3`, `image-01`, and `music-3.0`.
- China Mainland and International endpoints, credentials, currencies, and prices are not interchangeable.
- Resolve the full route key before using any parameter.
- MiniMax-M3 OpenAI compatibility defaults thinking on; Anthropic compatibility defaults thinking off. Never normalize those defaults into one provider-wide rule.
- `reasoning_split` changes response layout only; it does not enable or disable thinking.
- Prefer `max_completion_tokens`; `max_tokens` is legacy on OpenAI compatibility.
- Fields ignored by the Anthropic compatibility layer are not supported controls. Reject them rather than assuming they work.
- Image, video, and music payloads are native MiniMax contracts, not OpenAI/Anthropic messages.
- `MiniMax-H3` uses the regional root domain and native asynchronous V2 routes; never append H3 paths to a `/v1` media base URL.
- H3 primary generation, H3-Context-IR, and H3 regeneration are distinct surfaces with distinct required fields and result mappings.
- H3 requires MiniMax pay-as-you-go API access. Do not infer a special key type, and do not substitute a legacy video model, package, API surface, or region.
- `unknown` is fail-closed. Do not infer support or absence from a generic schema or a single-model example.

## Request Kinds

- `chat`: text-first generation and tools
- `vision`: image/video understanding
- `imaging`: text-to-image or subject-reference image-to-image
- `video`: MiniMax-H3 primary generation, H3-Context-IR prompt enhancement, or 768P-to-2K regeneration
- `music`: text/lyrics-to-music

## Out of Scope

Other MiniMax models, arbitrary-video processing, regional fallback, model ranking, automatic substitution, request execution, and implicit parameter translation between surfaces.
