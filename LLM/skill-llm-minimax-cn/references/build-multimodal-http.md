# Build MiniMax China Mainland Multimodal HTTP

Resolve the surface first. OpenAI compatibility uses typed `image_url` / `video_url` message parts. Anthropic compatibility uses Anthropic image/video content blocks with its documented size and format limits. Native image generation uses `subject_reference`; it is not an M3 vision message. Reject untyped media.
