# Shared Recency Window Policy

Use this policy for any provider skill that syncs model catalogs from official docs.

## Boundary Confirmation Rule

When the user asks to sync models, ask the user to confirm a recency boundary first.

Default proposal:

- `6 months`

Do not start sync until the user either:

- confirms the default boundary, or
- gives a different boundary

## Cutoff Rule

Convert the confirmed boundary into one absolute cutoff date based on the sync date.

Example:

- sync date: `2026-04-24`
- boundary: `6 months`
- cutoff date: `2025-10-24`

Use absolute dates in the catalog after sync. Do not keep only relative wording such as `half year`.

## Classification Rule

For each model row reviewed during sync:

- if the official recency basis date is on or after the cutoff date, classify it as `candidate`
- if the official recency basis date is before the cutoff date, classify it as `retired`

Use the same cutoff date to review:

- newly discovered official rows
- rows already present in the current catalog

## Basis-Date Rule

Use one clear official date for the recency decision.

Preferred basis date order:

1. official model release date
2. official model availability date
3. official model page update date only when it clearly refers to that exact model row

If the official docs do not clearly provide a suitable basis date for a row, stop and ask the user instead of guessing.

## Selector Rule

Rows classified as `retired` should not remain user-selectable.

Provider skills may express this by marking the local catalog row as `deprecated` while keeping the historical record visible.
