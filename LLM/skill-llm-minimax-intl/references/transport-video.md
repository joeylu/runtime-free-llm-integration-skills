# MiniMax International MiniMax-H3 Video Transport

Use this transport only after resolving one exact H3 RouteKey:

- `video::MiniMax-H3::video-generation::v2::provider-compatible`
- `video::MiniMax-H3::h3-context-ir::v2::provider-compatible`
- `video::MiniMax-H3::video-regeneration::v2::provider-compatible`
- `video::MiniMax-H3::video-task-query::v2::provider-compatible`
- `video::MiniMax-H3::video-task-list::v2::provider-compatible`
- `video::MiniMax-H3::video-task-cancel-delete::v2::provider-compatible`

All routes use `Authorization: Bearer <API_KEY>` and `Content-Type: application/json` on `https://api.minimax.io`. The account/key must have MiniMax-H3 pay-as-you-go API access. Never switch region, root, API key, surface, model, or billing path after resolution.

## Common H3 Content Contract

Primary generation and H3-Context-IR use this normalized mapping:

| Normalized Input | Wire Item |
| --- | --- |
| `Inputs.Prompt` | `{"type":"text","text":"..."}` |
| `Inputs.FirstFrameImage` | `{"type":"image_url","image_url":{"url":"..."},"role":"first_frame"}` |
| `Inputs.LastFrameImage` | `{"type":"image_url","image_url":{"url":"..."},"role":"last_frame"}` |
| each `Inputs.ReferenceImages` item | `{"type":"image_url","image_url":{"url":"..."},"role":"reference_image"}` |
| each `Inputs.ReferenceVideos` item | `{"type":"video_url","video_url":{"url":"..."},"role":"reference_video"}` |
| each `Inputs.ReferenceAudio` item | `{"type":"audio_url","audio_url":{"url":"..."},"role":"reference_audio"}` |

The provider documentation defines every supported mode with one non-empty text item. This skill therefore emits exactly one normalized `Inputs.Prompt` item; it does not expose arbitrary raw `content[]` passthrough.

Resolve exactly one mode before serialization:

1. **Text-only:** one text item and no media. `ratio` is required and must be one of `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; `adaptive` is invalid.
2. **Frame:** text plus first frame, last frame, or both. Reference roles are forbidden. Provider behavior is `adaptive`: omitting `ratio` or sending `adaptive` is effective; a documented concrete value is accepted but ignored. Skill behavior is stricter: reject a caller-supplied concrete ratio rather than silently sending an ineffective control.
3. **Reference:** text plus at least one reference image, video, or audio. Frame roles are forbidden. `ratio` is optional, defaults to `adaptive`, and may be `adaptive` or any documented concrete value.

Validate before sending:

- prompt length: 1–7000 characters; never truncate or split automatically;
- request body: no more than 64 MB; URL input is recommended for large assets and the skill does not invent Base64 conversion;
- image: JPG/JPEG/PNG/WEBP/HEIC/HEIF, no more than 30 MB each, width and height each 256–5760 px, width/height 0.4–2.5; first frame <=1, last frame <=1, reference images <=9;
- reference video: MP4/MOV, H.264/AVC or H.265/HEVC, embedded audio AAC/MP3, no more than 50 MB each, <=3 clips, each 2–15 seconds, total <=15 seconds, width and height each 256–5760 px, width/height 0.4–2.5, frame rate 23.976–60;
- reference audio: WAV/MP3, no more than 15 MB each, <=3 clips, each 2–15 seconds, total <=15 seconds;
- combined reference images/videos/audio: <=12 files.

Reject empty prompts, untyped media, unknown roles, duplicate frame roles, mixed frame/reference roles, unsupported formats, exceeded limits, and caller requests to rewrite or drop invalid inputs.

## Primary Generation

POST `https://api.minimax.io/v2/video_generation` with exactly:

- `model = MiniMax-H3`;
- validated `content`;
- required `resolution`: `768P` or `2K`;
- required integer `duration`: 4–15;
- the mode-valid `ratio` contract above;
- optional `callback_url`;
- `aigc_watermark` is not documented on International primary generation. Treat it as unknown and reject it rather than copying the China Mainland field.

The create response contains `task_id`; it does not establish an initial task status. Reject undocumented controls such as seed, negative prompt, FPS override, arbitrary camera objects, output-format aliases, or stream.

## H3-Context-IR

