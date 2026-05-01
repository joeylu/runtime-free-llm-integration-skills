# Shared Sync Policy

Use this policy for any provider-specific `skill-llm-xxxx` model sync workflow.

Read `recency-window-policy.md` together with this file.

## Trigger Rule

Sync only when the user explicitly asks for:

- latest models
- sync
- refresh
- verification against official docs

Do not auto-sync during normal implementation work.

## Source Rule

Use official provider documentation only.

## Live Collection Rule

Every model sync or metadata collection task must be performed live by the LLM against official provider documentation at the time of the task.

Do not write, use, or rely on scripts, scrapers, crawlers, generated parsers, SDK enum dumps, automated catalog generators, or any other programmatic processing to collect model rows, capabilities, pricing, context windows, input limits, or output limits.

The LLM may use normal reading and search tools to locate official documentation, but the reviewed values must be selected and recorded by the LLM from the official docs during that sync.

## Update Rule

When syncing:

1. confirm the recency boundary with the user, proposing `6 months` by default
2. convert the confirmed boundary into one absolute cutoff date
3. update the provider skill's model catalog
4. update the provider skill's pricing matrix with region, currency, unit, metered side, context band, and unit price rows
5. update the provider skill's capability matrix
6. collect context window, max input token, and max output token values when official docs clearly expose them
7. keep removed rows visible as `deprecated` or `removed`
8. stamp exact dates, cutoff dates, and source URLs
9. use the same cutoff date to re-review existing catalog rows

## Fail-Fast Rule

If the official docs do not clearly confirm a field, leave that field as `unknown`.

Do not upgrade `unknown` to `verified` by inference.

Do not infer context windows, input limits, or output limits from pricing tiers, request failures, sibling model names, or non-official references.

Do not infer currency, region, context bands, or unit prices from unlabeled price text. If official docs do not clearly expose one pricing dimension, set that dimension to `unknown`.

If the official docs do not clearly provide a recency basis date for a row, stop and ask the user.
