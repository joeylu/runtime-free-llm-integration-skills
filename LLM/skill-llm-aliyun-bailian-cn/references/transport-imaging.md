# Aliyun Bailian China Mainland Imaging Transport

## Connection Gate

Resolve `connection-profiles.md` and `workspace-configuration.md` before model or payload construction.

- Workspace profiles require `ALIYUN_BAILIAN_CN_WORKSPACE_ID`; shared profiles do not.
- Do not serialize a URL containing `{WorkspaceId}`.
- Do not add `X-DashScope-WorkSpace` to direct model-inference requests.
- Keep model, profile, region, workspace when applicable, and API Key fixed through the full request lifecycle.

## Family Gate

Resolve the exact model before constructing content or parameters.

### Qwen-Image 3.0 Family

- Exactly one user message.
- Text-to-image: one text item.
- Image editing: one to three image items plus one text item.
- Parameters: `prompt_extend`, `prompt_extend_mode`, `n`, `size`, `negative_prompt`, `seed`, `watermark`.
- `prompt_extend_mode=agent` is text-to-image only.

#### Synchronous Route — Standard and Pro

- Models: `qwen-image-3.0`, `qwen-image-3.0-pro`.
- API surface: `multimodal-generation`.
- Path: `/services/aigc/multimodal-generation/generation`.
- Do not send `X-DashScope-Async`.
- The completed response contains generated image output.

#### Asynchronous Route — Standard Only Verified

- Model: `qwen-image-3.0`.
- API surface: `image-generation`.
- Create path: `/services/aigc/image-generation/generation`.
- Send `X-DashScope-Async: enable` on task creation.
- Treat the submission response as accepted work: it returns `task_id`, not a completed image.
- Poll `GET {Profile.Base URL}/tasks/{task_id}` with the same profile, region, workspace when applicable, and API Key.
- Do not send `X-DashScope-Async` on the poll request.
- The task ID, task data, and generated image URLs are retained for 24 hours.

`qwen-image-3.0-pro / image-generation` is `unknown` and must be rejected. Alibaba Cloud's model-specific API reference documents this route and shows Pro examples, but the official error-code reference explicitly states that `qwen-image-3.0-pro` does not support asynchronous calls. Do not choose one official statement over the other.

```json
{
  "model": "qwen-image-3.0",
  "input": {
    "messages": [
      {
        "role": "user",
        "content": [{"text": "..."}]
      }
    ]
  },
  "parameters": {
    "prompt_extend": true,
    "prompt_extend_mode": "direct",
    "n": 1,
    "size": "1024*1024",
    "watermark": false
  }
}
```

### Wan 2.7 / Pro

- Synchronous and asynchronous create endpoints are separate.
- Supports generation, editing, groups, multi-image references, and optional bounding boxes.
- Parameters include `enable_sequential`, `thinking_mode`, `color_palette`, `bbox_list`, model-specific `size`, `n`, `seed`, and `watermark`.
- `thinking_mode` is effective only for non-sequential requests with no image input; do not treat it as an image-edit control.
- Never copy Qwen-Image prompt-extension or negative-prompt fields into Wan requests unless the exact Wan contract is later verified.

For asynchronous creation, add `X-DashScope-Async: enable` and poll the task. A submission response is not a completed image.

## Output

Provider task data and image URLs expire after 24 hours. Normalize by downloading the asset or returning an explicit temporary-URL status; never treat the URL itself as durable storage.
