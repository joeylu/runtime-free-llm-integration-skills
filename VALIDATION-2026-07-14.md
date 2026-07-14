# Validation — 2026-07-14

## Scope

Repository-wide schema v2, provider metadata, evidence, documentation, and migration consistency.

## Command

```bash
python tools/validate_repo.py
```

## Result

Passed on 2026-07-14:

```text
errors=0 warnings=0
```

Additional checks:

- `git diff --check`: passed
- README and QUICKSTART links: aligned with existing repository files
- changelog and migration notes: added

The validator checks local structure and cross-file consistency. It does not make authenticated provider requests or re-fetch every official source.
