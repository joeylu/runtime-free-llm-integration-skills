# Shared Error Contract

Use this contract for every `skill-llm-xxxx` integration.

## Error Fields

| Field | Meaning |
| --- | --- |
| `ErrorCode` | Stable machine-friendly error code |
| `UserMessage` | Short user-facing error text |
| `DebugMessage` | More exact engineering detail |
| `Retryable` | Whether retry is usually meaningful |
| `Stage` | Where the error happened |
| `ProviderCode` | Raw provider code when available |
| `ProviderRequestId` | Raw provider request id when available |

## Standard Error Codes

| Error Code | Meaning |
| --- | --- |
| `config_error` | Local configuration is missing or invalid |
| `validation_error` | The request is invalid before sending |
| `capability_unverified` | Requested feature is not verified in the capability matrix |
| `unsupported_option` | The documented model or request kind does not support the option |
| `auth_error` | Authentication failed |
| `network_error` | Network transport failed |
| `request_url_error` | Request URL is missing, unknown, incompatible, or unsafe |
| `timeout_error` | Request or job exceeded timeout |
| `rate_limit_error` | Provider throttled the request |
| `provider_error` | Provider returned a non-success response |
| `parse_error` | Response shape could not be parsed safely |
| `empty_result_error` | Provider returned no usable result |
| `canceled` | Caller canceled the request |

## Standard Stages

Use one of these stage keys:

- `validating`
- `preparing`
- `resolving-request-url`
- `sending`
- `submitting-job`
- `waiting-provider-accept`
- `waiting-first-byte`
- `streaming`
- `waiting-result`
- `polling-job`
- `downloading-result`
- `local-processing`

## Rules

- Raise explicit errors instead of silent fallbacks.
- Keep `UserMessage` short and stable.
- Put provider-specific details in `DebugMessage` and `ProviderCode`.
- Use `capability_unverified` when the skill lacks proof, not only when the provider says no.

## Example

If the caller asks for `thinking` on a row marked `unknown`, emit `ErrorCode = capability_unverified` at `Stage = validating`.
