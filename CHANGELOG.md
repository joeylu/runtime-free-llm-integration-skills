# Changelog

All notable changes to this repository are documented in this file.

The format follows the principles of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Release headings use calendar dates until the repository adopts a formal version-tagging scheme.

## [Unreleased]

No unreleased changes.

## [2026-07-15]

### Changed

- Reframed the repository as a logic-only, normative documentation layer for agent reasoning about direct LLM API integrations.
- Clarified that provider contracts, route resolution, field mappings, fail-fast conditions, and API-side validation semantics remain in scope.
- Clarified that implementation, testing, installation, deployment, CI, and project acceptance belong to the host project or host agent environment.
- Updated wording that could be mistaken for repository-local development validation, replacing it with contract-oriented terms such as route resolution, contract gating, constraints, and explicit mappings.
- Updated host discovery and distribution guidance so that skill registration, copying, linking, plugin packaging, and workspace policy are delegated to the host environment.
- Updated audit guidance so that repository review produces documentation findings rather than implementation certification.
- Retained provider-side error types such as `validation_error`, JSON Schema constraints, strict tool schemas, request-time fail-fast rules, and other API contract semantics.
- Retained all provider and regional skill boundaries, model catalogs, capability matrices, pricing records, request URLs, transport rules, and Route Key V2 definitions.
- Retained the `implement` workflow as normative guidance for a host agent; the repository itself does not execute implementation work.

### Removed

- Removed all repository-local executable validators and structural checking utilities.
- Removed the official-source URL reachability checker.
- Removed the Codex skill installation utility.
- Removed the entire `tools/` directory and all references to running repository-local validation or installation commands.
- Removed any implied responsibility for linters, test harnesses, regression fixtures, CI jobs, scaffolding, code generation, deployment, or project acceptance.

## [2026-07-14]

### Breaking changes

- Expanded capability lookup from `RequestKind + API Model + API Surface` to the full route key:
  `RequestKind + API Model + API Surface + API Version + Endpoint Kind`.
- Added the canonical route-key representation:
  `{RequestKind}::{Model}::{ApiSurface}::{ApiVersion}::{EndpointKind}`.
- Added API version and endpoint kind to capability and request-route resolution, requiring consumers to migrate any lookup, cache, logging, fixture, or error key based on the previous three-part key.
- Expanded model-catalog and pricing schemas with explicit operation, modality, lifecycle, region, alias, billing-plan, tier, discount, validity, cache, and multiplier fields.
- Made all provider skills explicit-only and established `skill-llm-router` as the sole logical entry point eligible for implicit routing.

### Added

- Added row-level `Last Verified At` and official `Source` fields for capability records.
- Added distinct Gemini Interactions routes for stable `v1` and compatibility `v1beta` surfaces.
- Added a dedicated router skill for exact provider, region, model, API surface, API version, and endpoint-kind resolution without model recommendation or silent substitution.
- Added explicit MiniMax supported-surface and out-of-scope manifests.
- Added migration guidance for Route Key V2.

### Changed

- Reframed every provider skill as a runtime integration contract rather than a model-selection, approval, or governance system.
- Kept model selection with the user or host project and removed default-model, selected-model, candidate, and approval semantics from runtime instructions.
- Removed model identifiers from connection profiles so that profiles describe endpoints and credential references only.
- Structured model entries around request operation, input and output modalities, flow kind, identifier kind, alias resolution, lifecycle, and regional scope.
- Structured pricing records around list price, effective price, billing plan, service tier, discount type, validity period, cache class, and multiplier.
- Narrowed Aliyun Bailian International scope to the maintained and verified `qwen3.7-max` chat route.
- Removed unsupported music claims from the Aliyun Bailian China Mainland skill.
- Updated model records across catalogs, capabilities, pricing references, request URLs, transports, and examples:
  - added `qwen3.7-max` for Aliyun Bailian China Mainland;
  - replaced `glm-5.1` with `glm-5.2`;
  - replaced `kimi-k2.6` with `kimi-k2.7-code`;
  - replaced MiniMax M2.7 runtime rows with `MiniMax-M3` for China Mainland and International regions.
- Clarified that MiniMax M3 vision uses the same OpenAI-compatible Chat Completions endpoint as chat.
- Kept regional provider data independent so that availability, endpoints, pricing, and behavior are not copied across regions without regional official evidence.

### Fixed

- Normalized shared response kinds to `chat`, `vision`, `imaging`, and `music`, removing transport-specific values such as `text-chat`, `image-generation`, and `music-generation` from `ResultKind` usage.
- Defined deterministic DeepSeek reasoning mappings:
  - `none` sends `thinking.type=disabled` and omits `reasoning_effort`;
  - `low`, `medium`, and `high` map to wire value `high`;
  - `xhigh` and `max` map to wire value `max`.
- Explicitly prohibited sending `reasoning_effort="none"` to DeepSeek.
- Preserved MiniMax `adaptive` as a distinct thinking state rather than collapsing it into a shared boolean.
- Scoped the MiniMax M3 Chat Completions adaptive default to that exact route and prevented it from being inherited by Responses or Anthropic-compatible surfaces.
- Split Gemini Interactions `v1` and `v1beta` capability records to prevent cross-version inheritance.
- Corrected Aliyun Bailian China Mainland `qwen3.7-max` pricing to retain both list and effective promotional prices:
  - input: CNY 12 list / CNY 6 effective per million tokens;
  - output: CNY 36 list / CNY 18 effective per million tokens.
- Kept the promotional end date as `unknown` because no official end date was published.
- Fixed numbering, grammar, and isolated Markdown formatting artifacts across the documentation.
