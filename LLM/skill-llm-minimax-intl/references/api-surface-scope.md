# MiniMax International API Surface Scope

| API Surface | Scope Status | Models | Default-Thinking Rule Inherited | Source | Notes |
| --- | --- | --- | --- | --- | --- |
| `chat-completions` | `maintained` | `MiniMax-M3` | `yes; adaptive is equivalent to thinking on for M3 on this exact surface` | `https://platform.minimax.io/docs/api-reference/text-chat-openai` | `capability and transport rows exist` |
| `responses` | `explicitly-out-of-scope` | `MiniMax-M3` | `no` | `https://platform.minimax.io/docs/api-reference/responses-create` | `requires independent route, capability, defaults, and serializer evidence before enablement` |
| `anthropic-compatible` | `explicitly-out-of-scope` | `MiniMax-M3` | `no` | `https://platform.minimax.io/docs/api-reference/text-anthropic-api` | `requires independent route, capability, defaults, and serializer evidence before enablement` |
| `text-chatcompletion-v2` | `deprecated` | `M2.x family` | `no` | `https://platform.minimax.io/docs/api-reference/text-post` | `do not use for M3 integration` |
