# Shared Official Sync Policy

This policy separates **official fact collection** from **repository validation**.

## Trigger

Perform an official sync when the user asks for current/latest information, refresh, re-verification, or provider/model updates. Normal implementation may use the current snapshot but must respect row freshness and fail-closed rules.

## Sources

Use official provider sources only for provider facts. A source must be HTTPS and owned by the provider or its official cloud documentation domain.

Source precedence for conflicting facts:

1. exact endpoint/API reference for request fields and conditional validity;
2. exact model card for model ID, modalities, limits, and stability label;
3. official pricing page for regional price and effective windows;
4. official lifecycle/deprecation page for shutdown and replacement;
5. official release notes/changelog for release date and alias history;
6. official examples/migration guides for recommended usage.

When two authoritative sources still conflict, record both claims with `conflict_state = open`, set the affected field to `unknown` or `conflicted`, and fail closed.

## Collection Methods

Automated extraction, scripts, official machine-readable indexes, and SDK/schema inspection are allowed to improve repeatability, but they are not evidence by themselves unless the provider publishes them as official documentation.

Every extracted value must be:

- traceable to an official URL and locator;
- reviewed before promotion to `verified`;
- recorded in `LLM/_evidence/evidence.json`;
- compared against existing values and effective windows.

Prohibited behavior is unsupported inference, not automation. Do not infer facts from names, neighboring models, pricing bands, third-party registries, runtime errors, or examples that do not define the field.

## Sync Order

1. Identify provider, region, request kinds, and desired discovery scope.
2. Establish an absolute discovery cutoff; use the repository default when the user did not specify one.
3. Review exact model IDs and provider lifecycle.
4. Review aliases and fixed targets.
5. Review API surfaces and versions.
6. Review request fields and capabilities.
7. Review limits while preserving official display values.
8. Review regional/deployment pricing and effective windows.
9. Update claim-level evidence first.
10. Update provider catalogs/matrices from reviewed claims.
11. Run structural validation and inspect the diff.

## Fail-Closed Rules

- Keep unclear facts `unknown`.
- Do not convert `K`/`M` displays to exact integers without an official unit convention.
- Do not use an expired promotion for current estimates.
- Do not treat a local replacement as provider deprecation.
- Do not treat a recent-release cutoff as a selector rule.
- Do not silently change a default model, region, profile, surface, or API version.
