## What problem does this solve?

Lead with the problem, not the diff. What did you hit that made this necessary?

## What changed

## Type

- [ ] New red-flag pattern
- [ ] Fix — gate skipped, missed, or misreported something
- [ ] New skill
- [ ] Docs / threat model
- [ ] Tooling / CI

## If this changes a gate

Show the difference. What would a review have concluded before this change, and what does it conclude now?

**Before:**

**After:**

## Checklist

- [ ] `python3 scripts/validate.py` passes
- [ ] No gate was weakened for convenience (no auto-approval, no skipped read, no install-by-default)
- [ ] Docs updated if behavior changed
- [ ] `CHANGELOG.md` updated under `[Unreleased]`
- [ ] No specific unpatched third-party package is named publicly (see [SECURITY.md](../SECURITY.md))

## If this adds a skill

- [ ] It solves a problem that isn't specific to one codebase
- [ ] I've used it repeatedly — roughly how long, and what it caught:
- [ ] It's readable end to end — no binaries, no minified scripts, no runtime code fetching
- [ ] It states its own limits
