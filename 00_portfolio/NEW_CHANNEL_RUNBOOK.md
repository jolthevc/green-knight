# New Channel Runbook

**Status:** Canonical operational runbook  
**Purpose:** Provide the step-by-step procedure for taking a Green Knight channel from approved concept to first published and evaluated videos.

---

## 1. How to Use This Runbook

This is the operational "start here" document for launching a new Green Knight channel.

It does not replace the detailed standards elsewhere in the repository.

Instead, it tells an AI, operator, or future team member:

- what to do
- in what order
- which system to update
- which canonical standard governs each step
- what must exist before moving forward
- what gets handed to a human editor
- what happens after publication

If there is uncertainty about *how* to complete a step, open the referenced canonical standard.

The sequence matters.

Do not jump directly from a channel idea to video production.

---

# PART I: CREATE THE CHANNEL

## Step 1: Confirm the Channel Concept Exists in the Portfolio Database

Open the Green Knight portfolio Sheet.

Canonical location is stored in:

`00_portfolio/PORTFOLIO_CONFIG.yaml`

Use the `00_CHANNELS` tab.

Before beginning channel creation, the row should contain at minimum:

- `channel_id`
- `channel_name` or working name
- `status`
- `concept`
- `target_audience`
- `audience_opportunity`
- `content_engine`
- `positioning`
- `economics_thesis`
- `next_action`

If the concept is still vague, do not create the full channel infrastructure yet.

Use the channel ideation / diligence process first.

---

## Step 2: Assign the Permanent Channel ID

Use the next available channel ID.

Example:

`CH001`

The channel ID is permanent.

The name can change.

The ID should be used across:

- GitHub
- Google Sheets
- Google Drive
- n8n
- analytics
- all video IDs

Never recycle an old channel ID.

---

## Step 3: Create the GitHub Channel Folder

Clone the canonical template:

```
01_templates/channel/
```

into:

```
channels/
  CH001-channel-slug/
```

The new folder should contain:

- `CHANNEL_CORE.md`
- `CHANNEL.md`
- `AUDIENCE.md`
- `CONTENT.md`
- `VOICE.md`
- `PACKAGING.md`
- `VISUAL_STYLE.md`
- `PRODUCTION.md`
- `EXAMPLES.md`
- `channel.yaml`
- `narration.yaml` when synthetic narration is used
- `NARRATION_CALIBRATION.md` when synthetic narration is used

Do not delete template sections because they are difficult to answer.

If a section genuinely does not apply, explain why.

---

## Step 4: Complete the Channel Definition

Fill the channel files before producing the first video.

Recommended completion order:

### 4.1 `CHANNEL.md`
Define:

- what the channel is
- why it exists
- viewer promise
- differentiation
- content engine
- risks
- hypotheses

### 4.2 `AUDIENCE.md`
Define:

- primary viewer
- motivations
- sophistication
- attention profile
- desired payoff
- what they find boring
- what they click
- anti-audience

### 4.3 `CONTENT.md`
Define:

- editorial territory
- content pillars
- recurring formats
- topic selection logic
- framing principles
- in-scope and near-miss ideas
- expansion paths

### 4.4 `VOICE.md`
Define:

- narrator personality
- writing behavior
- sophistication
- humor
- explanation style
- language to favor and avoid
- strong examples and anti-examples

### 4.5 `PACKAGING.md`
Define:

- title philosophy
- thumbnail philosophy
- curiosity style
- title-thumbnail relationship
- familiarity vs novelty
- strong and weak patterns

### 4.6 `VISUAL_STYLE.md`
Define:

- overall visual identity
- footage mix
- graphics
- maps
- charts
- typography
- motion
- music
- AI-image policy
- strong references
- anti-references

### 4.7 `PRODUCTION.md`
Define:

- target runtime
- cadence
- narration approach
- production complexity
- editor responsibilities
- asset rules
- revision expectations
- cost expectations

### 4.8 `EXAMPLES.md`
Seed with:

- good video concepts
- bad video concepts
- strong framings
- title examples
- thumbnail references
- hooks
- script examples
- visual references
- comparable channels

The examples file should improve over time.

### 4.9 `CHANNEL_CORE.md`
After the deeper channel files are coherent, complete the concise channel core.

This is the high-signal context loaded by essentially every channel-specific AI workflow.

It should summarize the deeper files rather than create a second set of rules.

### 4.10 `channel.yaml`
Complete the machine-readable configuration.

### 4.11 Narrator Definition
For a synthetic-narration channel:

