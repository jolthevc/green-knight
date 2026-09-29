# Source Log Standard

**Status:** Canonical portfolio-wide standard  
**Purpose:** Preserve traceability between meaningful claims and the evidence supporting them.

---

## 1. Role

The source log is Green Knight's internal evidence ledger for a video.

The viewer does not need to hear citations in every sentence.

Green Knight does need to know where consequential factual claims came from.

The source log should make fact-checking, revisions, disputes, and later reuse easier.

---

## 2. Source IDs

Assign stable source IDs.

Recommended pattern:

`S001`, `S002`, `S003`

A source ID refers to a source, not to an individual claim.

Where useful, claims may receive separate claim IDs.

---

## 3. Required Fields Per Source

Capture:

- source ID
- title
- publisher / institution / author
- source type
- publication date
- access date where relevant
- URL or file location
- relevant pages / sections / timestamps
- what this source supports
- reliability notes
- material caveats

---

## 4. Claim Mapping

For consequential claims, preserve a mapping between the claim and supporting source IDs.

Recommended fields:

- claim ID
- claim text or concise description
- supporting source IDs
- confidence
- caveat
- location in script or section

---

## 5. Source Classes

Useful classifications:

- primary
- official data
- academic
- legal
- company material
- reputable journalism
- trade publication
- expert commentary
- secondary reference
- user-generated / community
- archival
- other

Classification does not automatically determine reliability.

---

## 6. Confidence

Confidence should describe the evidence behind the claim, not the writer's enthusiasm.

Possible labels:

- HIGH
- MEDIUM
- LOW
- CONTESTED

If confidence is low or evidence is contested, the script should reflect that.

---

## 7. Dates and Scope

For statistics, always preserve:

- date or period
- geography
- population
- unit
- whether nominal or real where relevant
- whether estimate or observed value

A number without scope is often misleading.

---

## 8. Source Replacement

If a weak source is used for discovery and a stronger primary source is later found, update the source log rather than retaining the weak source as canonical support.

---

## 9. Rights vs Evidence

A source being valid evidence does not automatically mean its media can be reused visually.

Evidence sourcing and asset licensing are separate questions.

---

## 10. Failure Modes

Avoid:

- bare URL dumps
- sources without an explanation of what they support
- claims supported only by search snippets
- circular sourcing
- stale data presented without date context
- unsupported confidence
- treating company marketing as independent verification
- losing page or timestamp references for long sources

---

## 11. Completion Gate

The source log passes when a reviewer can trace every consequential factual assertion in the video to adequate evidence without recreating the research process from scratch.
