# Canonical Video Lifecycle

**Status:** Canonical portfolio-wide standard  
**Purpose:** Define how every Green Knight video moves from an initial idea to a published and evaluated media asset.

---

## 1. Why This Exists

Green Knight should not automate an ambiguous creative process.

Before n8n workflows are built, the company must define:

- what state a video can be in
- what artifact is required at each stage
- what each artifact must accomplish
- what information moves forward
- what can block progression
- what can cause a reframe, revision, or kill
- what gets stored in Sheets, Drive, and GitHub
- what humans versus AI are expected to do

This lifecycle is the shared production architecture used across all channels.

The creative content of channels can differ radically.

The lifecycle should remain substantially consistent.

---

## 2. Core Principle

A video is not merely a file that gets written and edited.

It is a chain of hypotheses, evidence, creative decisions, and production artifacts.

Each major stage should reduce uncertainty before Green Knight commits more time or money.

The system should preserve enough context to answer later:

> Why did we choose this idea?

> What did we believe would make it work?

> What evidence supported the script?

> What promise did the packaging make?

> What did the audience actually do?

> What did we learn?

---

## 3. Canonical States

The machine-readable source of truth for legal states and transitions is `schemas/lifecycle.yaml`.

This document explains the lifecycle in human terms. If a transition described here ever conflicts with the YAML, fix the inconsistency rather than letting two lifecycle definitions persist.

Every video should occupy one primary lifecycle state.

### IDEA
A low-cost candidate exists in the channel's video-ideas pool.

No meaningful production commitment has been made.

### SELECTED
The idea has been chosen for development.

A permanent `video_id` is assigned and the canonical Drive folder is created.

### BRIEFED
The video thesis, viewer question, framing, strategic rationale, and research requirements are defined.

Required artifact: `VIDEO_BRIEF`.

### RESEARCHING
Research is actively being gathered.

### RESEARCHED
The research packet and source inventory are sufficiently complete for editorial development.

Required artifacts:

- `RESEARCH_PACKET`
- `SOURCE_LOG`

### RESEARCH_REVIEW
The evidence is audited against the proposed thesis.

Permitted outcomes:

- PROCEED
- RESEARCH_MORE
- REFRAME
- KILL

### OUTLINING
The research is being converted into narrative structure.

### OUTLINED
A detailed story architecture exists.

Required artifact: `OUTLINE`.

### OUTLINE_REVIEW
The outline is tested for narrative strength, completeness, pacing, evidence, and channel fit.

Permitted outcomes:

- APPROVE
- REVISE
- RESEARCH_MORE
- REFRAME
- KILL

### SCRIPTING
The approved outline is being converted into final narration.

### SCRIPTED
A recordable script exists.

Required artifact: `SCRIPT`.

### SCRIPT_REVIEW
The script is audited for story quality, voice, clarity, factual support, pacing, and fulfillment of the video thesis.

Permitted outcomes:

- APPROVE
- REVISE
- RETURN_TO_OUTLINE
- RESEARCH_MORE
- KILL

### PACKAGING
Titles, thumbnails, and opening-promise alignment are being developed.

Permitted outcomes:

- SELECT
- RETURN_TO_SCRIPT
- KILL

If the strongest truthful package requires a materially different opening or script promise, return to scripting rather than stretching the package beyond the video.

### PACKAGED
An approved packaging direction exists.

Required artifact: `PACKAGING_PACKET`.

### PRODUCTION_READY
All inputs required by human production are complete.

Required artifact: `PRODUCTION_PACKET`.

The video should not enter production merely because a script exists.

### IN_PRODUCTION
A human or production system is assembling the finished visual product.

### FIRST_CUT
A complete first cut exists.

### REVISION
Production feedback is being incorporated.

### QA
The final candidate is being checked for editorial, factual, visual, audio, rights, brand, packaging, and technical quality.

### READY_TO_PUBLISH
QA has passed and all publishing inputs are complete.

### PUBLISHED
The video is live on YouTube.

Canonical files move from the channel's unpublished structure to its published structure according to the Drive standard.

### MEASURING
Performance windows are being populated.

### EVALUATED
A postmortem exists and the durable learnings have been written back to the appropriate systems.

Required artifact: `POSTMORTEM`.

### KILLED
Active work has stopped before publication.

A killed video should retain its history and reason for termination.

---

## 4. Canonical Flow

```
IDEA
  ↓
SELECTED
  ↓
BRIEFED
  ↓
RESEARCHING
  ↓
RESEARCHED
  ↓
RESEARCH_REVIEW
  ├── RESEARCH_MORE ─────┐
  ├── REFRAME ───────────┤
  ├── KILL               │
  └── PROCEED            │
                         ↓
                    OUTLINING
                         ↓
                    OUTLINED
                         ↓
                  OUTLINE_REVIEW
                   ├── REVISE
                   ├── RESEARCH_MORE
                   ├── REFRAME
                   ├── KILL
                   └── APPROVE
                         ↓
                    SCRIPTING
                         ↓
                    SCRIPTED
                         ↓
                   SCRIPT_REVIEW
              ├── REVISE
              ├── RETURN_TO_OUTLINE
              ├── RESEARCH_MORE
              ├── KILL
              └── APPROVE
                         ↓
                    PACKAGING
              ├── RETURN_TO_SCRIPT
              ├── KILL
              └── SELECT
                         ↓
                     PACKAGED
                         ↓
                 PRODUCTION_READY
                         ↓
                  IN_PRODUCTION
                         ↓
                    FIRST_CUT
                         ↓
                     REVISION
                         ↓
                        QA
                   ├── FAIL → REVISION
                   └── PASS
                         ↓
                 READY_TO_PUBLISH
                         ↓
                    PUBLISHED
                         ↓
                    MEASURING
                         ↓
                    EVALUATED
```

