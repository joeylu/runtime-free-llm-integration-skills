# Aliyun Bailian International/Singapore Vision Transport

No International vision model is currently both active and selected in this skill.

The selected `qwen3.7-max` alias resolves to the text-only `qwen3.7-max-2026-05-20` snapshot. Do not send image, video, audio, or file input to it through either `responses` or `chat-completions`.

## Fail-Fast Rule

For `RequestKind = multimodal-chat`:

1. require an active selected `vision` row in `model-catalog.md`
2. require an exact `vision + model + API surface` capability row
3. require a verified request URL row for the same surface
4. require a transport mapping for the requested media type

Because those conditions are not met by the current catalog, stop with a capability/model-selection error before sending. Do not silently substitute `qwen3.7-max-2026-06-08`, another region, another model, or a chat-only row.

## Official Source

- `https://www.alibabacloud.com/help/en/model-studio/text-generation`
