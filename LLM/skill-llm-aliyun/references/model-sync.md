# Aliyun Model Sync

Use this workflow only when the user explicitly asks for one of these:

- latest Aliyun models
- sync model list
- verify current catalog
- remove downlisted or deprecated models
- refresh pricing or capability metadata

Read `../_shared/recency-window-policy.md` before starting.

## Source Rule

Use official Aliyun Bailian documentation only.

Do not sync from:

- blogs
- forums
- screenshots
- repo enum comments
- third-party wrappers

## Sync Steps

1. Ask the user to confirm the recency boundary. If the user does not specify one, propose the default boundary `6 months`.
2. Convert that confirmed boundary into one absolute cutoff date using the sync date.
3. Open the official Aliyun Bailian direct-model documentation that matches the requested model kind.
4. Compare the official model list against `references/model-catalog.md`.
5. For every matched row, update:
   - `Catalog Status`
   - `Selection Status`
   - `Is Default`
   - `Verification State`
   - `Recency Classification`
   - `Recency Basis Date`
   - `Recency Cutoff Date`
   - `Price Region`
   - `Price Unit`
   - `Input Price`
   - `Output Price`
   - `Pricing Note`
   - `Last Verified At`
   - `Source`
6. Add new official rows with the same schema.
7. Re-review rows already present in the current catalog using the same cutoff date.
8. If the user wants a curated local model set, ask the user to choose:
   - which `candidate` rows become `selected`
   - which selected row is the default for each model type
9. Mark selected rows as `active` and `selected`.
10. For candidate rows the user does not select, use one of these two paths:
    - if the row is retained as a catalog row, keep the full catalog schema and mark `Catalog Status = deprecated` and `Selection Status = not-selected`
    - if full schema fields were not collected, keep it only in a clearly labeled review-notes section and do not expose it to selectors or request builders
11. Mark unavailable rows that were already catalog rows as `removed` instead of silently deleting them.
12. Mark rows outside the confirmed boundary as `deprecated` and `retired` even if the provider still lists them as available.
13. Exclude pre-sync placeholders only when they were never official catalog rows; if any downstream code references them, stop and ask for a migration decision.
14. Update `references/capability-matrix.md` in the same sync task using `../_shared/capability-matrix-schema.md`.
15. Keep `music` empty until official rows are actually verified.

## Stream Evidence Rule

Do not treat `stream` like a field that always needs a model-row-specific example.

You may set `Supports Stream = verified` when either:

1. an official Aliyun page or official example explicitly shows that exact model using `stream=true`, or
2. the official Aliyun stream transport document defines stream for the callable protocol family, and an official model-family page lists that model in the same family, and no official page says stream is unsupported for that model

When using rule 2:

- record the evidence chain in the row `Notes`
- keep the evidence inside the same provider and model family
- do not carry Qwen stream evidence onto GLM, Kimi, Wan, or other families unless official docs for that family also cover stream
- if the transport doc and model-family page do not clearly match, keep `Supports Stream = unknown`

## Thinking Evidence Rule

Do not treat `thinking` like one boolean flag.

Update these fields separately:

- `Thinking Mode`
- `Thinking Default`
- `Thinking Budget Field`
- `Thinking Budget Default`

You may verify them from official:

- deep-thinking or reasoning-mode docs
- model capability tables
- parameter reference pages
- official examples that explicitly show `enable_thinking`, `thinking_budget`, or an equivalent field

Important:

- a model list that only exposes a maximum reasoning length does not by itself verify that a caller-set budget field exists
- when the docs say a mixed-thinking model defaults on or defaults off, record that in `Thinking Default`

## Temperature Evidence Rule

Do not treat `temperature` as a plain yes or no field.

Update these fields:

- `Temperature Mode`
- `Temperature Defaults`

You may verify them from official:

- parameter reference pages
- parameter default tables
- model-family docs that explicitly scope defaults by thinking or non-thinking mode

If one official row gives only one shared default, record it as `all-modes: <value>`.

## Json Object Evidence Rule

Do not treat structured output as a plain yes or no field.

Update `Json Object Mode` from official:

- structured-output docs
- model capability tables
- model-family docs that explicitly scope structured output to thinking or non-thinking mode

If the docs say "only non-thinking mode", record `Json Object Mode = non-thinking-only`. Do not collapse it to plain supported.

## Fail-Fast Rule

If the official docs do not clearly confirm a field, leave that field as `unknown`.

Do not infer support for:

- `thinking budget` field from a model-list maximum alone
- `temperature` defaults without an official parameter or defaults page
- `json_object` mode compatibility without an official structured-output or model-capability page
- `seed`
- `size`
- `duration`

Do not guess `stream` from naming, release notes alone, or similarity to another family. Only use the stream evidence rule above.

If the official docs do not clearly provide a recency basis date for one reviewed row, stop and ask the user instead of guessing whether that row is `candidate` or `retired`.

## Output Rule

After a sync task, the skill should have:

- an updated `references/model-catalog.md`
- an updated `references/capability-matrix.md`
- exact recency cutoff dates in reviewed catalog rows
- exact price region and price unit fields in selected catalog rows
- exact official source URLs in the changed rows
- no silently deleted catalog rows
- any non-catalog review-note rows clearly labeled so they cannot be mistaken for selectable catalog rows