- create `narration.yaml`
- create `NARRATION_CALIBRATION.md`
- define the narrator identity in `VOICE.md`
- generate a channel-specific voice-design / search prompt and calibration passage
- leave the provider voice as a candidate until a human chooses it

Workflow creation defines what the narrator should sound like. Human taste selects the actual voice.

---

## Step 5: Review the Channel as a Whole

Before creating videos, perform a cross-document review.

Ask:

- Is the viewer clearly defined?
- Is the content universe large enough?
- Is the content engine repeatable?
- Is the channel distinct?
- Could two independent writers produce recognizably similar work?
- Could two independent editors produce recognizably similar work?
- Is the packaging philosophy concrete?
- Is the visual bar clear?
- Are there obvious contradictions between files?
- Does the production model fit the expected economics?

Fix contradictions before launch.

---

# PART II: CREATE THE OPERATING INFRASTRUCTURE

## Step 6: Select and Lock the Channel Narrator

If the channel uses synthetic narration:

1. open the channel's `NARRATION_CALIBRATION.md`
2. audition or design candidate voices in the approved provider
3. choose the voice that best fits the full channel, not merely the most impressive short demo
4. save the winning voice under Green Knight's provider account/workspace
5. record its provider `voice_id`, baseline model, and relevant settings in `narration.yaml`
6. set `profile_status: locked`
7. set `00_CHANNELS.narration_status = READY`

This is a one-time human taste decision per narrator profile.

Do not automate voice selection.

If narration is not required, set `narration_status = NOT_REQUIRED`.

---

## Step 7: Create the Channel Tab in Google Sheets

Duplicate:

`CH_TEMPLATE`

Rename using:

`CH001 - Short Name`

Do not alter the canonical column structure.

Update the `00_CHANNELS` row with:

- current status
- GitHub path
- Drive folder once created

---

## Step 8: Create the Google Drive Channel Folder

Under:

```
Green Knight Holdings/
  Channels/
```

create:

```
CH001 - Channel Name/
  Unpublished/
  Published/
```

Do not add unnecessary empty folders.

Record the channel folder in:

- `00_CHANNELS.drive_folder`
- `channel.yaml`

Follow:

`04_storage_system/DRIVE_ARCHITECTURE.md`

---

## Step 9: Confirm Cross-System Identity

Before video ideation, verify:

### GitHub
Channel folder uses `CH001`.

### Sheets
Portfolio row and tab use `CH001`.

### Drive
Channel folder uses `CH001`.

### channel.yaml
Uses the same ID and the correct storage references.

If these disagree, stop and fix them.

---

# PART III: BUILD THE INITIAL CONTENT SLATE

## Step 10: Generate a Broad Video Idea Pool

Run the shared video ideation process.

Load:

- `CHANNEL_CORE.md`
- `CONTENT.md`
- `EXAMPLES.md`
- relevant portfolio learnings

Use:

`05_ai_system/prompts/video_ideation.md`

The goal is not to fill a calendar.

The goal is to identify high-quality tests of the channel thesis.

A new channel should normally begin with a broad pool of ideas rather than immediately choosing the first plausible topic.

---

## Step 11: Curate the Initial Slate

Select a smaller initial slate from the idea pool.

The slate should collectively test meaningful assumptions.

Consider diversity across:

- content pillars
- recognizable vs unfamiliar subjects
- framing
- packaging territories
- story types
- evergreen potential

Do not deliberately create weak videos merely to make the experiment "balanced."

Every selected video should still deserve to exist.

Write selected ideas to the channel Sheet.

---

## Step 12: Assign Video IDs

When an idea moves to `SELECTED`, assign:

`CH001-V0001`

then:

`CH001-V0002`

and so on.

Never reuse IDs from killed videos.

---

# PART IV: DEVELOP EACH VIDEO

## Step 13: Create the Video Drive Folder

When a video becomes `SELECTED`, create under:

`Unpublished/`

Example:

```
CH001-V0001 - Working Video Title/
  Assets/
  Production/
  Final/
```

Write the folder link into the video Sheet row.

Do not create empty editorial documents before they are needed.

---

## Step 14: Create the Video Brief

Use:

- selected video row
- channel context
- `VIDEO_BRIEF_STANDARD.md`
- `video_brief.md` prompt

Save the approved artifact in Drive as:

`01_VIDEO_BRIEF_v1`

Update Sheet status to:

`BRIEFED`

---

## Step 15: Research

Create:

- `02_RESEARCH_PACKET_v1`
- `03_SOURCE_LOG_v1`

Use:

