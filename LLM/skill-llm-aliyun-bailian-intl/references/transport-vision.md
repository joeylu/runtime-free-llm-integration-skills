# Aliyun Bailian International Vision Transport

No International `vision` row is documented in this skill.

The moving `qwen3.7-max` alias documented here is text-only. Do not send image, video, audio, or file input to it through `responses` or `chat-completions`.

Before implementing International vision, all of the following must exist for the exact region and model:

1. a `vision` row in `model-catalog.md`;
2. a verified request URL row;
3. `Supports Image Input = verified` in `capability-matrix.md`;
4. request and response mapping rules in this transport.

Until those rows exist, stop with `capability_unverified`. Do not substitute a snapshot, China Mainland endpoint, another model, or a chat-only row.
