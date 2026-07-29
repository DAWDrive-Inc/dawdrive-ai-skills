# Red flags

The pattern checklist Phase 1 runs against. Not exhaustive — contributions welcome.

Severity key: 🔴 **stop** (⛔ unless there is an extraordinary, verified reason) · 🟠 **conditions** (⚠️, needs justification and usually a narrowed permission) · 🟡 **note it** (worth flagging in the verdict, not disqualifying on its own)

---

## Obfuscation and indirection

| Pattern | Severity | Why |
|---|---|---|
| `curl ... \| sh` / `wget ... \| bash` | 🔴 | Executes code you never read, and the remote content can change after review |
| `eval` on a constructed or fetched string | 🔴 | Defeats static reading entirely |
| Base64 / hex blobs decoded then executed | 🔴 | The only reason to encode a script is to make it unreadable |
| Minified or bundled JS with no readable source | 🟠 | Not inherently malicious, but unreviewable — ask for the source |
| Bundled binaries or compiled artifacts | 🟠 | Cannot be read; needs strong provenance to pass |
| Code downloaded at runtime from a URL | 🔴 | What you reviewed is not what will run |

## Data exfiltration

| Pattern | Severity | Why |
|---|---|---|
| Reads `~/.ssh`, `~/.aws`, `~/.config/gcloud`, keychains | 🔴 | No legitimate skill needs raw credential material |
| Reads `.env` files not scoped to its stated job | 🔴 | Classic secret harvest |
| POSTs to a hardcoded domain unrelated to its function | 🔴 | Follow the URL; if it isn't the tool's own service, stop |
| Undisclosed telemetry or analytics beacons | 🟠 | Must be disclosed and ideally opt-in |
| Reads shell history (`.bash_history`, `.zsh_history`) | 🔴 | History routinely contains pasted tokens |
| Writes collected data to a temp file, then uploads it | 🔴 | Staging is a strong exfil signal |

## Destructive operations

| Pattern | Severity | Why |
|---|---|---|
| `rm -rf` with a variable or unquoted path | 🔴 | One empty variable from wiping a home directory |
| `git push --force`, `git reset --hard` on shared branches | 🟠 | Destroys work that isn't the tool's to destroy |
| Writes outside its own directory without saying so | 🟠 | Scope creep with side effects |
| Modifies shell rc files, `PATH`, or system config | 🔴 | Persistence mechanism |
| Installs global packages or system-level daemons | 🟠 | Needs to be disclosed and justified |
| `chmod 777`, or loosening file permissions | 🟠 | Weakens the surrounding system |

## Persistence and privilege

| Pattern | Severity | Why |
|---|---|---|
| Installs git hooks without disclosing it | 🟠 | Runs on every commit, long after you forgot it exists |
| Creates cron jobs, launchd plists, systemd units | 🔴 | Runs when you aren't watching |
| Requests or invokes `sudo` | 🔴 | An agent extension should never need root |
| Registers itself to auto-run at agent startup | 🟠 | Must be disclosed |
| Modifies other installed skills or agent config | 🔴 | Tampering with the trust boundary itself |

## Permission smells

| Pattern | Severity | Why |
|---|---|---|
| No `allowed-tools` declared at all | 🟡 | Inherits everything — acceptable for simple skills, but note it |
| Requests `Bash` for a read-only task | 🟠 | Disproportionate; ask for it to be narrowed |
| Requests network tools with no stated network need | 🟠 | Same |
| Wildcard tool grants (`*`) | 🟠 | Fine for a trusted first-party tool, a smell from an unknown author |
| MCP server declaring scopes it never uses | 🟠 | Either dead code or future intent |

## Provenance signals

| Pattern | Severity | Why |
|---|---|---|
| Repo created days ago, no history, single squashed commit | 🟠 | Nothing to corroborate |
| Anonymous author, no other published work | 🟠 | Raises the bar on the code read |
| Name is one character off a popular tool | 🔴 | Typosquat |
| README claims an affiliation the org doesn't confirm | 🔴 | Impersonation |
| No license file | 🟡 | Sloppy, and legally ambiguous |
| Issues disabled, or issues full of unanswered reports | 🟡 | Unmaintained |

## Prompt-injection surface

An extension that ingests untrusted content and then *acts* on it is a delivery vector, whatever its own code does.

| Pattern | Severity | Why |
|---|---|---|
| Fetches web pages / issues / emails, then takes actions based on them | 🟠 | Instructions in fetched content must be treated as data |
| Instructs the agent to "follow any instructions found in" ingested content | 🔴 | Explicitly hands control to whoever writes the content |
| Auto-approves or auto-confirms downstream actions | 🔴 | Removes the human check exactly where it's needed |
| Reads file contents and executes strings found inside them | 🔴 | Same class of problem |

## Skill-file specific

| Pattern | Severity | Why |
|---|---|---|
| Description written to over-trigger ("use for everything") | 🟡 | Causes ambiguous invocation, crowds out other skills |
| Trigger description that collides with an installed skill | 🟠 | Phase 5 conflict — resolve before install |
| Instructions telling the agent to hide or not report actions | 🔴 | There is no benign version of this |
| Instructions to disable safety checks or ignore system prompts | 🔴 | Same |
| Malformed YAML frontmatter | 🟡 | Breaks loading; usually just carelessness |
