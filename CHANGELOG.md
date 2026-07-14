# Changelog

## 2026-07-14

### Changed

- Upgraded the repository to v2 provider catalogs and shared schemas with exact model, request-kind, API-surface, API-version, region, and pricing keys.
- Added row-level freshness, provider lifecycle, local selection, moving-alias, retirement, and replacement metadata.
- Updated the curated defaults for OpenAI, Gemini, DeepSeek, Aliyun Bailian, and MiniMax.
- Replaced Aliyun Bailian China Mainland `qwen3.6-plus` with `qwen3.7-plus` and International `qwen3.6-max-preview` with `qwen3.7-max`.
- Updated the related Aliyun capabilities, endpoints, workspace URL templates, prices, transports, and migration status.
- Standardized new request kinds such as `text-chat`, `multimodal-chat`, `image-generation`, and `music-generation` while keeping legacy aliases at the normalization boundary.
- Separated caller-defined function tools from provider-hosted tools and made role/history requirements explicit.
- Simplified `README.md`, `QUICKSTART.md`, and `COMMANDS.md` around common human workflows.

### Added

- Added `LLM/_evidence/evidence.json` with claim-level official-source evidence.
- Added shared evidence-manifest and role-support schemas.
- Added role-support matrices for every provider and hosted-tool references where supported.
- Added `tools/validate_repo.py` for deterministic structural and cross-file validation.
- Added dated migration and validation notes for this repository-wide update.

### Compatibility

- Existing legacy catalog and profile views remain available during migration.
- Unknown, stale, conflicted, unsupported, or region-mismatched values continue to fail closed.
