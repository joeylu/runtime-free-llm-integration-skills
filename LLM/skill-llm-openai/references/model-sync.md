# OpenAI Model Sync

Use this workflow only when the user explicitly asks for one of these:

- latest OpenAI models
- sync model list
- verify current catalog
- remove downlisted or deprecated models
- refresh pricing or capability metadata

Read `../../_shared/recency-window-policy.md` before starting.

## Source Rule

Use official OpenAI documentation only.

Prefer:

- `https://developers.openai.com/api/docs/models`
- `https://developers.openai.com/api/docs/guides/latest-model`
- `https://developers.openai.com/api/docs/guides/structured-outputs`
- `https://developers.openai.com/api/docs/guides/function-calling`
- `https://developers.openai.com/api/docs/guides/reasoning`
- `https://developers.openai.com/api/docs/guides/image-generation`
- `https://developers.openai.com/api/docs/api-reference/responses/create`
- `https://openai.com/api/pricing/`

Do not sync from:

- blogs
- forum posts
- screenshots
- SDK enum comments
- third-party wrappers

## Live Collection Rule

Every sync or metadata collection task must be performed live by the LLM against official OpenAI documentation at the time of the task.

Do not write, use, or rely on scripts, scrapers, crawlers, generated parsers, SDK enum dumps, automated catalog generators, or any other programmatic processing to collect model rows, capabilities, pricing, context windows, max input tokens, or max output tokens.

The LLM may use normal reading and search tools to locate official documentation, but the reviewed values must be selected and recorded by the LLM from official docs during that sync.

## Sync Steps

1. Ask the user to confirm the recency boundary. If the user does not specify one, propose the default boundary `6 months`.
2. Convert that confirmed boundary into one absolute cutoff date using the sync date.
3. Open the official OpenAI direct-model documentation that matches the requested model kind.
4. Compare the official model list against `model-catalog.md`.
5. For every matched row, update all columns required by `../../_shared/model-catalog-schema.md`.
6. Add new official rows with the same schema.
7. Re-review rows already present in the current catalog using the same cutoff date.
8. If the user wants a curated local model set, ask the user to choose:
   - which `candidate` rows become `selected`
   - which selected row is the default for each model type
9. Mark selected rows as `active`.
10. Mark candidate rows that the user did not select as `deprecated` and `not-selected`.
11. Mark unavailable rows as `removed` instead of silently deleting them.
12. Mark rows outside the confirmed boundary as `deprecated` and `retired` even if the provider still lists them as available.
13. Collect `Context Window Tokens`, `Max Input Tokens`, and `Max Output Tokens` only when official OpenAI docs clearly expose them for the exact model row.
14. Update `pricing-matrix.md` in the same sync task using `../../_shared/pricing-matrix-schema.md`.
15. Update `capability-matrix.md` in the same sync task using `../../_shared/capability-matrix-schema.md`.
16. Keep `music` empty until official rows are actually verified for the shared `music` request kind.

## Evidence Rules

- Verify `stream` from the Responses API reference, model detail page, or request-kind guide.
- Verify `ReasoningEffort` from the model page, latest-model guide, reasoning guide, or Responses API reference.
- Verify `ReasoningSummary` from the Responses API reference or reasoning guide.
- Verify `json_schema` and `json_object` from structured-output docs or the Responses API reference.
- Verify caller-defined tools from function-calling docs or the Responses API reference.
- Verify OpenAI-hosted tools separately; do not use hosted-tool support as proof of caller-defined function support.
- Verify image generation, image edit, image input, size, count, and partial-image stream from the image-generation guide or image API reference.

## Fail-Fast Rule

If the official docs do not clearly confirm a field, leave that field as `unknown`.

Do not infer support for:

- a specific reasoning value
- raw reasoning visibility
- strict tool schemas
- parallel tool calls
- image seed
- image size
- image count
- streaming partial images
- context window
- max input tokens
- max output tokens
- price region
- price currency
- price unit
- price context band
- unit price

Do not infer context values from pricing tiers, observed request failures, sibling model names, SDK enum comments, or non-official references.

Do not infer pricing dimensions from unlabeled price text. If official docs do not clearly expose region, currency, context band, or unit price, keep that pricing field as `unknown`.

If official docs conflict on one reviewed row or field, stop and ask the user instead of guessing.

## Output Rule

After a sync task, the skill should have:

- an updated `model-catalog.md`
- an updated `pricing-matrix.md`
- an updated `request-urls.md` when endpoint paths, base URLs, or API surfaces changed
- an updated `capability-matrix.md`
- exact recency cutoff dates in reviewed catalog rows
- exact context window, max input, and max output fields when officially verified, otherwise `unknown`
- exact price region, currency, price unit, metered side, context band, and unit price rows in `pricing-matrix.md`
- exact official source URLs in changed rows
- no silently deleted models
