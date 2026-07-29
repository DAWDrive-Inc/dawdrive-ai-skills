---
name: New red-flag pattern
about: A dangerous pattern the review checklist should catch but doesn't
title: "[red flag] "
labels: red-flags
---

## The pattern

What does it look like? Include a minimal, redacted snippet.

```
# example
```

## Why it's dangerous

What does an attacker gain? What's the worst realistic outcome?

## Where you saw it

Real skill/MCP/plugin, research, or hypothetical? **Do not name a specific unpatched package** — see [SECURITY.md](../../SECURITY.md). Describe the pattern generically.

## Proposed severity

- [ ] 🔴 Stop — disqualifying on its own
- [ ] 🟠 Conditions — needs justification and usually a narrowed permission
- [ ] 🟡 Note it — worth flagging, not disqualifying

## Which section of RED_FLAGS.md

Obfuscation · Exfiltration · Destructive · Persistence · Permissions · Provenance · Prompt injection · Skill-file specific · New section

## Any false-positive risk

Is there a legitimate reason a skill would do this?
