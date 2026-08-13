# MiniMax Vision Transport

MiniMax-M3 accepts typed image and video input on both maintained text surfaces. Field shapes differ:

- OpenAI compatibility: `image_url` and `video_url` typed message parts.
- Anthropic compatibility: Anthropic image/video source blocks.

Validate MIME type, transport (URL/base64/provider file), and size against the exact surface. Do not place media URLs in plain text and call it verified multimodal input.
