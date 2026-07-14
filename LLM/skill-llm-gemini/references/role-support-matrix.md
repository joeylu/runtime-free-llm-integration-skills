# gemini Role Support Matrix

- `SchemaVersion: 1`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/role-support-matrix-schema.md` first. This matrix is surface-level; exact model capability rows may narrow it further.

| Provider | API Surface | API Version | Accepted Roles | Developer Role | System Role | Assistant Tool History | Normalization Policy | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `gemini` | `generate-content` | `v1beta` | `user,model,function` | `unsupported` | `verified` | `preserve model functionCall followed by function role FunctionResponse` | `map shared Instructions to system_instruction; reject developer-role messages` | `2026-07-14` | `evset-gemini-role-support-matrix-gemini-generate-content-v1beta-5f06214ee5` | `Content roles differ from OpenAI messages.` |
| `gemini` | `interactions` | `v1` | `user,model; typed function call/response items` | `unsupported` | `verified` | `preserve interaction steps and function call/response linkage` | `map shared Instructions to system_instruction; reject developer-role messages` | `2026-07-14` | `evset-gemini-role-support-matrix-gemini-interactions-v1-7a33292bbc` | `Stable Interactions v1.` |
| `gemini` | `interactions` | `v1beta` | `user,model; typed function call/response items` | `unsupported` | `verified` | `preserve interaction steps and function call/response linkage` | `map shared Instructions to system_instruction; reject developer-role messages` | `2026-07-14` | `evset-gemini-role-support-matrix-gemini-interactions-v1beta-fc2ae851ba` | `Explicit compatibility version.` |
| `gemini` | `stream-generate-content` | `v1beta` | `user,model,function` | `unsupported` | `verified` | `preserve model functionCall followed by function role FunctionResponse` | `map shared Instructions to system_instruction; reject developer-role messages` | `2026-07-14` | `evset-gemini-role-support-matrix-gemini-stream-generate-content-v1beta-bdf65ae44c` | `Streaming uses the same content-role contract.` |

## Rules

- A role marked `unknown` is rejected until exact official evidence is added.
- `Normalization Policy = none` means fail instead of rewriting.
- Tool-result messages/items must preserve the provider-issued linkage ID and the preceding assistant/model call item.
- Claim details are in `../../_evidence/evidence.json`.
