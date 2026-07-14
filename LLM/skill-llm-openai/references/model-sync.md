# Model Update

Use this file when the user requests a model or API update.

## Official Sources

- `https://developers.openai.com/api/docs/models`
- `https://developers.openai.com/api/docs/pricing`
- `https://developers.openai.com/api/docs/changelog`

## Update Steps

1. Identify whether the change is a clear replacement for a model already documented here.
2. Verify the exact model ID, region, endpoints, capabilities, limits, examples, pricing, and lifecycle from official sources.
3. Update every dependent catalog, capability, pricing, request-URL, transport, and example reference in one change.
4. For paired regional skills, verify each region independently during the same update.

If the model has no documented predecessor in this repository, ask the user before adding it.
