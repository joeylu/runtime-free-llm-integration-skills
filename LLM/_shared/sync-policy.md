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

## Update Rule

When syncing:

1. confirm the recency boundary with the user, proposing `6 months` by default
2. convert the confirmed boundary into one absolute cutoff date
3. update the provider skill's model catalog
4. update the provider skill's capability matrix
5. keep removed rows visible as `deprecated` or `removed`
6. stamp exact dates, cutoff dates, and source URLs
7. use the same cutoff date to re-review existing catalog rows

## Fail-Fast Rule

If the official docs do not clearly confirm a field, leave that field as `unknown`.

Do not upgrade `unknown` to `verified` by inference.

If the official docs do not clearly provide a recency basis date for a row, stop and ask the user.
