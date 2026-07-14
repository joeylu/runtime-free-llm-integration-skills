# Aliyun Bailian International / Singapore Capability Matrix

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Key: `Request Kind + API Model + API Surface + API Version`

Read `../../_shared/capability-matrix-schema.md` first. Each row covers one exact surface and one exact API version. `unknown` and `unsupported` both block a requested option; `unsupported` means the official contract explicitly excludes it.

The matrix contains selected rows and, where explicitly labeled in the catalog, reviewed candidates. A capability row never makes a model locally selectable by itself.

## Current Matrix

| Request Kind | API Model | API Surface | API Version | Supports Non-Stream | Supports Stream | Thinking Mode | Thinking Default | Thinking Budget Field | Thinking Budget Default | Temperature Mode | Temperature Defaults | Json Object Mode | Json Schema Mode | Tool Calling Mode | Strict Tool Schema Mode | Parallel Tool Calls | Tool Choice When Thinking | Required Tool-History Fields | Reasoning Effort Field | Reasoning Effort Values | Reasoning Summary Field | Reasoning Output Visibility | Supports Image Input | Supports Seed | Supports Image Size | Supports Image Count | Supports Duration Seconds | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `qwen3.7-max` | `chat-completions` | `compatible-mode-v1` | `verified` | `verified` | `mixed` | `on` | `verified` | `model maximum; exact value not exposed outside the console model card` | `all-modes` | `thinking: 0.6; non-thinking: 0.7` | `unsupported` | `unknown` | `unknown` | `unknown` | `unknown` | `unknown` | `n/a` | `n/a` | `n/a` | `unknown` | `raw` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `evset-aliyun-bailian-intl-capability-matrix-text-chat-qwen3-7-max-chat-completions-compatible-mode-v1-f3dca621f1` | `Chat Completions surface: non-stream and stream are verified; qwen3.7-max is mixed-thinking and defaults on; thinking_budget, preserve_thinking, temperature defaults, and raw reasoning_content are documented; structured output is explicitly unsupported; model-level Function Calling is listed, but mode-specific caller-defined tool compatibility is not explicit, so Tool Calling Mode remains unknown; the alias resolves to the text-only 2026-05-20 snapshot` |
| `text-chat` | `qwen3.7-max` | `responses` | `compatible-mode-v1` | `verified` | `verified` | `mixed` | `medium` | `unsupported` | `n/a` | `all-modes` | `range: [0,2); default not documented` | `unsupported` | `unsupported` | `all-modes` | `unsupported` | `unsupported` | `unknown` | `n/a` | `verified` | `none,minimal,low,medium,high` | `verified` | `summary` | `n/a` | `n/a` | `n/a` | `n/a` | `n/a` | `evset-aliyun-bailian-intl-capability-matrix-text-chat-qwen3-7-max-responses-compatible-mode-v1-77ce4d7860` | `Responses: qwen3.7-max is in the Singapore supported-model list; non-stream and stream, custom functions, tool_choice, temperature, previous_response_id, store, and Session Cache are documented; response_format, strict schemas, and parallel-tool request control are not listed and are blocked; reasoning defaults to medium and is exposed as summary items; code_interpreter requires reasoning enabled for qwen3.7-max` |

## Resolution Rule

Resolve the connection profile, exact surface, exact API version, and effective thinking state before reading this table. Do not merge capabilities across rows or retry on another surface/version without a new explicit selection. Claim details are in `../../_evidence/evidence.json`.
