# Changelog

All notable changes to this project are documented in this file.

This project follows a milestone-based development approach rather than strict semantic versioning in early stages.

---

## v2.0.0 — Strategy Architecture Stabilization

### Added
- Strategy-based grouping architecture replacing conditional logic
- Explicit strategy registry to control ordering and extensibility
- Modular strategy extraction (`images`, `docs`, `audio`, `video`, `archive`, `fallback`)
- Fail-fast validation for strategy contracts
- Fallback detection and enforcement (exactly one, must be last)

### Changed
- Grouper refactored into a pure orchestrator
- Group definitions derived dynamically from registered strategies
- Project execution moved from script-style to package-style (`python -m`)

### Guarantees
- `accepts(file)` must return a boolean
- Every strategy must define a non-empty `group_name`
- Duplicate group names are rejected at startup
- Exactly one fallback strategy is required
- Fallback strategy is always evaluated last
- Misconfiguration fails before any file processing

### Notes
- Phase 2 completes the architectural foundation for V2
- No user-facing features were added in this release
- This release focuses on correctness, extensibility, and maintainability
