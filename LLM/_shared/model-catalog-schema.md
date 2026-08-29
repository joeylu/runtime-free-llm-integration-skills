# Shared Model Catalog Schema

A provider catalog lists the models for which that skill maintains runtime integration rules. `Model Type` remains as a compatibility alias for `RequestKind`; machine-readable operation and modality fields carry the actual model semantics.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Model Type` | compatibility request kind: `chat`, `vision`, `imaging`, `music`, `speech`, or `transcription` |
| `Operation` | `text-generation`, `multimodal-understanding`, `image-generation`, `music-generation`, `speech-generation`, or `speech-transcription` |
| `Input Modalities` | comma-separated exact maintained inputs such as `text,image,video,audio,pdf` |
| `Output Modalities` | comma-separated maintained outputs such as `text`, `image`, or `audio` |
| `Flow Kind` | maintained task flow, for example `chat`, `vision`, `text-to-image`, or `image-edit` |
| `API Model` | exact provider model identifier sent over the wire |
| `Status` | `active`, `preview`, or `deprecated` |
| `Identifier Kind` | `opaque-provider-id`, `moving-alias`, `fixed-snapshot`, or `preview-id` |
| `Resolves To` | documented snapshot target for a moving alias, otherwise `n/a` or `unknown` |
| `Effective From` | documented activation date/time, `unknown`, or `n/a` |
| `Deprecates At` | documented deprecation date/time, `unknown`, or `n/a` |
| `Retires At` | documented retirement date/time, `unknown`, or `n/a` |
| `Replacement Model` | documented replacement, `unknown`, or `n/a` |
| `Region Scope` | exact region scope for this provider skill |
| `Context Window Tokens` | official context window, `n/a`, or `unknown` |
| `Max Input Tokens` | official input limit, `n/a`, or `unknown` |
| `Max Output Tokens` | official output limit, `n/a`, or `unknown` |
| `Notes` | short model-specific runtime fact |
| `Last Verified At` | absolute verification date or `unverified` |
| `Source` | exact official model or API source URL |

## Rules

- Use exact provider model IDs.
- Keep one row per request kind when the same model has distinct chat and vision rules.
- Do not infer input modalities from a marketing label; record only the maintained flow verified by this skill.
- A moving alias must record `Resolves To` when the provider publishes the current target.
- Keep lifecycle dates as `unknown` rather than inferring them.
- A model row must have at least one matching full-route capability row.
- Replace a documented model only under `sync-policy.md` and update all dependent files in the same change.
