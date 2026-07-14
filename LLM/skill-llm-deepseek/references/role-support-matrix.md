# deepseek Role Support Matrix

- `SchemaVersion: 1`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/role-support-matrix-schema.md` first. This matrix is surface-level; exact model capability rows may narrow it further.

| Provider | API Surface | API Version | Accepted Roles | Developer Role | System Role | Assistant Tool History | Normalization Policy | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `deepseek` | `beta` | `beta` | `system,user,assistant,tool` | `unsupported` | `verified` | `preserve assistant tool_calls; when thinking, also reasoning_content and non-null content; match tool_call_id` | `developer-to-system only with explicit caller authorization; otherwise fail` | `2026-07-14` | `evset-deepseek-role-support-matrix-deepseek-beta-beta-6e20233ea0` | `Beta enables strict tool schemas but does not change role precedence.` |
| `deepseek` | `chat-completions` | `provider-default` | `system,user,assistant,tool` | `unsupported` | `verified` | `preserve assistant tool_calls; when thinking, also reasoning_content and non-null content; match tool_call_id` | `developer-to-system only with explicit caller authorization; otherwise fail` | `2026-07-14` | `evset-deepseek-role-support-matrix-deepseek-chat-completions-provider-default-14886e3d03` | `Thinking-mode compatibility rules are mandatory.` |

## Rules

- A role marked `unknown` is rejected until exact official evidence is added.
- `Normalization Policy = none` means fail instead of rewriting.
- Tool-result messages/items must preserve the provider-issued linkage ID and the preceding assistant/model call item.
- Claim details are in `../../_evidence/evidence.json`.
