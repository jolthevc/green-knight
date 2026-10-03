# AI and n8n Workflow Architecture

**Status:** Canonical portfolio-wide standard  
**Purpose:** Define how Green Knight uses n8n and AI models to create, evaluate, and improve media properties without building an unnecessarily complex automation stack.

---

## 1. Core Architecture Principle

Green Knight should not build one enormous workflow for the entire media lifecycle.

The preferred architecture is:

- a small number of stage-level workflows
- a few reusable shared subworkflows
- one lightweight orchestrator where a multi-stage run is useful
- persistent state in GitHub, Google Sheets, and Google Drive
- n8n as orchestration rather than memory

A workflow should be long enough to complete one coherent job and no longer.

The goal is not to minimize node count.

The goal is to make each workflow understandable, testable, recoverable, and replaceable.

---

## 2. n8n's Job

n8n should:

1. receive a structured input
2. load canonical context
3. resolve current lifecycle state
4. call the appropriate AI workflow
5. validate the result
6. save large artifacts to Drive
7. write concise structured state to Sheets
8. advance or return lifecycle state
9. hand work to humans where required
10. preserve enough execution metadata for debugging

n8n should not:

- become the canonical store of strategy
- contain large hard-coded channel definitions
- duplicate prompt text in many nodes
- rely on node-local memory for durable state
- hard-code model names throughout many workflows
- silently rewrite portfolio standards
- create channel-specific copies of shared workflows without a real need

---

## 3. Standard Workflow Input

Every major workflow should accept a common envelope where relevant:

```json
{
  "channel_id": "CH001",
  "video_id": "CH001-V0001",
  "action": "develop_video",
  "initiated_by": "manual|scheduled|upstream_workflow",
  "force": false
}
```

Not every workflow needs a `video_id`.

Channel ideation, for example, operates at portfolio level.

---

## 4. Shared Subworkflows

### A. LOAD_PORTFOLIO_CONFIG

Reads:

`00_portfolio/PORTFOLIO_CONFIG.yaml`

Returns live IDs and canonical paths.

This should be the first shared dependency rather than hard-coding IDs in every workflow.

### B. LOAD_CHANNEL_CONTEXT

Input:

`channel_id`

Loads the relevant channel GitHub folder and returns a normalized context bundle containing, where applicable:

- CHANNEL
- AUDIENCE
- CONTENT
- VOICE
- PACKAGING
- VISUAL_STYLE
- PRODUCTION
- EXAMPLES
- channel.yaml

### C. LOAD_VIDEO_STATE

Input:

`channel_id`, `video_id`

Reads the canonical video row from the channel Sheet.

Returns:

- current status
- topic
- thesis
- why_this_video
- framing
- packaging metadata
- Drive folder
- performance fields if relevant

### D. LOAD_ARTIFACT

Loads the current approved Drive artifact required by the next stage.

Examples:

- video brief
- research packet
- source log
- outline
- script
- packaging packet

### E. CALL_MODEL

Receives:

- model role alias
- system prompt
- task prompt
- context bundle
- output schema
- temperature / reasoning configuration where supported

Returns:

- raw model output
- structured output
- usage metadata
- model identity

Model names should be resolved through the canonical model registry rather than hard-coded throughout the workflow estate.

### F. VALIDATE_OUTPUT

Checks:

- valid JSON where structured output is required
- required fields
- enum values
- basic length expectations
- source references where required
- artifact-specific requirements

Validation should catch malformed output.

It should not pretend to replace editorial quality review.

### G. WRITE_DRIVE_ARTIFACT

Creates or updates the relevant versioned Drive artifact.

### H. UPDATE_SHEET_STATE

Writes only the structured fields appropriate to the stage.

### I. RECORD_DECISION

Records stage outcome such as:

- APPROVE
- REVISE
- RESEARCH_MORE
- REFRAME
- KILL

This may simply be represented through lifecycle state and artifact content until a dedicated run ledger is justified.

