# OpenAI Model Sync

Use this workflow only when the user explicitly asks for one of these:

- latest OpenAI models
- sync model list
- verify current catalog
- remove downlisted or deprecated models
- refresh pricing or capability metadata

Read `../_shared/recency-window-policy.md` before starting.

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

## Sync Steps

1. Ask the user to confirm the recency boundary. If the user does not specify one, propose the default boundary `6 months`.
2. Convert that confirmed boundary into one absolute cutoff date using the sync date.
3. Open the official OpenAI direct-model documentation that matches the requested model kind.
4. Compare the official model list against `references/model-catalog.md`.
5. For every matched row, update all columns required by `../_shared/model-catalog-schema.md`.
6. Add new official rows with the same schema.
7. Re-review rows already present in the current catalog using the same cutoff date.
8. If the user wants a curated local model set, ask the user to choose:
   - which `candidate` rows become `selected`
   - which selected row is the default for each model type
9. Mark selected rows as `active`.
10. Mark candidate rows that the user did not select as `deprecated` and `not-selected`.
11. Mark unavailable rows as `removed` instead of silently deleting them.
12. Mark rows outside the confirmed boundary as `deprecated` and `retired` even if the provider still lists them as available.
13. Update `references/capability-matrix.md` in the same sync task using `../_shared/capability-matrix-schema.md`.
14. Keep `music` empty until official rows are actually verified for the shared `music` request kind.

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

If official docs conflict on one reviewed row or field, stop and ask the user instead of guessing.

## Output Rule

After a sync task, the skill should have:

- an updated `references/model-catalog.md`
- an updated `references/capability-matrix.md`
- exact recency cutoff dates in reviewed catalog rows
- exact price region and price unit fields in selected catalog rows
- exact official source URLs in changed rows
- no silently deleted models
