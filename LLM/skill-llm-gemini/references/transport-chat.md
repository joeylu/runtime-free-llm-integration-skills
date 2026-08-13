# Gemini Chat Transport

## Interactions

```json
{
  "model": "gemini-3.6-flash",
  "input": "...",
  "generation_config": {"thinking_level": "medium"},
  "stream": false
}
```

Use `previous_interaction_id` for continuation only when the prior Interaction is reusable. Resend required tools, system instructions, and generation configuration. For structured output, use the current `response_format` schema.

## GenerateContent

Use `contents`, `systemInstruction`, `generationConfig`, and surface-specific tools. Replay the complete history, including thought signatures and function-call identity. `FunctionResponse` for Gemini 3.6 must include both `call_id` and `name`.

## Gemini 3.6 Gate

Do not send `temperature`, `top_p`, `top_k`, `candidate_count`, legacy `thinking_budget`, or prefilled model turns. Do not silently convert Interactions fields to GenerateContent paths.
