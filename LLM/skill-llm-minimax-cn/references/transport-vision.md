# MiniMax China Mainland Vision Transport

Use this transport for `RequestKind = vision` with `MiniMax-M3` on `chat-completions`.

## Request

- Resolve a profile whose `Request Kinds` includes `vision`.
- Use the same `POST /chat/completions` URL as chat.
- Send the exact model ID `MiniMax-M3`.
- Map text and images into the provider's OpenAI-compatible message content parts.
- Accept only image inputs through the shared `Inputs.Images` field. MiniMax also documents video message input, but video requires a separate typed host contract and must not be encoded as an image.
- Apply thinking, temperature, tools, stream, and output-token rules from the `vision + MiniMax-M3 + chat-completions` capability row.

## Response

- Reuse the chat stream and non-stream parsing rules.
- Separate returned thinking text from final answer text according to `transport-chat.md`.
- Preserve tool-call IDs and arguments exactly.

## Failure Conditions

Stop before sending when the profile, URL row, image input, or any requested advanced field is not verified for this exact row.

Official source: https://platform.minimaxi.com/docs/api-reference/text-chat-openai
