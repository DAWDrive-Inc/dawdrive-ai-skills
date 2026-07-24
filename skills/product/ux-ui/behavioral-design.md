Name: ux-check
Description: Run a structured UX audit of a screen or component against three lenses — FTU (first-time user), TRUST (high-stakes safety), and COG (cognitive load). Use when reviewing new screens before shipping, auditing existing UI for quality, or stress-testing a design against real user mental models. Works from a screenshot, a description, a JSX/HTML file, or a live route.
Version: 1.0.0
User invocable: true
Argument hint: [screen name or file path or description]

UX Check Skill
Run the full audit unless the user scopes it to one lens (e.g. "FTU only", "just TRUST").

Input
Accept any of:

A file path to a component or page (.jsx, .tsx, .html)
A route name or screen description
A screenshot (visual inspection)
Raw descriptive text of the UI
If a file path is given, read the file before auditing. If a screenshot is available, inspect it visually.

Output format
For each check, output one line:

[PASS] FTU.1 — Next action obvious
[WARN] FTU.5 — Jargon budget: 4 product-specific terms found ("Vault", "Version Graph", "BOM", "Release Lock")
[FAIL] COG.2 — Primary action count: 3 competing CTAs visible
Then a Summary block at the end:

PASS: N   WARN: N   FAIL: N
Top priority fixes:
1. [most severe FAIL or WARN + one-sentence fix]
2. ...
Use judgment — a WARN is "technically within limits but worth watching", a FAIL is "clear violation of the check".

The Checks
FTU — First-Time User
Five checks for what a brand-new user can do on the screen.

FTU.1 Next action obvious Within five seconds, can a first-time user identify what to do next? Look for a single dominant call-to-action, visual hierarchy that draws the eye, and absence of competing focal points.

FTU.2 No required prerequisite knowledge Does the screen require understanding a concept that hasn't been introduced yet? Flag any term or interaction that presupposes familiarity with the product's internal model.

FTU.3 Recoverable mistakes Is the cost of being wrong clear before they commit? Check for destructive actions with no confirmation, ambiguous buttons, and irreversible flows with no undo or preview.

FTU.4 Empty states do work Empty states should teach, not just announce emptiness. Check that zero-state UI explains what belongs here, why it's empty, and what to do next. "No items" alone is a failure.

FTU.5 Jargon budget Count product-specific terms. More than two for a first-time user is usually a warning sign. List the terms found and their count.

TRUST — High-Stakes Moments
Trust and safety at high-stakes moments.

TRUST.1 Preview before commit Can users see what will happen before it happens? Check for confirmation dialogs, preview modes, or summary screens before destructive or irreversible actions.

TRUST.2 Test mode Can they experiment without affecting real customers or data? Look for sandbox modes, draft states, or staging environments surfaced in the UI.

TRUST.3 State clarity Is it obvious whether something is draft, live, paused, or scheduled? Check that status labels are unambiguous and visually distinct.

TRUST.4 Reversibility How difficult is it to undo? Note if undo is absent, buried, or only available within a short window.

TRUST.5 Audit trail Can users see what happened, who did it, and when? Check for activity logs, timestamps, and actor attribution on meaningful actions.

TRUST.6 Volume signposting Before high-impact actions, is the scale obvious? Examples: "This will send to 42,000 contacts." "This will delete 7 projects." Flag if missing.

TRUST.7 No dark patterns No forced choice. No hidden cancellation. No guilt copy ("No thanks, I don't want to improve my workflow"). No fake scarcity. Flag any instance found.

COG — Cognitive Load
Simple counts that act as warning flags.

COG.1 Decision count More than three decisions before progress is usually a problem. Count distinct choices the user must make to complete the primary flow.

COG.2 Primary action count There should be one obvious next step. Count competing CTAs or buttons of equal visual weight.

COG.3 New concept count More than one new concept per screen is often too much. Count concepts that require explanation or that a first-time user would need to look up.

COG.4 Reading load More than 50 words of body copy is usually worth reviewing. Count visible body text (exclude labels, field names, and navigation). Flag if over threshold.

Calibration notes
Apply all checks from the perspective of the user's first encounter with this screen.
If the screen is deep in a flow (e.g. step 3 of onboarding), note that context — FTU checks apply to the screen in isolation AND relative to what's been introduced so far.
TRUST checks apply most heavily to: delete flows, publish/send flows, payment flows, and any action that affects other people.
COG checks are counts, not judgments. Report the number. Let the team decide if the count is acceptable for their context.
A screen can PASS all checks and still be mediocre design. This audit catches failure modes, not greatness.
