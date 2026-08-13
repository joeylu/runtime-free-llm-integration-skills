# Aliyun Bailian International Chat Transport

## Selection

- `chat-completions`: broad parameter coverage, video input, native `reasoning_content`, structured output, and function tools.
- `responses`: typed output items, `previous_response_id`, hosted tools, and `reasoning.effort`; narrower media and parameter support.
- `multimodal-generation`: DashScope-native payload; never copy OpenAI field paths directly.

## Chat Completions Shape

```json
{
  "model": "qwen3.8-max",
  "messages": [{"role": "user", "content": "..."}],
  "enable_thinking": true,
  "reasoning_effort": "medium",
  "stream": true,
  "stream_options": {"include_usage": true}
}
```

For `qwen3.8-max`, omit `thinking_budget` whenever `reasoning_effort` is present. 
## Responses Shape

```json
{
  "model": "qwen3.8-max",
  "input": "...",
  "reasoning": {"effort": "medium"},
  "stream": false
}
```

Do not send `thinking_budget`. Function outputs must immediately follow and reuse the matching `call_id`.

## DashScope Shape

```json
{
  "model": "qwen3.8-max",
  "input": {"messages": [{"role": "user", "content": [{"text": "..."}]}]},
  "parameters": {"enable_thinking": true, "reasoning_effort": "medium"}
}
```

For streaming, add `X-DashScope-SSE: enable`. Validate all optional fields against `model-parameters.md` before serialization.
