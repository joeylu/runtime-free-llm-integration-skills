# aliyun-bailian-intl Role Support Matrix

- `SchemaVersion: 1`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/role-support-matrix-schema.md` first. This matrix is surface-level; exact model capability rows may narrow it further.

| Provider | API Surface | API Version | Accepted Roles | Developer Role | System Role | Assistant Tool History | Normalization Policy | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `aliyun-bailian-intl` | `chat-completions` | `compatible-mode-v1` | `system,user,assistant,tool` | `unknown` | `verified` | `preserve assistant tool_calls and matching tool_call_id` | `none; reject developer unless exact model documentation verifies it` | `2026-07-14` | `evset-aliyun-bailian-intl-role-support-matrix-aliyun-bailian-intl-chat-completions-compatible-mode-v1-ff149efb4a` | `Official compatible Chat documents system/user/assistant; tool history is required for tool responses.` |
| `aliyun-bailian-intl` | `dashscope-native` | `native-v1` | `n/a` | `unsupported` | `unsupported` | `n/a` | `none` | `2026-07-14` | `evset-aliyun-bailian-intl-role-support-matrix-aliyun-bailian-intl-dashscope-native-native-v1-24ce3c25a5` | `No shared message-role contract for the unselected music route.` |
| `aliyun-bailian-intl` | `dashscope-native-async` | `native-v1` | `n/a` | `unsupported` | `unsupported` | `n/a` | `none` | `2026-07-14` | `evset-aliyun-bailian-intl-role-support-matrix-aliyun-bailian-intl-dashscope-native-async-native-v1-143df69d77` | `No message-role envelope.` |
| `aliyun-bailian-intl` | `dashscope-native-sync` | `native-v1` | `n/a` | `unsupported` | `unsupported` | `n/a` | `none` | `2026-07-14` | `evset-aliyun-bailian-intl-role-support-matrix-aliyun-bailian-intl-dashscope-native-sync-native-v1-ee797ecf2c` | `No message-role envelope.` |
| `aliyun-bailian-intl` | `responses` | `compatible-mode-v1` | `user,assistant; typed function call/output items` | `unknown` | `verified` | `preserve response items, call IDs, and function outputs` | `use top-level instructions; do not synthesize developer role` | `2026-07-14` | `evset-aliyun-bailian-intl-role-support-matrix-aliyun-bailian-intl-responses-compatible-mode-v1-33dcc8131c` | `OpenAI-compatible Responses route; exact provider fields still govern.` |

## Rules

- A role marked `unknown` is rejected until exact official evidence is added.
- `Normalization Policy = none` means fail instead of rewriting.
- Tool-result messages/items must preserve the provider-issued linkage ID and the preceding assistant/model call item.
- Claim details are in `../../_evidence/evidence.json`.
