# Prompt Architecture

**Status:** Canonical portfolio-wide standard  
**Purpose:** Define how Green Knight prompts are structured, versioned, loaded, and reused.

---

## 1. Prompt Philosophy

Prompts should provide enough context for excellent judgment without becoming bloated transcripts of every Green Knight rule.

A prompt should tell the model:

- its job
- the objective
- the relevant context
- the constraints
- the artifact standard
- what good looks like
- what failure looks like
- the required output contract

Do not duplicate every portfolio document inside every prompt.

Load canonical context separately.

---

## 2. Prompt Components

A major AI call should generally be assembled from:

### A. System role
What function the model serves.

### B. Task objective
What artifact or decision is required.

### C. Portfolio context
Only the relevant portfolio standards.

### D. Channel context
Always load `CHANNEL_CORE.md` for an instantiated channel, then only the deeper channel files relevant to the stage.

### E. Video state
Relevant structured fields from Sheets.

### F. Existing artifacts
Only artifacts required for this stage.

### G. Stage standard
The canonical artifact standard.

### H. Output contract
Schema or clear structured format.

### I. Decision permissions
Whether the model may approve, revise, reframe, research more, or kill.

---

## 3. Context Minimization Without Under-Contexting

Green Knight prefers sufficient context over minimal-token prompts.

However, the system should not load the entire repository into every call.

Examples:

### Video ideation should load
- portfolio overview excerpt if needed
- `CHANNEL_CORE.md`
- content
- examples
- historical video performance / learnings

It usually does not need:
- production standard
- full Drive architecture
- QA standard

### Script drafting should load
- `CHANNEL_CORE.md`
- audience
- voice
- approved outline
- research packet
- source log
- script standard

It usually does not need:
- entire portfolio channel ideation standard
- Drive folder standard
- portfolio database schema

The goal is relevant richness.

---

## 4. Shared Prompts vs Channel Context

Prompts should generally remain shared.

Channel differentiation should come from loaded channel context.

Avoid:

`script_prompt_business.md`

`script_prompt_history.md`

`script_prompt_travel.md`

unless those categories genuinely require different reasoning processes.

Prefer:

`script.md`

plus the appropriate channel context.

---

## 5. Prompt Versioning

Prompts live in GitHub.

Use versioning through normal Git history.

If a workflow needs explicit prompt-version metadata, use a simple semantic label inside the file.

Do not create dozens of duplicate prompt files for minor revisions.

---

## 6. Output Contracts

Where downstream automation depends on structure, require structured output.

Examples:

- ideation lists
- review decisions
- lifecycle outcomes
- learning tags
- metadata

Where the output is primarily a rich artifact, allow natural Markdown plus a small structured header.

Examples:

- research packet
- outline
- script
- production packet

Do not force long-form creative writing into awkward JSON simply because n8n can parse it.

---

## 7. Critic Prompts

Critic prompts should:

- receive the original objective
- receive the artifact
- receive the standard
- identify specific failures
- distinguish blocking from nonblocking issues
- allow rejection
- avoid rewriting for stylistic novelty

The critic should focus on decision quality.

---

## 8. Anti-Anchoring

Prompts should avoid unnecessary exact scores, examples, or outputs that can anchor the model.

Use qualitative standards unless numeric calibration has a real operational purpose.

If numerical scoring is used, define anchors carefully and test for score clustering.

---

## 9. Examples and Anti-Examples

Where creative calibration matters, prefer:

- a small number of strong examples
- a small number of revealing anti-examples
- explanation of why each works or fails

Do not flood prompts with examples that cause imitation.

Channel `EXAMPLES.md` should do most of this work.

---

## 10. Prompt Failure Modes

Avoid:

- giant monolithic prompts
- duplicated standards
- conflicting instructions
- stale copied channel context
- asking one model to perform unrelated stages simultaneously
- forcing every answer into a score
- vague "make it engaging" guidance
- hidden assumptions
- prompts that cannot reject bad inputs

---

## 11. Prompt Directory

Initial shared prompt set:

```
05_ai_system/prompts/
  channel_ideation.md
  video_ideation.md
  video_brief.md
  research.md
  research_review.md
  outline.md
  outline_review.md
  script.md
  script_review.md
  packaging.md
  production_packet.md
  performance_analysis.md
```

These prompts are orchestration-facing instructions.

The detailed standards remain canonical in their respective folders.
