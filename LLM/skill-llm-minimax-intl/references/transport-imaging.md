# MiniMax Imaging Transport

Use `POST /v1/image_generation` with `model: image-01`.

- T2I: prompt plus output controls.
- Subject-reference I2I: add the documented `subject_reference` array of character-reference objects.
- `aspect_ratio` takes precedence over `width`/`height`; width and height must be supplied together.
- `n` is 1..9; `response_format` is `url|base64`; URL expires after 24 hours.
- Streaming remains `unknown` and must be rejected.
