# Quickstart

1. Choose the provider and region.
2. Read that provider's `SKILL.md` in its stated order.
3. Match the requested model in `model-catalog.md`.
4. Resolve the connection profile and exact full route row in `request-urls.md`, including API version and endpoint kind.
5. Check the exact full route key in `capability-matrix.md`.
6. Apply the matching transport and shared request, response, error, progress, and logging contracts.

Example:

```text
Use LLM/skill-llm-aliyun-bailian-cn/SKILL.md.
Integrate glm-5.2 through the documented Chat Completions surface.
Follow the exact capability and transport rules; do not switch regions or models silently.
```

When updating models, follow `LLM/_shared/sync-policy.md`: replace clear successors, ask before adding unrelated models, verify paired regions independently, and update dependent runtime rules together.
