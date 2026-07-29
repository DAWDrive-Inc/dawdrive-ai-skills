# Changelog

All notable changes to this repo are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Individual skills carry their own `version` in front matter; this file tracks the repo.

## [Unreleased]

### Added

- **`skills/security/skill-intake.md`** (v1.0.0) — a 7-phase security gate for vetting Claude Code skills, MCP servers, and plugins before installation. Candidates stay in `/tmp` until explicitly approved; every verdict is appended to a permanent intake log.
- **`docs/skill-intake/THREAT_MODEL.md`** — what the gate defends against, and the limits it explicitly does not cover (not a sandbox, no transitive dependency review, no re-review on update).
- **`docs/skill-intake/RED_FLAGS.md`** — severity-tagged checklist covering obfuscation, exfiltration, destructive operations, persistence, permission smells, provenance signals, and prompt-injection surface.
- **`docs/skill-intake/EXAMPLE_REVIEW.md`** — two worked reviews, one ⚠️ and one ⛔.
- **`install.sh`** — confirmation-gated installer. Maps `skills/<domain>/<name>.md` to the `~/.claude/skills/<name>/SKILL.md` layout Claude Code loads. No network calls, no silent overwrites.
- **`scripts/validate.py`** + CI — validates skill front matter, catches duplicate skill names, and checks every internal markdown link.
- **`templates/INTAKE_LOG.md`** — seed file for the intake registry.
- `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue and PR templates.

### Changed

- **`README.md`** — expanded from a project description into a skills index with per-skill entries, install instructions, and a featured write-up.

### Notes

`skill-intake` derives from a skill in daily private use since June 2026. Genericized for publication: removed personal references, broadened the scan phase beyond a single vendor, and added an explicit prompt-injection check to Phase 1.

## Earlier

- `skills/product/ux-ui/github-101.md` (v1.1.0) — GitHub coach for founders and creators building with AI coding assistants.
- `skills/product/ux-ui/behavioral-design.md` (v1.0.0) — human-behavior UX audit across understand / trust / act / recover / sustain.

[Unreleased]: https://github.com/DAWDrive-Inc/dawdrive-ai-skills/commits/main
