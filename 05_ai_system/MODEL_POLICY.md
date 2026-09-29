# Model Selection Policy

**Status:** Canonical portfolio-wide standard  
**Purpose:** Define where Green Knight should spend on model quality, where it should optimize cost and speed, and how model choices should remain replaceable over time.

---

## 1. Principle

Green Knight should use the best economically sensible model for the decision being made.

The objective is not:

- cheapest possible inference
- most expensive model everywhere
- loyalty to one provider
- maximizing the number of model calls

The objective is:

> Put premium intelligence on decisions that materially change the quality, audience appeal, factual reliability, or economic value of the asset.

---

## 2. Do Not Hard-Code Model Names Into Workflow Logic

Model capabilities and pricing change.

n8n workflows should refer to logical model roles.

Example aliases:

- `premium_reasoning`
- `premium_writing`
- `premium_multimodal`
- `research_model`
- `fast_utility`
- `embedding_model`

The actual provider/model mapping should live in one machine-readable registry.

Changing the preferred model should require editing one registry, not dozens of nodes.

---

## 3. Premium Reasoning

Use for:

- channel ideation
- channel diligence
- video ideation
- research synthesis
- research audit
- outline creation
- outline critique
- script planning
- packaging strategy
- performance interpretation
- channel review
- portfolio learning

These stages involve judgment where small quality differences can materially affect the asset.

---

## 4. Premium Writing

Use for:

- final script drafting
- major script revision
- voice-sensitive narration
- difficult hooks
- language where channel identity matters

If the best reasoning model is also the best writer, the aliases may point to the same model.

Do not force provider diversity for its own sake.

---

## 5. Research Model

Use a model or agent capable of strong source-grounded web research when external facts are required.

Research output should preserve:

- sources
- dates
- scope
- uncertainty
- conflicting evidence

The research model should not be selected purely for prose quality.

---

## 6. Premium Multimodal

Use for:

- QA of finished video
- thumbnail evaluation
- visual-style evaluation
- complex production-packet planning
- frame-level consistency checks where appropriate

This role requires strong visual understanding.

---

## 7. Fast Utility

Use for:

- schema repair
- simple extraction
- normalization
- metadata generation
- short summaries of already-known structured information
- filename generation
- status explanations
- deterministic transformations that still benefit from language understanding

Where code or deterministic n8n logic is sufficient, prefer that over any model.

---

## 8. Critic Model Policy

High-leverage stages may use a second premium call.

The default is not a panel.

Use:

- one creator
- one critic/reviser

The critic must receive the relevant rubric and context.

It should be allowed to say:

- approve
- revise
- reframe
- research more
- kill

A critic that is forced to produce edits will often polish bad work instead of rejecting it.

---

## 9. Cross-Model Use

Using a different model for critique can be useful when:

- the stage is especially subjective
- the first model has a known bias
- factual challenge matters
- independent perspective is valuable

However, cross-model diversity is not itself a quality metric.

Do not create a multi-provider committee by default.

---

## 10. Cost Hierarchy

Green Knight should think about AI spend relative to downstream value.

Approximate hierarchy:

### Highest willingness to spend
- channel thesis
- video thesis
- research quality
- story architecture
- final script
- packaging
- postmortem interpretation

### Medium willingness to spend
- production packet
- thumbnail critique
- QA
- source organization

### Lowest willingness to spend
- formatting
- status changes
- file naming
- metadata copying
- deterministic transforms

---

## 11. Latency

Latency is secondary to quality for offline editorial production.

A 60-second excellent result is usually preferable to a 5-second mediocre result when the artifact will guide a video asset.

Fast models remain useful for interactive admin and utility tasks.

---

## 12. Model Testing

Before changing the canonical model for a stage, compare outputs on real Green Knight tasks.

Evaluate:

- factual reliability
- originality
- channel fit
- structural quality
- writing quality
- compliance with output schema
- need for human correction
- cost
- latency

Do not switch models based only on public benchmarks.

---

## 13. Escalation

A workflow may escalate from a utility model to a premium model when:

- confidence is low
- validation fails repeatedly
- ambiguity is material
- source conflict exists
- the stage is being blocked

Do not automatically escalate every task.

---

## 14. Current Philosophy

Green Knight should be comfortable spending more than a typical "YouTube automation" operation on editorial intelligence if it allows human production costs to remain low while materially improving audience outcomes.

AI is not merely a cost reducer.

It is intended to be the central editorial intelligence layer of the company.
