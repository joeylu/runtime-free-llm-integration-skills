# Gemini Imaging Transport

## Current Interactions Shape

```json
{
  "model": "gemini-3.1-flash-image",
  "input": "Create ...",
  "response_format": {
    "type": "image",
    "mime_type": "image/png",
    "aspect_ratio": "16:9",
    "image_size": "2K"
  }
}
```

Reference images are typed input items. `gemini-3.1-flash-image` supports 0.5K/1K/2K/4K and controllable thinking `minimal|high`; `gemini-3-pro-image` supports 1K/2K/4K, but this skill leaves its caller-selectable thinking values `unknown`.

Do not send `seed` or output-count fields: exact support is unverified. Do not copy Interactions `response_format` paths into GenerateContent. Only Flash Image supports retained video-to-image input. Its model page also declares PDF input; keep PDF as a typed document/file input and do not relabel it as an image.
