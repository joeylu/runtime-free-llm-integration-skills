# MiniMax Chat Transport

## OpenAI-Compatible

```json
{
  "model": "MiniMax-M3",
  "messages": [{"role":"user","content":"..."}],
  "thinking": {"type":"adaptive"},
  "reasoning_split": true,
  "max_completion_tokens": 131072,
  "stream": true,
  "stream_options": {"include_usage": true}
}
```

Omitting `thinking` keeps it on. `reasoning_split` only changes output layout; its omission default is undocumented.

## Anthropic-Compatible

Use `/anthropic/v1/messages`, Anthropic content blocks, and `max_tokens`. Thinking is off when omitted; use `thinking:{"type":"adaptive"}` to enable. Do not copy OpenAI defaults or `reasoning_split` into this surface.
