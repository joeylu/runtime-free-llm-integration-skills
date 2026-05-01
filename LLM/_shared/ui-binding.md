# Shared UI Binding Rules

Use this file to keep platform UI logic consistent across Unity, web, app, and backend admin tools.

## Common Controls

| Control | Show When |
| --- | --- |
| connection profile selector | more than one active profile exists for the provider |
| provider selector | more than one active provider exists for the same vendor family, such as Aliyun Bailian China Mainland and International |
| model dropdown | always |
| stream toggle | capability matrix verifies stream |
| thinking toggle | `Thinking Mode = mixed` and the provider uses a boolean thinking control |
| thinking budget input | the resolved request uses thinking and `Thinking Budget Field = verified` |
| reasoning effort selector | `Reasoning Effort Field = verified` |
| reasoning summary selector | `Reasoning Summary Field = verified` |
| temperature control | `Temperature Mode` is not `unsupported`, `unknown`, or `n/a` |
| response format control | `Json Object Mode` or `Json Schema Mode` is not `unsupported`, `unknown`, or `n/a` |
| schema editor | `Json Schema Mode` is compatible with the resolved thinking state |
| tool/function editor | `Tool Calling Mode` is compatible with the resolved thinking state |
| strict tool schema toggle | `Strict Tool Schema Mode = verified` |
| parallel tool calls toggle | `Parallel Tool Calls = verified` |
| image picker | `RequestKind = vision` or imaging edit flow |
| seed input | capability matrix verifies seed |
| size input | capability matrix verifies size |
| image count input | `RequestKind = imaging` and capability matrix verifies output image count |
| duration input | capability matrix verifies duration |
| cancel button | cancellation is safe on that host surface |

## Binding Rules

- Bind model dropdown text to `API Model`.
- Bind model dropdown value to `API Model`.
- Bind connection profile text to `Display Name`.
- Bind connection profile value to `Profile Key`.
- Bind provider selection to the exact provider identifier, not only to a vendor display name.
- Bind progress UI to the shared progress contract, not raw provider payloads.
- Bind error banners, toasts, or dialogs to the shared error contract.
- In production UI, hide unsupported controls instead of rendering dead controls.
- In debug, admin, or integration-test UI, prefer disabled controls with a reason so the user can see which capability blocked the option.
- If capability state is `unknown`, either hide the control or block with an explicit explanation. Do not guess.
- If the selected connection profile restricts request kind, model, surface, or feature, hide or disable the blocked control with the profile reason.
- If the request URL row is `unknown` or missing for the selected provider/profile/surface, block the request before showing a test-connection success state.
- If `Reasoning Effort Field = verified`, prefer the reasoning effort selector over a boolean thinking toggle.
- If `Thinking Default = on` and `Json Object Mode = non-thinking-only`, do not silently flip thinking off when the user picks strict JSON. Block and explain that JSON requires explicitly disabling thinking.
- If `Temperature Mode`, `Json Object Mode`, `Json Schema Mode`, or `Tool Calling Mode` depends on the effective thinking state, bind the control to that state instead of treating it as a static yes-or-no field.
- If a provider uses `ReasoningEffort`, expose the provider's official values and map them to effective thinking before showing mode-sensitive controls.

## Result Panels

- Render `TextContent` for `chat` and `vision`.
- Render `StructuredContent` for verified schema outputs.
- Render `ToolCalls` when the model asks the app to call caller-defined tools.
- Render `ImageOutputs` for `imaging`.
- Render `AudioOutputs` for `music`.
- Render usage, latency, and finish reason in a secondary diagnostics area when the caller wants debugging visibility.
