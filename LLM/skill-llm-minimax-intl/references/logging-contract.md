# MiniMax International Logging Contract

Read `../../_shared/logging-fields.md` first.

## Provider-Specific Fields

Add these fields when available:

| Field | Meaning |
| --- | --- |
| `minimax_region` | `international` |
| `minimax_response_id` | provider response id when present |
| `minimax_reasoning_split` | whether thinking content was extracted from MiniMax think tags |
| `minimax_task_id` | H3 task ID; also map to normalized `job_id` |
| `minimax_task_type` | `generation`, `h3_context_ir`, or `regeneration` |
| `minimax_task_status` | `queued`, `running`, `succeeded`, `failed`, or `cancelled` |
| `minimax_video_resolution` | returned `768P` or `2K` when present |
| `minimax_video_duration_seconds` | returned video duration when present |
| `minimax_video_ratio` | returned output ratio when present |

## Rules

- Log normalized shared fields first.
- Redact API keys and bearer tokens.
- Do not log raw prompts, raw responses, extracted thinking content, original H3 content arrays, input media URLs, callback URLs, or H3 result URLs unless the host explicitly enables protected diagnostic snapshots.
- Do not log MiniMax China Mainland traffic under `provider = minimax-intl`.
