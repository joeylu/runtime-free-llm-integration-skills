# MiniMax China Mainland Logging Contract

Read `../../_shared/logging-fields.md` first.

## Provider-Specific Fields

Add these fields when available:

| Field | Meaning |
| --- | --- |
| `minimax_region` | `china-mainland` |
| `minimax_response_id` | provider response id when present |
| `minimax_reasoning_split` | whether thinking content was extracted from MiniMax think tags |

## Rules

- Log normalized shared fields first.
- Redact API keys and bearer tokens.
- Do not log raw prompts, raw responses, or extracted thinking content unless the host explicitly enables diagnostic snapshots.
- Do not log MiniMax International traffic under `provider = minimax-cn`.
