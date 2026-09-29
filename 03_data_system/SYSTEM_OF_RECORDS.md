# System of Records and Handoffs

**Status:** Canonical portfolio-wide standard  
**Purpose:** Define which Green Knight system is authoritative for each type of information and how GitHub, Google Sheets, Google Drive, n8n, and YouTube interact.

---

## 1. Why This Exists

Green Knight intentionally uses a lightweight stack.

That only works if each system has a clearly defined job.

The same fact should not be independently maintained in several places unless there is a specific reason.

When systems disagree, this document determines which source should be treated as canonical.

---

## 2. The Five Systems

### GitHub = rules, definitions, and durable operating knowledge

GitHub contains:

- portfolio strategy
- operating standards
- channel templates
- channel-specific definitions
- prompt files
- schemas
- workflow specifications
- quality standards
- durable portfolio learnings
- machine-readable configuration

GitHub answers:

> How should Green Knight think and operate?

### Google Sheets = structured operating state

Sheets contains:

- channel records
- video records
- lifecycle status
- concise pre-publication hypotheses
- concise packaging metadata
- production cost
- publication metadata
- standardized performance data
- economics
- structured learnings
- next actions
- links to canonical GitHub and Drive locations

Sheets answers:

> What exists, what state is it in, what did we believe, what happened, and what should happen next?

### Google Drive = large working artifacts and media files

Drive contains:

- briefs
- research
- source logs
- outlines
- scripts
- packaging packets
- production packets
- assets
- edits
- final media
- detailed QA
- detailed postmortems

Drive answers:

> Where is the actual work product?

### n8n = orchestration

n8n:

- reads GitHub context
- reads structured state from Sheets
- reads and writes Drive artifacts
- calls AI models
- validates outputs
- changes lifecycle status
- routes work
- hands off to humans
- retrieves analytics
- writes results back to Sheets

n8n should not be the long-term source of truth for portfolio knowledge.

### YouTube = distribution and audience evidence

YouTube provides:

- published media
- audience distribution
- performance data
- monetization data

Relevant data should flow back into Sheets.

---

## 3. Canonical Ownership by Information Type

### Portfolio strategy
**Canonical:** GitHub

### Channel strategic definition
**Canonical:** GitHub channel folder

Sheets may contain a concise summary for comparison.

### Channel status
**Canonical:** Sheets

GitHub configuration may mirror status for workflow convenience, but Sheets is the live operating state unless the architecture is deliberately changed.

### Video status
**Canonical:** channel Sheet tab

### Video thesis / why / framing
**Canonical structured summary:** Sheets  
**Canonical detailed brief:** Drive

The Sheet should remain concise.

Drive contains nuance.

### Research
**Canonical:** Drive

### Sources
**Canonical:** Drive source log

### Outline
**Canonical:** Drive

### Script
**Canonical:** Drive

### Packaging development
**Canonical detailed artifact:** Drive  
**Canonical final structured summary:** Sheets

### Production files
**Canonical:** Drive

### Final video and thumbnail master
**Canonical internal file:** Drive  
**Canonical public distribution:** YouTube

### Performance data
**Canonical operating copy:** Sheets  
**Origin:** YouTube

### Detailed postmortem
**Canonical:** Drive

### Primary learning / tags / next action
**Canonical structured record:** Sheets

### Durable channel-level creative rule
**Canonical after validated adoption:** GitHub channel files

### Durable portfolio-wide rule
**Canonical after validated adoption:** GitHub portfolio standards or learnings

---

## 4. The Promotion Path for Learning

A useful observation should move through the system deliberately.

Example:

### Step 1: YouTube
A video generates unusually strong CTR.

### Step 2: Sheets
The performance metrics are recorded.

### Step 3: Drive postmortem
The team records:

- observation
- interpretation
- confidence
- confounders
- what not to infer

### Step 4: Sheets structured learning
The row receives a concise:

- `primary_learning`
- `learning_tags`
- `next_action`

### Step 5: Channel GitHub context
If repeated evidence supports a durable channel-specific principle, update the relevant channel file.

Example:

`PACKAGING.md`

### Step 6: Portfolio GitHub learning
If a pattern appears across multiple channels and survives scrutiny, it may become a portfolio-level principle.