- `RESEARCH_PACKET_STANDARD.md`
- `SOURCE_LOG_STANDARD.md`
- `research.md` prompt

Then run the research fact gate from `FACT_CHECK_STANDARD.md` as part of research review.

Allowed outcomes:

- PROCEED
- RESEARCH_MORE
- REFRAME
- KILL

Do not continue merely because research has already cost money.

---

## Step 16: Outline

Create the outline using:

- brief
- research
- source log
- channel context
- `OUTLINE_STANDARD.md`

Save:

`04_OUTLINE_v1`

Run outline review and approve the video's **Promise Lock** before scripting. The Promise Lock defines the core viewer promise, strongest truthful packaging claim, opening obligation, and important forbidden implications.

If revision is required, preserve meaningful versions.

Do not script a structurally weak outline.

---

## Step 17: Script

Create the script using:

- approved outline
- research
- source log
- audience
- voice
- approved Promise Lock

Save:

`05_SCRIPT_v1`

Run the script fact gate from `FACT_CHECK_STANDARD.md` as part of script review.

The script must be recordable, source-supported, and aligned with the approved Promise Lock.

Do not send a script to production simply because it is polished prose.

---

## Step 18: Packaging

Create:

`06_PACKAGING_PACKET_v1`

Use:

- final script
- channel `PACKAGING.md`
- audience context
- historical performance when available

Develop:

- distinct title territories
- distinct thumbnail concepts
- title-thumbnail pairs
- finalists
- recommended package
- opening alignment

Packaging outcome is `SELECT`, `RETURN_TO_SCRIPT`, or `KILL`. If the strongest truthful package requires a meaningful script/opening change, return to scripting rather than overstating the video.

Select a working final package when the outcome is `SELECT`.

The human editor or thumbnail specialist may improve execution later.

---

## Step 19: Create the Production Packet

Create:

`07_PRODUCTION_PACKET_v1`

Use:

- script
- source log
- `VISUAL_STYLE.md`
- `PRODUCTION.md`
- packaging direction
- portfolio editor and visual quality standards

The packet should label direction as:

- REQUIRED
- PREFERRED
- OPEN

The editor should know exactly where they have creative freedom.

---

# PART V: HAND OFF TO THE EDITOR

## Step 20: Create the Editor Brief

Use:

`06_production_system/EDITOR_BRIEF_TEMPLATE.md`

The editor should receive access to the smallest useful set of material.

### Normally share:

- Editor Brief
- approved script
- locked narrator profile / voice reference
- revocable access to the approved voice platform where synthetic narration is used
- pronunciation guidance as needed
- production packet
- packaging packet or relevant packaging direction
- source assets supplied by Green Knight
- channel `VISUAL_STYLE.md`
- relevant channel `EXAMPLES.md`
- necessary brand assets

### Normally do not require the editor to read:

- portfolio strategy
- full research packet
- entire source log
- database schema
- channel economics
- unrelated GitHub governance
- unrelated videos' working artifacts

Give them the context required to make good creative decisions without drowning them in internal documentation.

---

## Step 21: Explicitly Explain the Editor's Creative Role

The editor should understand:

> You are expected to bring taste and improve execution.

They may:

- generate and regenerate approved narration with the locked channel voice
- adjust narration pauses, emphasis, and pacing against picture
- source better footage
- improve visual treatments
- adjust pacing
- improve motion
- improve transitions
- improve composition
- propose stronger thumbnail execution
- reject generic-looking approaches

They may not silently alter:

- thesis
- facts
- narration wording or channel voice identity
- story architecture
- major claims
- major packaging promise

Follow:

- `EDITOR_CREATIVE_STANDARD.md`
- `VISUAL_QUALITY_STANDARD.md`

---

## Step 22: First Cut

Editor delivers the first cut into:

`Production/`

Green Knight reviews for:

- editorial fidelity
- visual quality
- pacing
- brand
- factual accuracy
- generic stock/slop
- graphics
- AI imagery
- sound
- package fulfillment

Do not wait until final export to identify fundamental visual problems.

---

## Step 23: Revisions

Send revision notes using:

### MUST FIX
Material issue.

### STRONG PREFERENCE
Desired creative treatment.

### OPTIONAL THOUGHT
Editor may use judgment.

Revision quality should improve over time as editor and channel become calibrated.

---

# PART VI: QA AND PUBLICATION

## Step 24: Final QA

Use:

`02_video_system/QA_STANDARD.md`

and:

`06_production_system/VISUAL_QUALITY_STANDARD.md`

QA includes:

