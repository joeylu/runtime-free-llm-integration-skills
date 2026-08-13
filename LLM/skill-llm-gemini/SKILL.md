---
name: skill-llm-gemini
description: Runtime contract for direct Gemini Developer API integration. Use it to resolve exact retained model IDs, Interactions or GenerateContent routes, model-specific thinking and sampling rules, tools, structured output, multimodal input, image generation/editing, state, streaming, pricing, and response mapping. It constructs requests only and does not cover Vertex AI.
---

# Skill LLM Gemini

## Purpose

Build a validated Gemini Developer API request for a model already selected by the user or host project. Do not recommend, substitute, or execute models.

## Read Order

Read shared schemas first, then:

1. `references/connection-profiles.md`
2. `references/request-urls.md`
3. `references/model-catalog.md`
4. `references/capability-matrix.md`
5. `references/model-parameters.md`
6. the matching transport
7. `references/hosted-tools.md` only when hosted tools are requested
8. `references/pricing-matrix.md` only when cost matters
9. `references/model-sync.md` only during an explicit update

## Runtime Rules

- Maintained IDs are exactly those in `references/model-catalog.md`.
- Resolve the full route key before using a capability: request kind, model, surface, API version, and endpoint kind.
- Interactions `v1`, Interactions `v1beta`, `generate-content`, and `stream-generate-content` are separate contracts.
- The stable Interactions `v1` route exists, but official examples may use `v1beta`; never switch versions silently.
- For `gemini-3.6-flash`, remove caller-supplied `temperature`, `top_p`, `top_k`, `candidate_count`, legacy `thinking_budget`, and prefilled model turns.
- Thinking levels and defaults are model-specific. Do not copy `gemini-3.6-flash` levels to either image model.
- Preserve thought signatures and function-call identity exactly when replaying history. Never expose hidden thoughts.
- Interactions continuation does not authorize omission of tools or configuration that the next turn still needs.
- Image output controls belong to `response_format` on current Interactions schema; GenerateContent uses its own field paths.
- A field marked `unknown` is rejected. Documentation silence is not evidence of absence.

## Request Kinds

- `chat`: text-first generation or agent turns
- `vision`: typed image, video, audio, or PDF understanding where the model row allows it
- `imaging`: image generation or editing

## Out of Scope

Vertex AI, consumer Gemini settings, model ranking, automatic discovery, raw chain-of-thought display, and request execution.
