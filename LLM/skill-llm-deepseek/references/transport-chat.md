# DeepSeek Chat Transport

- `SchemaVersion: 2`
- `LastReviewedAt: 2026-07-14`
- Canonical route: `text-chat@chat-completions@provider-default`
- Strict-tool route: `text-chat@beta@beta`

Resolve the profile, exact surface, API version, URL, model, and capability row before mapping any field.

## Route Boundary

| Requested behavior | Required route |
| --- | --- |
| ordinary Chat Completions | `chat-completions@provider-default` |
| strict function schema validation | `beta@beta` |

The beta route is explicit. Do not retry ordinary requests on beta, retry beta requests on ordinary Chat Completions, or infer strict support from tool support.

## Base Request Mapping

| Shared field | DeepSeek field |
| --- | --- |
| `Model` | `model` |
| `Inputs.Messages` | `messages` |
| `IsStream` | `stream` |
| `ThinkingRequested` | `thinking.type` |
| `ReasoningEffort` | `reasoning_effort` plus effective `thinking.type` |
| `Temperature` | `temperature`, non-thinking only |
| `ResponseFormat = json_object` | `response_format.type = json_object` |
| `Tools` | OpenAI-compatible function tools |
| `ToolChoice` | only when effective thinking is false and the exact row permits it |

## Thinking Resolution

- `ThinkingRequested = true` -> `thinking.type = enabled`.
- `ThinkingRequested = false` -> `thinking.type = disabled`.
- `ReasoningEffort = none` -> thinking disabled.
- `low` or `medium` -> thinking enabled with provider value `high`.
- `high` -> provider value `high`.
- `xhigh` -> provider value `max`.
- `max` -> provider value `max`.

If `ThinkingRequested` and `ReasoningEffort` disagree, stop. Do not send `ThinkingBudget`; selected V4 rows mark it unsupported.

## Thinking-Mode Request Guards

After resolving effective thinking, enforce all of these before sending:

1. Reject `ToolChoice` when thinking is enabled. DeepSeek's thinking compatibility contract does not support it.
2. Omit temperature and unsupported sampling controls when thinking is enabled.
3. For every prior assistant message that contains tool calls, preserve the provider-returned `reasoning_content` exactly.
4. Keep assistant `content` non-null in tool-call history. Use the provider-compatible empty string only when the provider returned no visible answer; never serialize JSON `null`.
5. Preserve tool-call IDs and match each tool result to the original call.

Missing or altered required history is a pre-send `invalid_continuation`/capability error, not a provider retry opportunity.

## Role Boundary

The official agent-integration compatibility notes mark the `developer` role unsupported. Normalize repository-level developer instructions into the verified provider instruction strategy before message construction; never send a `developer` message directly. Read `role-support-matrix.md` for the exact route.

## Structured Output and Tools

- `json_object` is allowed where the exact capability row permits it.
- `json_schema` remains blocked while unknown.
- Function tools are verified.
- Strict tool schemas require the `beta@beta` row and its verified URL.
- Parallel tool-call semantics remain blocked while unknown.

## Response Mapping

- `ResultKind = text-chat`
- final assistant text -> `TextContent`
- `reasoning_content` -> `ThinkingContent`
- function calls -> `ToolCalls`
- cache-hit/cache-miss and other token details -> `Usage`
- provider finish reason -> `FinishReason`
- actual route -> `Transport`

## No Alias Guessing

`deepseek-chat` and `deepseek-reasoner` are lifecycle-bound aliases recorded in `model-catalog.md`. Do not infer their target or mode from the alias name, and do not select them after their recorded provider shutdown time.

Official references:

- `https://api-docs.deepseek.com/guides/thinking_mode`
- `https://api-docs.deepseek.com/guides/tool_calls`
- `https://api-docs.deepseek.com/quick_start/agent_integrations/oh_my_pi/`
- `https://api-docs.deepseek.com/updates/`
