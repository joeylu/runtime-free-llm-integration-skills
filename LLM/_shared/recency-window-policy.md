# Shared Discovery and Review Freshness Policy

A recency window is a **discovery aid**, not a provider lifecycle rule.

## Defaults

- Default discovery lookback: `6 months`.
- Default factual review freshness target: `90 days` unless a provider file declares a shorter target.
- Price, alias, API-version, and lifecycle claims should be reviewed sooner whenever their official source is known to change frequently.

## Discovery Window

When a user asks for a current-model sync and does not give a boundary, an agent may use the repository default without blocking the task. Convert it to one absolute cutoff date and record it in the sync report.

Use the window to prioritize newly released or newly available models. Do not:

- mark an older model deprecated merely because it predates the cutoff;
- remove a selected model merely because a newer model exists;
- treat absence from a recent-release page as proof of shutdown.

## Review Freshness

Set:

- `current` when the row's evidence was reviewed within the provider's freshness target and no newer conflicting official source is known;
- `stale` when the target is exceeded or a volatile claim has passed its effective window;
- `unreviewed` when no explicit official review exists.

A stale row is blocked by the selector, but its `Provider Lifecycle` remains unchanged until official lifecycle evidence says otherwise.

## Lifecycle Evidence

Use an official lifecycle/deprecation page for `scheduled-deprecated`, `deprecated`, `shutdown`, or `removed` whenever one exists. Release age, local replacement, pricing absence, and catalog omission are not lifecycle evidence.

Future provider shutdown dates are valid factual dates. Store them in `Provider Shutdown At` and keep the row `scheduled-deprecated` until the deadline. After the deadline, re-verify the provider state before changing it to `shutdown` or `removed`.