This prevents one noisy result from immediately becoming governance.

---

## 5. How an AI Should Start a Channel Task

For a channel-specific editorial task, an AI or n8n workflow should generally load:

1. relevant portfolio-wide standard from GitHub
2. channel-specific GitHub context
3. the target video row from the channel Sheet
4. any required existing Drive artifact from the current lifecycle stage

Do not load the entire portfolio by default.

Context should be sufficient, relevant, and canonical.

---

## 6. How an AI Should Write Results

When a workflow produces a large artifact:

1. save the artifact to the canonical video Drive folder
2. preserve appropriate versioning
3. update the video lifecycle status in Sheets
4. update only the concise structured Sheet fields required by the stage
5. do not paste the entire artifact into a Sheet cell
6. do not commit per-video working artifacts to GitHub

---

## 7. Channel Creation Handoff

When a channel concept is approved:

### GitHub
Create a channel folder by cloning the canonical channel template and complete its definitions.

### Sheets
Create or update the `00_CHANNELS` row.

Duplicate `CH_TEMPLATE` into a new channel video tab.

### Drive
Create the channel folder with:

- `Unpublished`
- `Published`

### Configuration
Write the relevant GitHub, Sheets, and Drive identifiers into the channel configuration.

All systems should use the same permanent `channel_id`.

---

## 8. Video Creation Handoff

When a video is selected:

### Sheets
Assign permanent `video_id`.

Set status to `SELECTED`.

### Drive
Create the canonical video folder under `Unpublished`.

Create:

- `Assets`
- `Production`
- `Final`

Write the folder link back to the video row.

### GitHub
Do not create a per-video folder.

The video uses the shared standards plus its channel definition.

---

## 9. Publication Handoff

When QA passes and the video publishes:

### YouTube
Video goes live.

### Sheets
Write:

- final title
- publish date
- runtime
- production cost
- YouTube URL
- status

### Drive
Move the canonical video folder from `Unpublished` to `Published`.

Do not create a duplicate.

### Analytics
Begin standardized performance capture.

---

## 10. Analysis Handoff

When the measurement window matures:

### Sheets
Populate standardized metrics.

### Drive
Create or update detailed postmortem.

### Sheets
Write concise:

- result class
- primary learning
- learning tags
- next action

### GitHub
Update channel or portfolio standards only when evidence justifies promotion into durable knowledge.

---

## 11. Conflict Resolution

If the same information appears in multiple systems and conflicts:

### Strategic / creative rule conflict
Use GitHub.

### Lifecycle status conflict
Use Sheets.

### Working artifact conflict
Use the latest approved canonical Drive artifact.

### Public performance conflict
Refresh from YouTube, then update Sheets.

### Detailed learning conflict
Review the postmortem and underlying evidence before promoting any conclusion.

Do not silently choose whichever copy is easiest to access.

---

## 12. Avoiding Duplication

Do not:

- paste full scripts into Sheets
- store portfolio governance in Drive
- store live analytics in GitHub
- rely on n8n execution history as institutional memory
- create separate prompt copies inside each channel unless the channel genuinely overrides the shared prompt
- create multiple Drive copies of published video folders
- maintain the same learning as independent free-text in several systems

Use links and IDs to connect systems rather than duplicating content.

---

## 13. Shared IDs

The system depends on stable identifiers.

### Channel
`channel_id`

Example:

`CH001`

Used in:

- GitHub channel path
- Sheets portfolio row
- channel Sheet tab
- Drive channel folder
- n8n input
- analytics mapping

### Video
`video_id`

Example:

`CH001-V0001`

Used in:

- channel Sheet row
- Drive video folder
- artifact metadata
- n8n input
- analytics mapping
- postmortem

Titles and names can change.

IDs should not.

---

## 14. Context Principle

A future AI should never need this original ChatGPT conversation to understand how Green Knight works.

The combination of:

- portfolio overview
- system-of-record standard
- channel standards
- video standards
- data schema
- storage standard
- machine-readable config

should provide sufficient context to operate the system correctly.

When a recurring ambiguity appears, improve the canonical documentation rather than relying on chat memory.
