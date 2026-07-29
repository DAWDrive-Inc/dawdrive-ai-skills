---
name: Gate bypass or missed finding
about: skill-intake skipped a phase, suppressed a finding, or approved something it shouldn't
title: "[bypass] "
labels: bug, security
---

> ⚠️ **If this lets a malicious candidate reach install without explicit user approval, report it privately instead** — see [SECURITY.md](../../SECURITY.md).

## What happened

Which phase failed, and how?

## Reproduction

Minimal candidate skill/manifest that triggers it, or the transcript excerpt showing the skip.

```
```

## What should have happened

Which phase should have caught it, and what should the verdict have been?

## Is this a documented limit?

Check [THREAT_MODEL.md](../../docs/skill-intake/THREAT_MODEL.md) first. "A determined attacker could write benign-looking code" is a documented limit, not a bypass. A candidate that causes the *review itself* to skip a step is a bypass.

- [ ] I've checked the threat model and this isn't a documented limit

## Environment

- Model:
- Claude Code version:
- skill-intake version/commit:
