# Shared Route Key Schema

A runtime route is identified by the exact composite key:

`RequestKind + API Model + API Surface + API Version + Endpoint Kind`

Canonical serialization:

`{RequestKind}::{Model}::{ApiSurface}::{ApiVersion}::{EndpointKind}`

## Rules

- Resolve the connection profile before the route key.
- Every capability row must match exactly one verified request-URL row by the full key.
- Never inherit a capability across versions, endpoint kinds, regions, or surfaces.
- `v1` and `v1beta` are different routes even when their current capability cells happen to match.
- A provider transport may narrow a route but may not silently rewrite any route-key component.
- Record the resolved route key in request diagnostics, response `Transport`, errors, and logs.
