# Build MiniMax International Multimodal HTTP

Resolve the surface first. OpenAI compatibility uses typed `image_url` / `video_url` message parts. Anthropic compatibility uses Anthropic image/video content blocks with its documented size and format limits. Native image generation uses `subject_reference`; it is not an M3 vision message.

MiniMax-H3 uses native V2 `content[]` items with exact `type` and `role` values. Primary generation and H3-Context-IR share the validated text/frame/reference content modes; regeneration instead resolves exactly one documented source mode. Read `transport-video.md` before serializing H3. Reject untyped media, mixed frame/reference roles, reconstructed regeneration inputs, and cross-surface fields.
