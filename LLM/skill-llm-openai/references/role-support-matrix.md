# openai Role Support Matrix

- `SchemaVersion: 1`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/role-support-matrix-schema.md` first. This matrix is surface-level; exact model capability rows may narrow it further.

| Provider | API Surface | API Version | Accepted Roles | Developer Role | System Role | Assistant Tool History | Normalization Policy | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `openai` | `chat-completions` | `v1` | `developer,system,user,assistant,tool` | `verified` | `verified` | `preserve assistant tool_calls and matching tool_call_id` | `none` | `2026-07-14` | `evset-openai-role-support-matrix-openai-chat-completions-v1-9ae98ba7fd` | `Developer/system priority is surface-defined; preserve order and IDs.` |
| `openai` | `image-api-edits` | `v1` | `n/a` | `unsupported` | `unsupported` | `n/a` | `none` | `2026-07-14` | `evset-openai-role-support-matrix-openai-image-api-edits-v1-1cbdcaaac4` | `No message-role envelope on this endpoint.` |
| `openai` | `image-api-generations` | `v1` | `n/a` | `unsupported` | `unsupported` | `n/a` | `none` | `2026-07-14` | `evset-openai-role-support-matrix-openai-image-api-generations-v1-e42bf611e2` | `No message-role envelope on this endpoint.` |
| `openai` | `responses` | `v1` | `user,assistant; typed function_call/function_call_output items` | `verified` | `verified` | `preserve typed response items, call IDs, and function-call outputs` | `prefer top-level instructions; preserve transcript roles; no silent role rewrite` | `2026-07-14` | `evset-openai-role-support-matrix-openai-responses-v1-85cbf73d21` | `Responses uses instructions plus typed input/output items.` |

## Rules

- A role marked `unknown` is rejected until exact official evidence is added.
- `Normalization Policy = none` means fail instead of rewriting.
- Tool-result messages/items must preserve the provider-issued linkage ID and the preceding assistant/model call item.
- Claim details are in `../../_evidence/evidence.json`.