POST `https://api.minimax.io/v2/h3_context_ir` with `model`, validated `content`, required integer `duration` 4–15, mode-valid `ratio`, and optional `callback_url`.

Do not send `resolution`, `aigc_watermark`, or video-output controls. This endpoint creates an asynchronous prompt-enhancement task and does not create video. On success, map `task.content.prompt` to `TextContent`; do not fabricate `VideoOutputs`.

## Video Regeneration

POST `https://api.minimax.io/v2/video_regeneration`. Resolve a strict exclusive union:

1. **Task-ID mode:** send `source_task_id` from `Inputs.SourceTaskId`. The source must be a succeeded `/v2/video_generation` task owned by the current account, still queryable within the 7-day window, and the account must have the documented whitelist access.
2. **Source-video mode:** reproduce every original H3 generation `content` item exactly, then append exactly one `{"type":"video_url","video_url":{"url":"..."},"role":"base_video"}` item from `Inputs.BaseVideo`. The source must meet MiniMax-H3 768P output specifications.

Both modes require `model = MiniMax-H3` and `resolution = 2K`. `callback_url` and `aigc_watermark` are optional; `aigc_watermark` defaults to `false` on this exact regeneration surface in both regions. Reject both source forms, neither source form, reconstructed or incomplete original content, caller-supplied duration/ratio, seed, stream, or arbitrary-video processing.

## Shared Task Lifecycle

| Operation | Method and URL | Boundary |
| --- | --- | --- |
| Query one | `GET https://api.minimax.io/v2/query/video_generation/{task_id}` | only tasks still available in the latest 7-day window |
| List | `GET https://api.minimax.io/v2/query/video_generation` | latest 7 days; optional documented filters only |
| Cancel/delete | `DELETE https://api.minimax.io/v2/video_generation/{task_id}` | state-dependent behavior below |

Store the create `task_id` under typed `ProviderMeta.job_id` and normalized `job_id`; never put it in `ContinuationId`.

`callback_url` and query/polling are independent capabilities. A configured callback does not disable query. Before sending a callback request, the host must be able to echo MiniMax's verification `challenge` unchanged within 3 seconds. Do not silently remove the callback, change monitoring mode, or invent callback success. When polling is selected, the official guide recommends a 10-second interval.

Observed status values are `queued`, `running`, `succeeded`, `failed`, and `cancelled`. Do not assume `queued` immediately after creation because create returns only `task_id`. Treat `queued`/`running` as active and `succeeded`/`failed`/`cancelled` as terminal.

List query fields are exactly `page_num`, `page_size`, `filter.status`, `filter.task_ids`, `filter.model`, and `filter.task_type`. `page_num` starts at 1. The rendered official reference does not publish a `page_size` range/default or the raw URL encoding of `filter.task_ids: string[]`. A raw HTTP adapter must use a serializer verified from an official machine-readable schema or stop; never guess comma-separated, repeated-key, bracket, or JSON encoding. Task types are exactly `generation`, `h3_context_ir`, and `regeneration`.

DELETE behavior is exact and state-dependent:

- `queued`: cancel; provider returns action/status `cancelled` and does not charge the cancelled queued task;
- `succeeded` or `failed`: delete the task record; provider returns action/status `deleted`;
- `running` or `cancelled`: provider rejects the operation; preserve that error.

## Response Mapping

On `succeeded`:

- `generation` or `regeneration`: map the single `task.content.url` to one `VideoOutputs` item. The URL points to the produced video file, which may contain the model's audio track; do not invent a separate audio URL.
- `h3_context_ir`: map `task.content.prompt` to `TextContent`.

Map the observed status, task type, modality, resolution, duration, ratio, usage, timestamps, and provider error into normalized metadata/progress/usage/error fields. Do not log raw prompts, original content arrays, media URLs, result URLs, API keys, bearer tokens, or callback payload secrets by default.

## Official Sources

- `https://platform.minimax.io/docs/api-reference/video-generation-v2-create`
- `https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir`
- `https://platform.minimax.io/docs/api-reference/video-generation-v2-regeneration`
- `https://platform.minimax.io/docs/api-reference/video-generation-v2-query`
- `https://platform.minimax.io/docs/api-reference/video-generation-v2-list`
- `https://platform.minimax.io/docs/api-reference/video-generation-v2-delete`
- `https://platform.minimax.io/docs/guides/video-generation`
