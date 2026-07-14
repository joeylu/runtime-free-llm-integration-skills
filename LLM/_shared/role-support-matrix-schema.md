# Shared Role Support Matrix Schema

Message-role behavior is keyed by:

`Provider + API Surface + API Version`

## Required Columns

| Column | Meaning |
| --- | --- |
| `Provider` | Provider key |
| `API Surface` | Exact surface |
| `API Version` | Exact version |
| `Accepted Roles` | Exact accepted input roles |
| `Developer Role` | `verified`, `unsupported`, or `unknown` |
| `System Role` | `verified`, `unsupported`, or `unknown` |
| `Assistant Tool History` | Required history fields or `n/a` |
| `Normalization Policy` | Explicit allowed transformation; `none` means fail instead of rewriting |
| `Last Verified At` | Review date |
| `Evidence Refs` | evidence-set IDs from `LLM/_evidence/evidence.json` |
| `Notes` | Constraints |

Never assume that an OpenAI-compatible endpoint accepts every OpenAI role. Role normalization must be explicit and must not change instruction precedence silently.
