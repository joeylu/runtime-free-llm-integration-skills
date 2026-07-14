# Gemini Imaging Transport

Use this for image generation or editing after choosing `gemini-3.1-flash-image` or `gemini-3-pro-image`.

## Surface Choice

- Prefer `interactions` for all new image work.
- Use `generate-content` only for explicit compatibility requirements.
- Interactions streaming is verified only for `gemini-3.1-flash-image`; `gemini-3-pro-image` streaming remains `unknown` and must fail fast. GenerateContent imaging remains non-stream in this skill.
- Do not call the shut-down Preview image IDs.

## Interactions Mapping

| Shared Field | Interactions Field | Rule |
| --- | --- | --- |
| `Model` | `model` | stable selected image model |
| `Inputs.Prompt` | text `input` item | required |
| `Inputs.ReferenceImages` | typed image input items | only within model-specific reference limits |
| `Inputs.ImageSize` | `response_format.image_size` | exact uppercase values such as `1K`, `2K`, `4K`; Flash also supports `0.5K` |
| `ProviderOptions.AspectRatio` | `response_format.aspect_ratio` | validate against the model table |
| `ProviderOptions.OutputMimeType` | `response_format.mime_type` | supported image MIME only |
| `ContinuationId` | `previous_interaction_id` | enables conversational editing only for a stored compatible Interaction |
| `StoreResponse` | `store` | false prevents later ID continuation |
| `ReasoningEffort` | model thinking-level field | Flash only: `minimal` or `high`; Pro is blocked as unknown |
| `HostedTools` | imaging-supported provider tools | Search grounding only after hosted-tool verification |

Set `response_format.type = image`. A mixed text-and-image response format may be used only when the caller explicitly asks for both and the adapter has a tested parser.

For `gemini-3.1-flash-image`, `IsStream = true` maps to body `stream: true` on the same Interactions endpoint. Parse `step.delta` types separately: append `text` deltas to `TextContent`, incrementally decode or buffer `image` deltas by MIME type, retain `thought_signature` as opaque state, and finish only after `interaction.completed` plus `[DONE]`. Unknown future event or delta types should be logged and skipped safely rather than reinterpreted.

## GenerateContent Compatibility

GenerateContent remains supported, but its image configuration and response parts differ from Interactions. Keep a dedicated adapter and contract test for the current official GenerateContent image payload. Never copy Interactions snake_case `response_format` fields directly into GenerateContent.

Map returned image parts from the provider response into `ImageOutputs`; preserve any accompanying text separately.

## Reference Limits

- `gemini-3.1-flash-image`: up to 14 references total, including up to 10 object images and up to 4 character references.
- `gemini-3-pro-image`: up to 14 references total, including up to 6 object images, up to 5 character references, and up to 3 style references.

Validate category-specific limits; do not check only the total.

## Output Controls

- Flash sizes: `0.5K`, `1K`, `2K`, `4K`.
- Pro sizes: `1K`, `2K`, `4K`.
- Use only official aspect ratios for the selected model.
- Reject lowercase size forms such as `1k`.
- `Inputs.ImageCount` is unsupported. Do not promise an exact number of generated images.
- `Inputs.Seed` is unsupported in this local contract.

## Thinking

Gemini 3 image models use thinking. For `gemini-3.1-flash-image`, default is `minimal` and verified caller levels are `minimal` and `high`. For `gemini-3-pro-image`, exact caller-selectable levels remain unknown, so block `ReasoningEffort`.

Thought images or signatures are provider internals. Do not display them as final output or raw chain-of-thought.

## Progress

Use stage-based progress only:

`validating -> preparing -> sending -> waiting-first-byte -> decoding-result -> local-processing -> completed`

Do not invent percentages.

## Response Mapping

- final image bytes or provider file references -> `ImageOutputs`
- accompanying final text -> `TextContent`
- provider-visible thought summary -> `ReasoningSummary`
- signatures/state items -> `ReasoningItems`
- Search sources -> `Annotations`
- reusable Interaction ID -> `ContinuationId`
- token/image usage -> `Usage`

Do not emit `completed` until all final image data has been decoded or securely resolved and, for Interactions streaming, the terminal interaction event has been observed.
