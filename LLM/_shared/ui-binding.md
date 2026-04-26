# Shared UI Binding Rules

Use this file to keep platform UI logic consistent across Unity, web, app, and backend admin tools.

## Common Controls

| Control | Show When |
| --- | --- |
| model dropdown | always |
| stream toggle | capability matrix verifies stream |
| thinking toggle | `Thinking Mode = mixed` |
| thinking budget input | the resolved request uses thinking and `Thinking Budget Field = verified` |
| temperature control | `Temperature Mode` is not `unsupported`, `unknown`, or `n/a` |
| response format control | `Json Object Mode` is not `unsupported`, `unknown`, or `n/a` |
| image picker | `RequestKind = vision` or imaging edit flow |
| seed input | capability matrix verifies seed |
| size input | capability matrix verifies size |
| image count input | capability matrix verifies image count |
| duration input | capability matrix verifies duration |
| cancel button | cancellation is safe on that host surface |

## Binding Rules

- Bind dropdown text to `UI Label`.
- Bind dropdown value to `API Model`.
- Bind progress UI to the shared progress contract, not raw provider payloads.
- Bind error banners, toasts, or dialogs to the shared error contract.
- In production UI, hide unsupported controls instead of rendering dead controls.
- In debug, admin, or integration-test UI, prefer disabled controls with a reason so the user can see which capability blocked the option.
- If capability state is `unknown`, either hide the control or block with an explicit explanation. Do not guess.
- If `Thinking Default = on` and `Json Object Mode = non-thinking-only`, do not silently flip thinking off when the user picks strict JSON. Block and explain that JSON requires explicitly disabling thinking.
- If `Temperature Mode` or `Json Object Mode` depends on the effective thinking state, bind the control to that state instead of treating it as a static yes-or-no field.

## Result Panels

- Render `TextContent` for `chat` and `vision`.
- Render `ImageOutputs` for `imaging`.
- Render `AudioOutputs` for `music`.
- Render usage, latency, and finish reason in a secondary diagnostics area when the caller wants debugging visibility.
