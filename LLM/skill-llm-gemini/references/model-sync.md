# Gemini Model Sync

Use this file only when the owner explicitly asks to sync, refresh, or verify latest Gemini models.

## Official Sources

Use official Gemini Developer API sources first:

- model overview: `https://ai.google.dev/gemini-api/docs/models`
- model pages: `https://ai.google.dev/gemini-api/docs/models/<model-id>`
- pricing: `https://ai.google.dev/gemini-api/docs/pricing`
- thinking: `https://ai.google.dev/gemini-api/docs/thinking`
- structured outputs: `https://ai.google.dev/gemini-api/docs/structured-output`
- function calling: `https://ai.google.dev/gemini-api/docs/function-calling`
- text and streaming: `https://ai.google.dev/gemini-api/docs/text-generation`
- image generation: `https://ai.google.dev/gemini-api/docs/image-generation`

Do not use third-party model lists as truth sources.

## Live Collection Rule

Every sync or metadata collection task must be performed live by the LLM against official Gemini Developer API documentation at the time of the task.

Do not write, use, or rely on scripts, scrapers, crawlers, generated parsers, SDK enum dumps, automated catalog generators, or any other programmatic processing to collect model rows, capabilities, pricing, context windows, max input tokens, or max output tokens.

The LLM may use normal reading and search tools to locate official documentation, but the reviewed values must be selected and recorded by the LLM from official docs during that sync.

## Sync Workflow

1. Confirm the recency boundary before changing rows.
2. Convert the recency boundary into an absolute cutoff date.
3. Review official model rows and release/deprecation notes.
4. Update `model-catalog.md` first.
5. Update `pricing-matrix.md` with region, currency, unit, metered side, context band, and unit price rows.
6. Update `request-urls.md` when endpoint paths, base URLs, or API surfaces change.
7. Update `capability-matrix.md` only for capabilities verified from official docs.
8. Collect `Context Window Tokens`, `Max Input Tokens`, and `Max Output Tokens` only when official Gemini docs clearly expose them for the exact model row.
9. Update transport files only when a provider API surface changes.
10. Keep unknown fields as `unknown`; do not infer support from similar providers, pricing tiers, observed request failures, SDK enum comments, or unlabeled price text.

## Selection Rule

Keep the selected local set small.

Select rows only when they are needed for practical integration:

- one default chat/vision model
- one higher-quality chat/vision alternative
- one default Nano Banana imaging model
- one higher-quality Nano Banana imaging alternative when verified

Put other reviewed rows under candidate notes unless the owner asks to expose them.

## Vertex AI Rule

Gemini Developer API and Vertex AI are separate endpoint families.

If the owner asks for Vertex AI, create or extend a separate profile and re-check:

- authentication
- base URL
- region/project routing
- model IDs
- request/response shapes
- streaming behavior
- image generation behavior

Do not silently reuse Developer API rows as Vertex AI rows.
