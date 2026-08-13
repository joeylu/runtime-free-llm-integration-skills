# Gemini Vision Transport

Use typed media inputs. `gemini-3.6-flash` and `gemini-3.1-pro-preview` accept text, image, video, audio, and PDF; the shared `vision` envelope only proves image input unless the host explicitly models the other media type.

- Interactions: typed items in `input`.
- GenerateContent: typed parts in `contents`.
- Never disguise audio/video/PDF as an image field.
- Preserve function call IDs and thought signatures across multimodal tool turns.
- Validate upload/file URI lifetime before constructing the request.
