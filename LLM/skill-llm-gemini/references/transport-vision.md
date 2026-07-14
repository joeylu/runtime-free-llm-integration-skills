# Gemini Vision Transport

Use this for `RequestKind = multimodal-chat` and image understanding. Chat state, thinking, tools, schema, cache, and stream rules inherit from `transport-chat.md`.

## Input Contract

The shared request requires ordered `Inputs.Messages` and `Inputs.Images`. Validate every image before serialization:

- supported MIME type
- size and count limits from current official media guidance
- reachable file or valid inline bytes
- no secret-bearing URLs in logs

This skill does not silently reinterpret audio, video, or PDF input as `Inputs.Images`. Those modalities are supported by the selected text models, but a host project must add a typed media-input extension and re-verify its upload, token, and response behavior.

## Interactions Mapping

Map each image to a typed image input item with its MIME type and either provider-supported bytes or URI representation. Preserve the caller's text/image order when it is semantically important.

For stateful follow-ups, `previous_interaction_id` can preserve prior multimodal history, but current `tools`, `system_instruction`, and `generation_config` must still be re-sent.

## GenerateContent Mapping

Map images into content parts on the selected `generate-content` or `stream-generate-content` surface. For stateless multi-turn requests, replay the full unmodified content history and thought signatures.

## Media Resolution

Use provider media-resolution controls only after exact verification for the selected model, media type, and API surface. Do not infer image token cost or fidelity from pixel dimensions alone.

## Tools and Structured Output

- Caller-defined functions follow the exact call/result identity rules in `transport-chat.md`.
- Multimodal function results must be inside the function result object.
- `json_schema` mappings differ by surface and must not be copied between Interactions and GenerateContent.
- Hosted tools require `hosted-tools.md` verification.

## Response Mapping

Map final text to `TextContent`, schema output to `StructuredContent`, function requests to `ToolCalls`, hosted activity to `HostedToolCalls`, grounding to `Annotations`, signatures to `ReasoningItems`, and usage to the normalized `Usage` object.

Image understanding does not produce `ImageOutputs`. Image generation belongs to `RequestKind = image-generation`.
