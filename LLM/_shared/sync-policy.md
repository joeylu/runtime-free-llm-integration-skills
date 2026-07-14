# Model Sync Policy

Use this policy only when the user requests model or API verification.

## 1. Clear Replacement

When an already documented model has a clear newer version in the same provider series, replace it throughout:

- `model-catalog.md`
- `capability-matrix.md`
- `pricing-matrix.md`
- `request-urls.md` when routing changes
- transport rules and examples

Keep the former identifier only in a dated migration note.

## 2. Unrelated New Model

When an official model has no documented predecessor in this repository, ask the user whether to add it.

## 3. Regional Providers

For paired regional skills, verify the replacement in each region during the same update. Apply only facts supported by that region's official documentation; never copy availability, pricing, endpoint, or capability claims from the other region.

## 4. Sources

Use official model pages, API references, examples, pricing pages, and lifecycle notices. Record the exact source URL on the affected row. Keep any unverified value as `unknown`.
