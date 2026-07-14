# minimax-intl Role Support Matrix

- `SchemaVersion: 1`
- `StructuralSnapshotDate: 2026-07-14`

Read `../../_shared/role-support-matrix-schema.md` first. This matrix is surface-level; exact model capability rows may narrow it further.

| Provider | API Surface | API Version | Accepted Roles | Developer Role | System Role | Assistant Tool History | Normalization Policy | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `minimax-intl` | `chat-completions` | `v1` | `user,assistant; tool-call content` | `unknown` | `unknown` | `preserve assistant tool-call content and matching tool results` | `none; reject system/developer roles unless a later exact reference verifies them` | `2026-07-14` | `evset-minimax-intl-role-support-matrix-minimax-intl-chat-completions-v1-f3471f32c5` | `Current exact endpoint page visibly verifies user/assistant and tool-call content; other roles remain fail-closed.` |
| `minimax-intl` | `image-generation` | `v1` | `n/a` | `unsupported` | `unsupported` | `n/a` | `none` | `2026-07-14` | `evset-minimax-intl-role-support-matrix-minimax-intl-image-generation-v1-e9e4bbdf00` | `No message-role envelope.` |
| `minimax-intl` | `music-generation` | `v1` | `n/a` | `unsupported` | `unsupported` | `n/a` | `none` | `2026-07-14` | `evset-minimax-intl-role-support-matrix-minimax-intl-music-generation-v1-0ec1b5f62f` | `No message-role envelope.` |

## Rules

- A role marked `unknown` is rejected until exact official evidence is added.
- `Normalization Policy = none` means fail instead of rewriting.
- Tool-result messages/items must preserve the provider-issued linkage ID and the preceding assistant/model call item.
- Claim details are in `../../_evidence/evidence.json`.
