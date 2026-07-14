# Gemini Music Transport

No local music model is selected in `model-catalog.md`, and no music capability row is bundled.

If a caller requests `RequestKind = music-generation`, stop before implementation. An explicit sync must first add:

- exact model and lifecycle status
- request URL and API surface
- input, duration, seed, and output constraints
- synchronous, background, or streaming protocol
- pricing
- response and file handling
- safety and attribution requirements

Do not map a Lyria, Live, TTS, or consumer Gemini feature into this skill by analogy.