---

## 5. Major Workflows

Green Knight should initially maintain approximately seven major workflows.

### Workflow 1: CHANNEL_IDEATION

**Purpose:** Generate, refine, and compare new channel theses.

**Inputs:**

- portfolio overview
- channel creation standards
- current portfolio
- prior killed / active channels
- portfolio learnings
- optional strategic constraints

**Model:** Premium reasoning.

**Outputs:**

- structured channel concepts
- rationale
- audience
- content engine
- positioning
- opportunity
- risks
- key hypotheses
- suggested next diligence

**Writes to:** `00_CHANNELS` only after concepts are intentionally accepted into the idea database.

This workflow should not create channel folders automatically.

---

### Workflow 2: VIDEO_IDEATION

**Purpose:** Generate a high-quality pool of video ideas for one channel.

**Inputs:**

- channel context
- prior videos
- prior performance
- current learnings
- content pillars
- optional external research

**Model:** Premium reasoning.

**Output per idea:**

- topic
- thesis
- why_this_video
- framing
- pillar
- initial packaging territory
- why it fits now
- risks

**Writes to:** channel Sheet as `IDEA` rows.

The workflow should generate diversity rather than 30 variants of the same idea.

---

### Workflow 3: VIDEO_DEVELOPMENT

**Purpose:** Move a selected video from brief through approved script.

This should be one orchestrator calling several smaller subworkflows, not one enormous prompt.

Substages:

1. BRIEF
2. RESEARCH
3. RESEARCH_REVIEW
4. OUTLINE
5. OUTLINE_REVIEW
6. SCRIPT
7. SCRIPT_REVIEW

The orchestrator owns state transitions.

The stage workflows own artifact quality.

This is the longest logical workflow in the system, but it should remain modular.

---

### Workflow 4: PACKAGING

**Purpose:** Develop title-thumbnail packages and verify promise alignment.

**Inputs:**

- channel packaging standard
- audience
- approved script
- approved outline
- relevant historical performance

**Model:** Premium reasoning / creative model.

**Passes:**

1. generate diverse packaging territories
2. critique and select finalists

Avoid excessive internal tournaments unless evidence supports them.

**Writes:**

- packaging packet to Drive
- concise final title / thumbnail concept to Sheets once approved

---

### Workflow 5: PRODUCTION_PACKET

**Purpose:** Translate the approved editorial product into an editor-ready visual plan.

**Inputs:**

- approved script
- source log
- visual style
- production standard
- packaging direction

**Model:** Premium reasoning with strong multimodal / visual-planning capability where available.

**Output:** Production packet.

A reviewer may critique the packet only when the content is unusually complex or the first pass fails validation.

---

### Workflow 6: QA_ASSIST

**Purpose:** Assist human QA.

AI can check:

- script-to-edit consistency
- missing sections
- visible text
- number/name consistency
- thumbnail/title alignment
- obvious visual mismatch

AI should not be the sole authority on rights-sensitive or high-risk issues.

**Model:** Capable multimodal model.

Human final approval remains appropriate initially.

---

### Workflow 7: PERFORMANCE_ANALYSIS

**Purpose:** Turn performance data into disciplined learning.

**Inputs:**

- video Sheet row
- channel baselines
- original video brief
- packaging packet
- relevant retention / analytics
- prior channel learnings

**Model:** Premium reasoning.

**Outputs:**

- observations
- interpretations
- confidence
- confounders
- primary learning
- learning tags
- next action
- possible portfolio relevance

**Writes:**

- detailed postmortem to Drive
- concise structured learning to Sheets

Durable rules are not automatically written into GitHub.

Promotion into GitHub requires repeated evidence or intentional human approval.

---

## 6. Optional Later Workflows

Do not build these until needed.

Potential examples:

