# MiniMax China Mainland Model Sync

Use this workflow only when the user explicitly asks for one of these:

- latest MiniMax China Mainland models
- sync model list
- verify current catalog
- remove downlisted or deprecated models
- refresh pricing or capability metadata

Read `../../_shared/recency-window-policy.md` before starting.

## Source Rule

Use official MiniMax China Mainland documentation only.

Prefer:

- API overview: `https://platform.minimaxi.com/docs/api-reference/api-overview`
- OpenAI-compatible chat API: `https://platform.minimaxi.com/docs/api-reference/text-chat-openai`
- image generation API: `https://platform.minimaxi.com/docs/api-reference/image-generation-t2i`
- music generation API: `https://platform.minimaxi.com/docs/api-reference/music-generation`
- video generation guide: `https://platform.minimaxi.com/docs/guides/video-generation`
- model release notes: `https://platform.minimaxi.com/docs/release-notes/models`
- pay-as-you-go pricing: `https://platform.minimaxi.com/docs/guides/pricing-paygo`

Do not use MiniMax International docs, endpoints, availability, or pricing for this skill.

Keep the local profile boundary during sync:

- `plan` remains chat-only unless the owner explicitly changes this skill.
- `build` may sync HTTP `chat`, `imaging`, and `music`.
- video docs may be recorded in `build-multimodal-http.md`, but do not add first-class video rows until shared schemas define `RequestKind = video`.

Do not sync from:

- blogs
- forums
- screenshots
- repo enum comments
- third-party wrappers

## Live Collection Rule

Every sync or metadata collection task must be performed live by the LLM against official MiniMax documentation at the time of the task.

Do not write, use, or rely on scripts, scrapers, crawlers, generated parsers, SDK enum dumps, automated catalog generators, repo enum comments, or any other programmatic processing to collect model rows, capabilities, pricing, context windows, max input tokens, or max output tokens.

The LLM may use normal reading and search tools to locate official documentation, but the reviewed values must be selected and recorded by the LLM from official docs during that sync.

## Sync Steps

1. Ask the user to confirm the recency boundary. If the user does not specify one, propose the default boundary `6 months`.
2. Convert that confirmed boundary into one absolute cutoff date using the sync date.
3. Open the official MiniMax China Mainland direct-model documentation that matches the requested model kind.
4. Compare the official model list against `model-catalog.md`.
5. For every matched row, update all columns required by `../../_shared/model-catalog-schema.md`.
6. Add new official rows with the same schema.
7. Re-review rows already present in the current catalog using the same cutoff date.
8. If the user wants a curated local model set, ask the user to choose which `candidate` rows become `selected` and which selected row is the default for each model type.
9. Mark selected rows as `active` and `selected`.
10. Mark unavailable rows that were already catalog rows as `removed` instead of silently deleting them.
11. Mark rows outside the confirmed boundary as `deprecated` and `retired` even if the provider still lists them as available.
12. Collect `Context Window Tokens`, `Max Input Tokens`, and `Max Output Tokens` only when official MiniMax docs clearly expose them for the exact model row.
13. Update `pricing-matrix.md` in the same sync task using `../../_shared/pricing-matrix-schema.md`.
14. Update `request-urls.md` in the same sync task using `../../_shared/request-url-matrix-schema.md` when a provider endpoint, path, or API surface changes.
15. Update `capability-matrix.md` in the same sync task using `../../_shared/capability-matrix-schema.md`.
16. Keep `vision` empty until official rows are actually verified.
17. Keep `plan` profile chat-only even when reviewing MiniMax multimodal docs.

## Fail-Fast Rule

If the official docs do not clearly confirm a field, leave that field as `unknown`.

Do not infer support for:

- JSON object mode
- JSON schema mode
- caller-defined tools
- strict tool schemas
- parallel tool calls
- thinking budget
- reasoning effort
- seed
- image size
- image count
- duration
- context window
- max input tokens
- max output tokens
- price region
- price currency
- price unit
- price context band
- unit price

Do not infer context values from pricing tiers, observed request failures, sibling model names, repo enum comments, or non-official references.

If official docs conflict on one reviewed row or field, stop and ask the user instead of guessing.

## Output Rule

After a sync task, the skill should have:

- an updated `model-catalog.md`
- an updated `pricing-matrix.md`
- an updated `request-urls.md` when endpoint paths or base URLs changed
- an updated `capability-matrix.md`
- exact recency cutoff dates in reviewed catalog rows
- exact context window, max input, and max output fields when officially verified, otherwise `unknown`
- exact price region, currency, price unit, metered side, context band, and unit price rows in `pricing-matrix.md`
- exact official source URLs in the changed rows
- no silently deleted catalog rows
- no first-class video rows unless shared schemas were extended in the same task
