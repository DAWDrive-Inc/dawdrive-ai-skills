---
name: behavioral-design
description: Audit a screen, workflow, feature, or product through the lens of human behavior, cognition, trust, accessibility, and task completion. Produces evidence-backed findings, behavioral risk analysis, and prioritized recommendations.
version: 1.0.0
user-invocable: true
---

# HUMAN UX Audit

Evaluate software through five dimensions:

UNDERSTAND
TRUST
ACT
RECOVER
SUSTAIN

The goal is not to judge aesthetics.

The goal is to identify where human behavior and system behavior diverge.

---

# Step 1 — Identify the User Goal

Determine:

Primary Goal:
...

Secondary Goals:
...

Success Criteria:
...

If the primary goal is unclear, note this immediately.

---

# Step 2 — Model User Expectations

Predict:

What does a first-time user expect will happen?

What does a returning user expect will happen?

What actually happens?

Output:

Expected:
...

Actual:
...

Mismatch:
...

---

# Severity Scale

PASS

INFO

WARN

FAIL

CRITICAL

Definitions:

PASS = No meaningful issue found

INFO = Observation only

WARN = Noticeable friction

FAIL = Likely to impact success

CRITICAL = High risk of abandonment, mistakes, or loss of trust

---

# Finding Format

[WARN] UNDERSTAND.3

Evidence:
...

Impact:
...

Recommendation:
...

---

# UNDERSTAND

Can users understand the interface?

UNDERSTAND.1 Purpose clarity

Can users identify what this screen is for?

UNDERSTAND.2 Next-step clarity

Can users identify what to do next?

UNDERSTAND.3 Language clarity

Is language written in user terms?

UNDERSTAND.4 Concept load

How many new concepts are introduced?

UNDERSTAND.5 Information hierarchy

Does visual structure guide attention effectively?

UNDERSTAND.6 Recognition over memory

Must users remember information from previous steps?

---

# TRUST

Can users confidently predict outcomes?

TRUST.1 Outcome visibility

Can users predict what happens next?

TRUST.2 System status visibility

Can users understand current state?

TRUST.3 Transparency

Are consequences explained?

TRUST.4 Permission clarity

Who can do what?

TRUST.5 Reversibility

Can mistakes be undone?

TRUST.6 Risk communication

Is impact communicated before actions occur?

TRUST.7 Ethical design

No manipulative patterns.

---

# ACT

Can users successfully complete their goal?

ACT.1 Happy-path success

ACT.2 Friction count

ACT.3 Decision count

ACT.4 Interaction efficiency

ACT.5 Dead ends

ACT.6 Progress visibility

ACT.7 Time-to-completion

Estimate:

Under 30 seconds

30 seconds–2 minutes

2–5 minutes

5+ minutes

---

# RECOVER

What happens when things go wrong?

RECOVER.1 Error prevention

RECOVER.2 Error clarity

RECOVER.3 Error recovery

RECOVER.4 Undo capability

RECOVER.5 Safe experimentation

Can users explore without fear?

RECOVER.6 State restoration

Can users return to a known-good state?

---

# SUSTAIN

What encourages continued usage?

SUSTAIN.1 Cognitive load

SUSTAIN.2 Learnability

SUSTAIN.3 Workflow integration

SUSTAIN.4 Motivation support

Does the interface help users feel capable?

SUSTAIN.5 Consistency

Are patterns reused?

SUSTAIN.6 Accessibility

Can a broad range of users succeed?

---

# Behavioral Signals

Estimate:

Confusion Risk

Trust Risk

Error Risk

Abandonment Risk

Learning Curve

For each:

Low
Medium
High

---

# Anti-Patterns

Identify:

- Choice overload
- Empty states
- Hidden system status
- Ambiguous actions
- Feature-first design
- Navigation traps
- Excessive setup
- Notification fatigue
- Modal chains
- Permission anxiety

---

# Priority Recommendations

Rank recommendations by expected user impact.

1.
2.
3.

---

# Final Assessment

Excellent

Strong

Needs Improvement

High Risk

Provide a concise explanation focused on user outcomes and behavior.