- NARRATION_AUTOMATION, only if production volume later makes editor-led voice generation a material cost or bottleneck
- CHANNEL_REVIEW
- PORTFOLIO_REVIEW
- SPONSORSHIP_MATCHING
- AFFILIATE_OPTIMIZATION
- LOCALIZATION
- SHORTS_REPURPOSING
- THUMBNAIL_TEST_ANALYSIS
- CONTENT_REFRESH
- ARCHIVE_HARVEST_ANALYSIS

The system should earn complexity.

---

## 7. Two-Pass Quality Pattern

For high-leverage creative work, the default pattern should be:

### Pass 1: Create

One strong model creates the artifact.

### Pass 2: Critique and revise

A separate call evaluates the artifact against:

- portfolio standard
- channel context
- artifact standard
- user promise
- evidence

The second call may use:

- the same premium model with a critic prompt
- a different premium model where useful

Avoid automatically adding third, fourth, or fifth model passes.

If an artifact repeatedly fails after two strong passes, the issue is likely upstream:

- bad idea
- weak research
- unclear channel definition
- poor prompt
- insufficient evidence

Do not solve upstream ambiguity with endless model calls.

---

## 8. State Machine Behavior

The workflow should respect the canonical lifecycle.

AI outputs can recommend state transitions, but the workflow must validate them.

Example:

```
RESEARCH_REVIEW
  PROCEED       -> OUTLINING
  RESEARCH_MORE -> RESEARCHING
  REFRAME       -> BRIEFED or RESEARCHING
  KILL          -> KILLED
```

State transitions should be explicit.

Do not infer progress merely because a file was created.

---

## 9. Error Handling

Every workflow should fail cleanly.

At minimum:

- do not advance status if artifact creation fails
- do not overwrite the last approved artifact with malformed output
- preserve retryability
- report which stage failed
- preserve input IDs
- avoid partial writes across systems where practical

For expensive model calls, retry only when the failure is technical.

Do not blindly retry low-quality editorial output with the exact same prompt and context.

---

## 10. Human Handoff

Human work should enter at clearly defined points.

Initial likely handoffs:

- channel approval and one-time narrator voice selection
- editor narration generation from the approved script using the locked channel voice
- channel approval
- strategic video selection where desired
- high-stakes editorial ambiguity
- final packaging selection
- video editing
- final QA

As system quality improves, Green Knight can reduce manual gates.

Narration generation is intentionally a production handoff rather than an automated TTS workflow at the initial scale. n8n should define and validate the narrator profile, not manufacture per-video audio unless scale later justifies the plumbing.

Do not make human approval mandatory at every stage simply because a human exists.

---

## 11. Workflow Length Principle

A useful rule:

> One workflow should correspond to one decision or one durable artifact family.

Examples:

Good:
- video ideation
- research
- outline
- script
- packaging

Bad:
- one workflow containing every stage, every model, every retry, every analytics loop, and every channel-specific exception

The orchestration layer may connect many subworkflows while keeping each component understandable.

---

## 12. Cost Philosophy

Green Knight is not optimizing for the lowest AI bill.

It is optimizing for the best economics of the media asset.

A $2 extra model call is irrelevant if it materially improves a video that costs $100 to produce and may generate thousands of dollars over its lifetime.

However, expensive models should be used where reasoning quality can change the outcome.

Do not spend premium-model tokens on:

- renaming files
- parsing simple JSON
- formatting dates
- copying metadata
- extracting obvious fields
- deterministic validation
- routine status updates

Spend on judgment.

Save on plumbing.

---

## 13. Initial Build Order

Build in this order:

1. LOAD_PORTFOLIO_CONFIG
2. LOAD_CHANNEL_CONTEXT
3. LOAD_VIDEO_STATE
4. model registry / CALL_MODEL
5. validation
6. Drive writer
7. Sheet writer
8. VIDEO_IDEATION
9. VIDEO_DEVELOPMENT stage workflows
10. PACKAGING
11. PRODUCTION_PACKET
12. PERFORMANCE_ANALYSIS
13. QA assistance

Do not build the entire system before one real channel and one real video have tested the contracts.
