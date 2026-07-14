# Gemini Logging Contract

Apply `../../_shared/logging-fields.md` first. Log normalized values before provider-specific extras.

## Minimum Gemini Fields

In addition to the shared minimum, record:

- `api_surface`
- `interaction_id_returned` as a boolean by default, not the opaque ID
- `previous_interaction_id_present`
- `store_response_effective`
- `state_mode = stateful | stateless | history-replay`
- `thinking_level_effective`
- `thought_signature_present`
- `thought_summary_present`
- `thinking_summaries_effective = auto | omitted`
- `sampling_override_rejected`
- `function_call_count`
- `function_result_count`
- `function_identity_validated`
- `hosted_tool_types`
- `interaction_step_types`
- `cache_mode`
- `cached_input_tokens` from Interactions `usage.total_cached_tokens` or GenerateContent `usageMetadata.cachedContentTokenCount`
- `thought_tokens` from Interactions `usage.total_thought_tokens` or GenerateContent `usageMetadata.thoughtsTokenCount`
- `safety_surface`
- `response_format_surface`
- `inline_image_output_count`
- `provider_finish_reason`

## Streaming Extras

For Interactions, record the observed step-event types and terminal state. For StreamGenerateContent, record candidate chunk count and terminal finish reason. Never merge the two protocols under an ambiguous parser label.

## Privacy and Retention

- Do not log API keys, raw continuation IDs, thought signatures, raw prompts, files, images, function arguments, or generated images by default.
- A request with `store=true` has provider-side retention implications. Log the effective boolean and profile policy.
- Raw payload snapshots require explicit owner approval and redaction.
- Grounding annotations may contain URLs or snippets; apply the host application's data-retention policy.

## Diagnostic Warnings

Record warnings for:

- Preview capability use
- structured output combined with tools
- the current official Computer Use documentation conflict
- omitted continuation because `store=false`
- empty GenerateContent output after a mismatched function-result round
- attempted sampling override blocked by `provider-default-only`
