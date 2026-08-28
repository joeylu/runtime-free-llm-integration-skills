# MiniMax International API Surface Scope

- `chat-completions`: OpenAI-compatible MiniMax-M3; thinking defaults on.
- `anthropic-messages`: Anthropic-compatible MiniMax-M3; thinking defaults off.
- `video-generation`: native asynchronous MiniMax-H3 primary generation.
- `h3-context-ir`: native asynchronous MiniMax-H3 multimodal prompt enhancement; returns text, not video.
- `video-regeneration`: native asynchronous MiniMax-H3 768P-to-2K regeneration.
- `video-task-query`: query one H3 task from the last 7 days.
- `video-task-list`: list H3 tasks from the last 7 days with exact filters.
- `video-task-cancel-delete`: state-dependent cancel or record deletion.
- `image-generation`: native `image-01`.
- `music-generation`: native `music-3.0`.

The three H3 create surfaces share query, list, and cancel-or-delete task-management endpoints, but their create parameters and result modalities remain separate. Do not translate optional fields between any surfaces without an exact row in `model-parameters.md`.