Backward routes are explicit in `schemas/lifecycle.yaml`. In particular:

- research `REFRAME` returns to `BRIEFED`
- outline `RESEARCH_MORE` returns to `RESEARCHING`
- outline `REFRAME` returns to `BRIEFED`
- script `RETURN_TO_OUTLINE` returns to `OUTLINING`
- script `RESEARCH_MORE` returns to `RESEARCHING`
- packaging `RETURN_TO_SCRIPT` returns to `SCRIPTING`

A workflow may revisit earlier stages whenever evidence changes the underlying premise.

Returning backward is not failure.

Publishing a weak video because work has already been spent is failure.

---

## 5. Storage Responsibilities

### Google Sheets

Sheets stores structured state and metadata.

It should eventually record:

- video ID
- channel ID
- lifecycle status
- topic
- thesis
- framing
- content pillar
- rationale
- packaging metadata
- production data
- cost
- publication metadata
- performance
- economics
- postmortem conclusions
- learning tags
- links to Drive artifacts

Sheets is not the primary home for large working documents.

### Google Drive

Drive stores the large per-video artifacts and production files.

The canonical video folder should eventually contain versions of:

- video brief
- research packet
- source log
- outline
- script
- packaging packet
- production packet
- assets
- narration
- project files where retained
- first cuts
- final export
- thumbnail
- captions
- postmortem where useful

### GitHub

GitHub stores the standards governing how those artifacts should be created.

Per-video working documents should not normally be committed to GitHub.

---

## 6. IDs and Naming

Every selected video receives a permanent `video_id`.

Recommended pattern:

`CH001-V0001`

The title can change.

The ID should not.

Drive folders may include both:

`CH001-V0001 - Working Video Title`

The ID allows systems to preserve continuity when the working title, final title, or packaging changes.

---

## 7. Artifact Versioning

Important artifacts should not be silently overwritten during development.

Recommended naming:

- `01_VIDEO_BRIEF_v1`
- `02_RESEARCH_PACKET_v1`
- `03_SOURCE_LOG_v1`
- `04_OUTLINE_v1`
- `04_OUTLINE_v2`
- `05_SCRIPT_v1`
- `05_SCRIPT_v2`
- `06_PACKAGING_PACKET_v1`
- `07_PRODUCTION_PACKET_v1`
- `08_QA_RECORD_v1`
- `09_POSTMORTEM_v1`

The exact Drive naming standard will be defined separately.

The operating principle is to preserve meaningful development history without creating unnecessary version clutter.

---

## 8. Quality Gate Philosophy

A stage does not pass merely because an artifact exists.

The artifact must satisfy the purpose of the stage.

Quality gates should evaluate the work against:

1. the portfolio standards
2. the channel-specific context
3. the video's own stated thesis and promise
4. the available evidence
5. the needs of the next stage

AI should be capable of rejecting its own output.

A critic should not automatically assume that revision is sufficient.

Allowed conclusions should include:

- insufficient evidence
- weak topic
- weak framing
- structurally broken story
- poor channel fit
- packaging that the script cannot fulfill
- production burden disproportionate to likely value

---

## 9. Human Review Philosophy

Green Knight should minimize unnecessary manual approvals, but it should not remove human judgment simply to make a workflow "fully automated."

Human intervention is most valuable when:

- a high-level thesis is being committed to
- research contains ambiguity
- a narrative choice materially changes the story
- factual or rights risk is meaningful
- packaging is strategically important
- a production decision depends on taste
- the output does not clearly meet the standard

As the system accumulates evidence and reliability, some review gates may become automated.

The standard should evolve based on performance, not ideology.

---

## 10. Kill Philosophy

Videos can be killed before publication.

Valid reasons include:

- thesis disproven by research
- insufficient evidence
- topic is less interesting than expected
- story cannot sustain long-form
- visual feasibility is poor
- channel fit is weak
- packaging cannot make the story appealing without misrepresentation
- production cost is disproportionate
- another video now dominates the opportunity cost

A killed video should retain:

- original idea
- development state
- reason for kill
- useful research
- lessons
- whether the idea could be reframed later

Green Knight should not treat sunk editorial effort as a reason to publish.

---

## 11. Definition of Production Ready

A video is production ready only when:

- thesis is stable
- required research is complete
- claims are supported
- outline is approved
- script is approved
- narration copy is final
- packaging direction is sufficiently defined
- the production packet is complete
- pronunciation issues are resolved
- required source materials are available
- channel visual context is available
- known rights-sensitive issues are identified
- the editor should not need to reinvent the editorial concept

If the editor must decide what the video is about, the upstream system failed.

---

## 12. Definition of Evaluated

A published video is not fully complete merely because it is live.

The loop closes only when:

- agreed performance windows are populated
- the result is compared against appropriate channel baselines
- observations are separated from interpretations
- major hypotheses are assessed
- durable lessons are captured
- useful learning tags are applied
- channel or portfolio standards are updated when evidence warrants it

A video becomes part of Green Knight's institutional memory only after this stage.

---

## 13. Lifecycle Governance

This lifecycle is portfolio-wide.

Individual channels may add requirements where justified, but should not casually redefine shared states.

If the shared lifecycle needs to change, update this canonical file rather than allowing each channel to create incompatible variants.

The goal is one operating language across the portfolio.
