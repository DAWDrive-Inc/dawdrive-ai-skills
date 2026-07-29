# dawdrive-ai-skills

DAWDrive, Inc. is a music production software development team that utilizes AI to assist with product builds and dev workflows. We are founded by a team of two music producers, so we know how hard it can be to get your ideas down and execute on them. These skills are applicable to any app, not just music. Product ideation can be for more than software.

Everything here runs daily against a real production codebase — a monorepo with a React frontend, an Express API, an Electron desktop app, and native file-provider extensions on Windows and macOS. These aren't demos.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Validation](https://github.com/DAWDrive-Inc/dawdrive-ai-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/DAWDrive-Inc/dawdrive-ai-skills/actions/workflows/validate.yml)

---

## Skills

### 🔒 Security

**[`skill-intake`](skills/security/skill-intake.md)** — a security gate for AI agent extensions

Vets any Claude Code skill, MCP server, or plugin **before** it touches your machine. Seven phases: read the code, check provenance, review permissions, scan, conflict-check, verdict, log. Nothing installs without your explicit approval.

→ [Threat model](docs/skill-intake/THREAT_MODEL.md) · [Red flags checklist](docs/skill-intake/RED_FLAGS.md) · [Example review](docs/skill-intake/EXAMPLE_REVIEW.md)

### 🎨 Product — UX/UI

**[`behavioral-design`](skills/product/ux-ui/behavioral-design.md)** — audit a screen, workflow, or product through the lens of human behavior, cognition, trust, and accessibility. Evaluates across five dimensions — understand, trust, act, recover, sustain — and produces evidence-backed findings rather than aesthetic opinions.

**[`github-101`](skills/product/ux-ui/github-101.md)** — a GitHub coach for founders and creators building with AI coding assistants. Teaches concepts before commands: where your code lives, how changes move, how to protect IP, and how AI agents interact with repositories.

---

## Install

Clone, read, then copy in:

```bash
git clone https://github.com/DAWDrive-Inc/dawdrive-ai-skills.git /tmp/dawdrive-ai-skills
```

**Read the skill you're installing first.** Every skill here is plain markdown — no bundled binaries, no minified scripts, no code fetched at runtime. That's a deliberate constraint, and it's what makes reading it feasible. Then:

```bash
cd /tmp/dawdrive-ai-skills && ./install.sh
```

`install.sh` lists what it's about to do, asks before every write, makes no network calls, and never overwrites an existing skill without confirmation.

To install one by hand — Claude Code expects each skill in its own directory as `SKILL.md`:

```bash
mkdir -p ~/.claude/skills/skill-intake
cp /tmp/dawdrive-ai-skills/skills/security/skill-intake.md ~/.claude/skills/skill-intake/SKILL.md
```

Restart your Claude Code session to pick them up.

---

## Featured: skill-intake

**Vet any Claude Code skill, MCP server, or plugin before it touches your machine.**

### The problem

Agent extensions are having their npm moment.

A Claude Code skill is a markdown file. An MCP server is a process your agent talks to. Both are trivially easy to publish, trivially easy to install, and — this is the part people skip — **both run with whatever tools your agent has been granted.** Bash. Filesystem writes. Network. Your credentials, if they're in scope.

Installing one is a supply-chain decision. Almost nobody treats it like one.

The typical install flow today is: see a link → paste the command → done. No read, no provenance check, no permission review, no record of what you added or why.

### What it does

`skill-intake` is a skill that reviews other skills. You point it at a candidate and it walks a fixed 7-phase gate before anything gets installed:

| Phase | Gate |
|---|---|
| **0** | Identify the candidate — clone to `/tmp`, never to your skills directory |
| **1** | Read every line — what it *actually* does vs. what it claims, network calls, filesystem reach, obfuscation |
| **2** | Check provenance — author, repo age, commit history, other published work |
| **3** | Review permissions — every tool it can invoke, and whether it needs them |
| **4** | Automated scan — Snyk / Semgrep if present, and an honest "skipped" if not |
| **5** | Conflict check — name collisions, overlapping triggers, functional duplicates |
| **6** | Verdict — ✅ / ⚠️ / ⛔, with reasoning. Waits for your explicit yes |
| **7** | Install + log — appends to a permanent intake log |

The core design constraint: **reviewing is not installing.** The candidate stays in `/tmp` until you say the word.

### Why it produces better reviews than just asking

Three properties do the work:

1. **The skill is the driver, not a suggestion.** Phases run in order. The model can't shortcut to "looks fine to me" because the verdict template requires filled-in findings from every prior phase.
2. **It refuses to fake a scan.** If no scanner is installed, the verdict says `skipped — no scanner installed` and falls back to the manual read. A security tool that quietly reports clean when it didn't run is worse than no tool, because it manufactures confidence.
3. **It writes down the decision.** Every verdict appends to `INTAKE_LOG.md` — source, permissions, scan result, reasoning. Six months later you can answer "why do I trust this thing?" without re-deriving it.

### Use

```
/skill-intake
```

Or just describe the intent:

> "I found this MCP server for Notion — is it safe to add?"

The skill triggers on install/evaluate intent and takes over from there.

### Example verdict

A full review, end to end, is in [`docs/skill-intake/EXAMPLE_REVIEW.md`](docs/skill-intake/EXAMPLE_REVIEW.md). Abbreviated:

> **Candidate:** `@playwright/mcp` — github.com/microsoft/playwright-mcp
> **What it does:** Exposes browser automation to the agent over stdio
> **Permissions:** Browser control; no shell, no arbitrary FS write, no network listeners
> **Source trust:** Reputable — Microsoft, active repo, thin wrapper over `playwright-core`
> **Scan:** 1 LOW finding (noise), 0 MEDIUM/HIGH/CRITICAL
> **Conflicts:** None
>
> **Verdict:** ⚠️ Install with conditions
> **Reasoning:** Behavior matches the claim exactly, provenance is first-party, permissions are proportionate, and the scan is clean. The one substantive finding is inherent rather than a defect: the server returns untrusted page content to the agent, which makes any browsing session a prompt-injection surface. That's a usage constraint, not a reason to reject.
>
> **Conditions:** install project-local rather than globally · pin the version instead of tracking `@latest` · treat page content as data, never instructions.

### What it is not

Read [`docs/skill-intake/THREAT_MODEL.md`](docs/skill-intake/THREAT_MODEL.md) before relying on this. In short: it's a **structured human-in-the-loop review**, not a sandbox and not a guarantee. It raises the floor from "paste and pray" to "read, reason, record." It does not stop a determined targeted attacker, it does not review transitive dependencies, and it does not replace running genuinely untrusted code in isolation.

---

## Contributing

New red-flag patterns and real-world review write-ups are the most valuable contributions. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](LICENSE). Copyright © 2026 DAWDrive, Inc.
