# Agent Commands

These are natural-language workflow intents, not executable command names.

## Composition Rule

Commands form this default dependency graph:

```text
sync -> audit -> implement
          \-> init
add-provider -> audit
split-provider -> audit
```

Run all clearly requested compatible stages in dependency order. Do not ask the user to choose merely because a request matches multiple commands. Ask only when a material boundary is genuinely ambiguous, such as provider, region, profile, requested request kind, or whether a breaking default change is intended.

No command overrides provider `SKILL.md`, shared schemas, official-evidence rules, or fail-fast behavior.

## Index

| Command | Common Phrases | Result |
| --- | --- | --- |
| `list-commands` | help, commands, available workflows | Summarize workflows without executing them |
| `init` | initialize, start integration, set up | Resolve a provider integration plan from the current curated snapshot |
| `implement` | build, wire, integrate, apply | Modify a host project using resolved provider contracts |
| `sync` | latest, refresh, re-verify, update models | Review official sources and update claims and dependent matrices |
| `audit` | review, verify, check, clean docs | Check semantic, structural, path, evidence, and cross-file consistency |
| `add-provider` | add provider, support another provider | Add a provider skill using the shared schemas |
| `split-provider` | separate regions, split commercial entries | Split mixed regional/commercial boundaries into distinct skills |

## `init`

1. Identify provider, region, host surface, request kinds, and whether UI/backend work is required.
2. Read the selected provider `SKILL.md` and its declared order.
3. Resolve profile, selected model, surface/version, route, capability, role, and regional scope.
4. Produce an implementation plan using only verified current rows.

Do not perform live sync unless requested or required evidence is stale/missing.

## `implement`

1. Use the resolved provider boundary and canonical request kind.
2. Reject unknown, unsupported, stale, conflicted, or profile-disallowed fields before writing request code.
3. Map through the provider transport and shared request/response/error/progress/logging contracts.
4. Never silently change provider, region, profile, model, surface, version, route, stream mode, or tool type after an error.
5. Run host-project tests and repository validation when repository files change.

## `sync`

1. Define provider, region, request kinds, surfaces/versions, and pricing scopes.
2. Use the shared default discovery lookback when none is supplied; this is research metadata, not lifecycle state.
3. Read official sources with the precedence in `LLM/_shared/sync-policy.md`.
4. Update `LLM/_evidence/evidence.json` first.
5. Update catalog, URL, capability, role, pricing, profile, and transport files together when affected.
6. Keep new candidates not selected unless repository-owner intent says otherwise.
7. Preserve unresolved conflicts and fail closed.
8. Run `python tools/validate_repo.py`.

## `audit`

Check at least:

- required provider files and schemas;
- orthogonal lifecycle/selection/freshness state;
- exact surface/version keys without comma-combined values;
- selected-model coverage across profiles, URLs, capabilities, roles, prices, and transports;
- regional/deployment pricing scope and effective windows;
- moving aliases and shutdown deadlines;
- evidence references, official domains, dates, and conflicts;
- relative paths, Markdown table shapes, YAML, and stale legacy language;
- validator result and diff review.

An audit may follow a sync automatically.

## `add-provider`

1. Create `LLM/skill-llm-<provider>/` with `SKILL.md`, `agents/openai.yaml`, and the standard reference set.
2. Declare regional/commercial scope and `CoverageMode`.
3. Add exact profile, route, capability, role, pricing, transport, and evidence contracts.
4. Keep all unverified fields fail-closed.
5. Audit the result.

## `split-provider`

1. Name each regional/commercial provider explicitly.
2. Move endpoint, credential, availability, model, price, and evidence data into the correct boundary.
3. Remove silent cross-region fallback and update all references.
4. Preserve migration notes for old identifiers.
5. Audit the result.
