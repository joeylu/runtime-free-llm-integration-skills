# Aliyun Bailian China Mainland Vision Transport

## Rules

- `qwen3.8-max` and `qwen3.7-plus` accept image and video input on Chat Completions and DashScope native surfaces.
- Responses is maintained for `input_image` only. Do not send video, audio, or generic files on that route.
- Keep text and media in documented typed content blocks. Do not disguise media URLs as plain text.
- Validate provider limits before request construction; do not infer one surface's media object shape from another.
- In multi-turn thinking/tool flows, replay required assistant reasoning and tool-call identities exactly.

## OpenAI-compatible Image Example

```json
{
  "model": "qwen3.8-max",
  "messages": [{
    "role": "user",
    "content": [
      {"type": "text", "text": "Describe the image."},
      {"type": "image_url", "image_url": {"url": "https://example.com/image.png"}}
    ]
  }]
}
```

## Responses Image Example

```json
{
  "model": "qwen3.8-max",
  "input": [{"role": "user", "content": [
    {"type": "input_text", "text": "Describe the image."},
    {"type": "input_image", "image_url": "https://example.com/image.png"}
  ]}]
}
```