- editorial
- factual
- visual
- audio
- brand
- rights
- packaging
- technical

Human final approval is appropriate initially.

---

## Step 25: Final Assets

Place approved assets in:

`Final/`

Typical package:

- final video master
- final thumbnail
- captions
- other publish-ready assets

Avoid ambiguous filenames such as:

`final-final-v7-real-final.mp4`

Maintain one clearly approved master.

---

## Step 26: Publish

Upload to YouTube.

Update the channel Sheet with:

- `final_title`
- `publish_date`
- `runtime_min`
- `production_cost`
- `youtube_url`
- status

Move the **same** video Drive folder from:

`Unpublished/`

to:

`Published/`

Do not duplicate it.

---

# PART VII: LEARN

## Step 27: Capture Performance

Initial standardized comparison window:

**30 days**

Capture the fields defined in:

`03_data_system/SHEETS_SCHEMA.md`

Including:

- impressions
- views
- CTR
- average percentage viewed
- revenue
- RPM
- lifetime metrics as they develop

---

## Step 28: Create the Postmortem

Use:

`POSTMORTEM_STANDARD.md`

Create:

`09_POSTMORTEM_v1`

Separate:

- observation
- interpretation
- confidence
- confounders

Do not rewrite the original hypothesis using hindsight.

---

## Step 29: Write Structured Learning Back to Sheets

Update:

- `result_class`
- `primary_learning`
- `learning_tags`
- `next_action`

Keep this concise.

Detailed analysis remains in the Drive postmortem.

---

## Step 30: Update Channel Standards When Evidence Justifies It

If repeated evidence reveals a durable channel-level rule, update the relevant GitHub file.

Examples:

- `PACKAGING.md`
- `CONTENT.md`
- `VOICE.md`
- `VISUAL_STYLE.md`
- `EXAMPLES.md`

Do not turn one video's result into a permanent rule.

---

# PART VIII: EARLY-CHANNEL CALIBRATION

## Step 31: Treat the First 3 to 5 Videos as Calibration

The first several videos deserve more active involvement.

Use them to establish:

- actual visual identity
- thumbnail language
- pacing
- production cost
- editor fit
- narration quality
- repeatable graphics
- AI-image usage
- what the audience actually responds to

Update the channel files as real evidence replaces initial assumptions.

---

## Step 32: Evaluate the Editor Relationship

After several videos ask:

- Is quality consistently above threshold?
- Is the editor improving weak directions?
- Are revisions decreasing?
- Does the channel look coherent?
- Is the editor good at thumbnail execution?
- Is Green Knight micromanaging because the standards are weak or because the editor is weak?
- Is production cost justified by output?

Do not solve persistent talent problems by creating increasingly exhaustive instructions.

---

# PART IX: DECIDE THE CHANNEL'S FUTURE

Use `00_portfolio/CHANNEL_TEST_STANDARD.md`.

A new channel should have an initial test plan before launch. The default first formal checkpoint is after approximately five published videos unless the channel has a reason to differ.

Once enough evidence exists, evaluate the channel.

Potential states:

- TESTING
- SCALE
- MAINTAIN
- HARVEST
- REPOSITION
- KILLED

A channel should not continue indefinitely merely because infrastructure has already been created.

Preserve the channel's history and learnings even if it is killed.

---

# Quick Launch Checklist

Before the first video enters production, confirm:

- [ ] permanent `channel_id`
- [ ] `00_CHANNELS` row
- [ ] GitHub channel folder complete
- [ ] audience defined
- [ ] content engine defined
- [ ] voice defined
- [ ] narrator profile selected / locked, or narration marked NOT_REQUIRED
- [ ] editor voice-platform access path defined where synthetic narration is used
- [ ] packaging defined
- [ ] visual style defined
- [ ] production model defined
- [ ] examples seeded
- [ ] `channel.yaml` complete
- [ ] channel Sheet tab created
- [ ] Drive channel folder created
- [ ] initial video idea pool generated
- [ ] first selected video has permanent `video_id`
- [ ] video Drive folder created
- [ ] brief approved
- [ ] research approved
- [ ] outline approved
- [ ] script approved
- [ ] packaging selected
- [ ] production packet complete
- [ ] editor brief complete

If all are true, the video is ready for human production.

---

# Automation Note

Initially, this runbook should be executed manually for the first pilot channel and first pilot video.

The purpose is to validate the operating system.

Once the process works cleanly end-to-end, n8n should automate the repetitive handoffs and state transitions described here.

The runbook should remain canonical even after automation.

n8n is an implementation of this process, not a replacement for understanding it.
