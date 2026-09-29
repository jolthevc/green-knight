# Fact Check Standard

**Status:** Canonical portfolio-wide standard  
**Purpose:** Catch unsupported or mis-scoped factual claims before Green Knight spends money on narration and editing.

---

## 1. Principle

Fact checking should happen before production, not primarily after a finished edit exists.

Green Knight uses two lightweight fact gates:

1. a research fact gate during `RESEARCH_REVIEW`
2. a script fact gate during `SCRIPT_REVIEW`

These are checks inside existing stages, not additional lifecycle stages.

---

## 2. Research Fact Gate

Before research receives `PROCEED`, verify that consequential evidence is traceable.

At minimum:

- important numbers have source, date/period, unit, and scope
- consequential factual assertions map to a source ID
- causal claims are supported as causal rather than merely correlated
- major contradictory evidence is represented
- the source log explains what each important source supports
- weak discovery sources are replaced by stronger evidence where practical

Where technically practical, confirm that cited URLs or files resolve and that the cited material actually contains the relevant evidence.

Do not automatically fail merely because a legitimate source is paywalled, archived, local, or otherwise difficult for a machine to fetch.

Unverifiable consequential claims should be flagged rather than silently passed.

---

## 3. Script Fact Gate

Before a script receives `APPROVE`, check the final narration against the source log.

At minimum:

- consequential numbers map to source-log claims
- named factual assertions map to evidence
- dates and chronology are consistent
- estimates are presented as estimates
- allegations and contested interpretations are described appropriately
- script wording has not become stronger than the underlying evidence
- important qualifications have not been lost during simplification

The goal is not to cite every sentence.

The goal is to prevent unsupported consequential claims from reaching narration and editing.

---

## 4. Automation

Use deterministic or low-cost checks where they are reliable.

Examples:

- extract numbers and proper nouns from a script
- compare them with source-log claims
- detect missing claim mappings
- verify URL availability
- flag mismatched dates or units

Use a capable reasoning model when the question requires interpretation.

Do not build a complex fact-checking agent network in v1.

---

## 5. Outcome

The fact gate produces one of:

- PASS
- BLOCK

A BLOCK should identify the exact unresolved claim or evidence issue and route through the existing review outcome:

- `RESEARCH_MORE`
- `REVISE`
- `REFRAME`
- `KILL`

No new lifecycle state is required.

---

## 6. Final QA

Final QA still checks factual presentation, including:

- on-screen numbers
- maps
- charts
- captions
- screenshots
- visual implication

But final QA should not be the first time the underlying narration is seriously fact-checked.
