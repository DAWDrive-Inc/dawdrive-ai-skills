# Security policy

## Reporting a vulnerability in this repo

If you find a problem with a skill published here — a way to make it skip a gate, approve something it shouldn't, or take an action the user didn't authorize — please report it privately first.

**Use GitHub's [private vulnerability reporting](https://github.com/DAWDrive-Inc/dawdrive-ai-skills/security/advisories/new)** on this repo, or email the address on the DAWDrive-Inc GitHub profile.

Please include:

- Which skill, and which version/commit
- What the skill does that it shouldn't, or fails to do that it should
- A minimal reproduction — ideally a candidate skill or manifest that slips through
- What an attacker gains

Expect an acknowledgement within a few days. Fixes for anything that lets a malicious candidate reach install without an explicit approval will be treated as urgent.

## Reporting a malicious third-party skill or MCP server

**This is not the place for that.** If `skill-intake` helped you find something malicious in someone else's package:

1. Report it to the **publisher or registry** first (npm, the GitHub repo, the marketplace it's listed on)
2. Give them reasonable time to respond before publishing details
3. If you'd like to contribute the *pattern* here — the technique, not the named unfixed vulnerability — open a PR against [`docs/skill-intake/RED_FLAGS.md`](docs/skill-intake/RED_FLAGS.md) describing the pattern generically

Please don't open public issues naming a specific unpatched package. Once it's fixed or publicly disclosed elsewhere, a write-up is welcome.

## Scope and limits

`skill-intake` is a structured human-in-the-loop review process, not a sandbox. It has known, deliberate limits — they're documented in [`docs/skill-intake/THREAT_MODEL.md`](docs/skill-intake/THREAT_MODEL.md).

Reports along the lines of "a determined attacker could write code that reads benign" describe a documented limit rather than a vulnerability. Reports that the gate can be *bypassed* — for example, a candidate whose contents cause the review to skip a phase, suppress a finding, or auto-approve itself — are genuine vulnerabilities in this repo and very much wanted.

## No warranty

These skills are provided as-is under the MIT license. You are responsible for what you install on your own machine. That's the point of the gate, not a disclaimer around it.
