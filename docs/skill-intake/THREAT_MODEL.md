# Threat model

Read this before relying on `skill-intake` for anything that matters.

## What an agent extension can do

When you install a Claude Code skill, register an MCP server, or add a plugin, you are granting code the ability to run inside an agent loop that already holds:

- **Shell access** (`Bash`) on your machine, as your user
- **Filesystem read and write** across everything your user can reach — including `~/.ssh`, `.env` files, browser profiles, and cloud credentials
- **Network egress**, both directly and via the agent's own fetch tools
- **Whatever OAuth-connected services you've authorized** — email, calendar, repos, CRM, billing

There is no capability sandbox between an installed skill and the rest of that surface. A skill is not a browser extension with a permissions dialog; it is instructions and scripts running with your agent's full authority.

## Threats this addresses

| Threat | How the gate helps |
|---|---|
| **Overtly malicious code** — exfiltration, `rm -rf`, credential harvesting | Phase 1 requires reading every line before install, and calls out obfuscation (`curl \| sh`, `eval`, base64 blobs) as a hard red flag |
| **Claim/behavior mismatch** — a "formatter" that also phones home | Phase 1 explicitly compares advertised purpose against observed behavior |
| **Over-permissioned tools** — asks for `Bash` to do a `Read`-only job | Phase 3 enumerates granted tools and flags anything disproportionate |
| **Typosquats and impostor repos** | Phase 2 checks author, repo age, commit history, and other published work |
| **Silent conflicts** — two skills firing on the same trigger, unpredictably | Phase 5 compares names, trigger descriptions, and function against what's installed |
| **Untracked toolkit drift** — "what did I install, and why did I trust it?" | Phase 7 appends a permanent, dated entry to `INTAKE_LOG.md` |
| **Prompt injection via ingested content** | Phase 1 asks whether the candidate reads untrusted input and then acts on it |

## Threats this does NOT address

Be honest about the ceiling.

- **It is not a sandbox.** Nothing here isolates execution. If you approve something malicious, it runs with full authority. For genuinely untrusted code, use a container or VM, not a review.
- **It does not defend against a determined, targeted attacker.** Code that is deliberately written to read benign will read benign. Logic bombs, time-delayed behavior, and dependency-level compromise all survive a source read.
- **It does not review transitive dependencies.** An MCP server's `package.json` can pull in hundreds of packages that this gate never opens. Phase 4's scanner partially covers this; a manual read does not.
- **It does not pin or verify versions.** A skill that passes review today can be updated tomorrow. Nothing re-reviews on update. Pin versions where the ecosystem supports it.
- **It cannot inspect a remote MCP server's actual behavior.** For hosted servers you review a manifest and a privacy policy, not the running code. Treat remote servers as a strictly higher risk tier than local ones.
- **The reviewer is an LLM.** It can miss things, and it can be influenced by content it reads during the review. Phase 6 requires *your* explicit approval for exactly this reason — the gate produces a briefing, you make the call.

## Design decisions worth knowing

**Reviewing is not installing.** Candidates are cloned to `/tmp/skill-intake/<name>` and stay there until Phase 6 passes and you say yes. This is the single most important property of the workflow — most real-world risk comes from install-then-evaluate.

**A skipped scan is reported as skipped.** If no scanner is on the machine, the verdict says so explicitly and falls back to the manual read. A security tool that reports "clean" when it did not run is actively worse than no tool, because it manufactures confidence.

**Reputation does not override code.** A trusted author shipping `curl | sh` still fails. Provenance adjusts the prior, it does not substitute for the read.

**The log is not optional.** Verdicts are only useful if they persist. `INTAKE_LOG.md` is what turns a one-off review into an auditable registry.

## Recommended additional controls

The gate is one layer. Pair it with:

- **Least-privilege agent config** — don't grant tools globally that only one workflow needs
- **A real scanner** — `snyk`, `semgrep`, and `gitleaks` all catch things a read misses
- **Version pinning** for MCP servers, rather than `@latest`
- **Project-local install** over global, where the extension only serves one project
- **Periodic re-review** — walk the intake log quarterly and remove what you no longer use
