# Contributing

Thanks for looking. This repo publishes skills that earn their place in a real daily workflow, so the bar is "does this hold up in production," not "does this demo well."

## Most valuable contributions

In rough order:

1. **New red-flag patterns** — a real pattern you've seen in the wild that [`docs/skill-intake/RED_FLAGS.md`](docs/skill-intake/RED_FLAGS.md) misses. Include what it looks like, why it's dangerous, and a severity.
2. **Real review write-ups** — you ran `skill-intake` against something and it caught (or missed) something interesting. Redact the candidate's name if it's an unfixed disclosure; see [`SECURITY.md`](SECURITY.md).
3. **Gaps in a threat model** — cases a skill is silently bad at. Being explicit about limits is a feature here, not an admission.
4. **New skills** — see the bar below.

## Repo layout

```
skills/<domain>/[<subdomain>/]<name>.md    the skill itself
docs/<name>/*.md                           deep docs for that skill — optional
templates/                                 files a skill expects to exist
```

Skills are **single markdown files, categorised by domain** — `skills/security/skill-intake.md`, `skills/product/ux-ui/behavioral-design.md`. `install.sh` maps each one to `~/.claude/skills/<name>/SKILL.md`, which is the layout Claude Code loads.

Skill names must be globally unique across the repo, since two skills with the same name would collide at that install path. CI enforces this.

## Front matter

```yaml
---
name: my-skill              # required, lowercase-kebab-case, must match the filename
description: …              # required — this is the trigger
version: 1.0.0              # required, semver
user-invocable: true        # optional — exposes it as /my-skill
argument-hint: "[what to pass]"   # optional
---
```

The `description` is what the model reads to decide *whether to reach for the skill at all*. Write it so it says **when** to use it, not just what it does. CI validates all of the above.

## Bar for a new skill

A skill in this repo must:

- **Solve a problem that isn't specific to one codebase.** If it hardcodes your project's structure, it belongs in your repo, not this one.
- **Have been used repeatedly, not written for the PR.** Say roughly how long you've run it and what it caught or saved.
- **Be readable end to end.** No bundled binaries, no minified scripts, no fetching code at runtime. This repo is about reviewability — a skill here has to survive its own gate.
- **Declare its permissions honestly.** If it needs `Bash`, say why in the skill body.
- **State its limits.** Every skill here ships with a "what this is not" section somewhere.

## Pull requests

- One logical change per PR.
- Explain the problem before the solution. A PR that opens with "here's a pattern I hit" is easier to evaluate than one that opens with a diff.
- If you're changing `skill-intake`'s phases, say what a review would have missed without your change.
- Run `python3 scripts/validate.py` locally before pushing.

## What gets declined

- Skills that duplicate an existing one here (the whole repo is about not stacking overlapping tools)
- Anything that weakens a gate for convenience — auto-approval, skipping the read, defaulting to install
- Prompt-tuning changes with no worked example showing the difference

## Code of conduct

See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
