# Near Miss Narration Calibration (near_miss_narrator_v1)

**Status:** Audition material. Not a video script and not for publication.  
**Purpose:** Define the Near Miss narrator and compare candidate voices on the same passage before locking `near_miss_narrator_v1`.

## 1. Narrator Brief

A calm investigator reconstructing a timeline for an intelligent friend. Tension rises through detail, time and restraint, never through volume.

- Calm, precise, controlled and credible.
- Low-to-medium register; warm but unhurried.
- Neutral, internationally clear accent; crisp on numbers, times and technical terms.
- Explains mechanisms patiently, one causal link at a time.
- Gets slower and more exact as stakes rise, not louder or faster.
- Leaves real silence at the decision and the save.
- Respectful toward everyone involved; no blame, no sensationalism.
- Humor is rare and bone-dry; never during the crisis.
- Avoid: trailer voice, news-anchor urgency, true-crime melodrama, breathy suspense.
- Default pace roughly 140-150 spoken words per minute. Guidance, not a hard rule.

## 2. Voice Design / Search Prompt

Paste into ElevenLabs Voice Design, or use as a Voice Library search brief. Gender is deliberately unspecified: try variants with "male" and "female" added at the start and audition both.

```text
A calm, precise mature narrator with a low-to-medium register and a neutral, internationally clear accent. Measured, controlled delivery, like an experienced accident investigator walking an intelligent friend through a timeline. Warm but restrained and highly credible. Builds tension through careful pacing, exact wording and quiet emphasis rather than volume. Crisp consonants on numbers and times, steady breath, comfortable with pauses. Never dramatic, breathless, sensational or like a movie trailer. Clean, close-mic studio documentary narration.
```

## 3. Calibration Passage

Invented composite for audition only. The aircraft, crew, figures and quoted checklist line are illustrative and make no factual claim about any real event. Nothing here should be reused in a video without the normal research workflow.

> At eleven fifty-two at night, the first officer noticed that one number was wrong. Not by much. By about three hundred feet.
>
> An altimeter does not measure height directly. It measures air pressure, and converts it to altitude using a reference value the crew sets by hand. Set the wrong value, and every reading that follows is wrong in exactly the same way. Consistently. Convincingly.
>
> The checklist was unambiguous: "Altimeters. Set and cross-checked, both pilots."
>
> That night, only one had been set. The cross-check existed for precisely this situation, which may be why everyone assumed it had already happened.
>
> Investigators later estimated that, on that heading, the aircraft would have reached the ridgeline in under a minute. That is an estimate, not a certainty. What is certain is simpler. She asked. And the captain checked.

About 135 words: roughly 55-60 seconds at the target pace.

What each part tests:

1. **Cold open** (paragraph 1): quiet tension. "By about three hundred feet." should land low and exact, not dramatic.
2. **Mechanism** (paragraph 2): patience and clarity at one listen. "Consistently. Convincingly." should sound considered, not ominous.
3. **Quoted procedure** (paragraph 3): a clean shift into quoted language without becoming a different person.
4. **Dry bureaucratic irony** (paragraph 4): the only light moment. Level and respectful; reject any take that smirks.
5. **Counterfactual with evidence tier** (paragraph 5): calm authority, the estimate read plainly as an estimate, and real space before "She asked."

## 4. Scorecard (1-5 per candidate)

Judge full-episode durability: imagine 20 minutes of this voice, not 60 seconds.

| Criterion | What good sounds like |
|---|---|
| Brief fit | Calm, precise, controlled, credible |
| Tension without volume | Stakes rise through pacing and exactness, not loudness |
| Mechanism clarity | Causal chain easy to follow at one listen |
| Numbers and times | Crisp, unambiguous, never rushed |
| Quoted procedure | Precise, audibly a quotation, same character |
| Evidence tiers | "Estimate" and "certain" read plainly and differently |
| Silence | Comfortable pauses at the decision and the save |
| No melodrama | No trailer, anchor or true-crime delivery |
| Durability | Pleasant and unfatiguing over a full episode |
| Artifacts | No glitches, odd breaths or mispronunciations |

## 5. Locking the Voice

When a winner is chosen:

- save the provider voice to the Green Knight account / workspace
- record its provider `voice_id` in `narration.yaml`
- record the baseline `model_id` and relevant settings used in the audition
- set `profile_status: locked`
- set the portfolio Sheet `narration_status` to `READY`
- record the winner and lock date below

This can be done by telling the n8n agent, for example: "Lock CH005 narrator with voice_id ..., model_id ..., default settings."

The production editor then receives revocable access to the locked voice where supported, generates narration from the approved script during production, and may iterate delivery against picture but may not change script wording or substitute a different narrator without approval.

A later narrator-identity change is a new profile (`near_miss_narrator_v2`), not a silent edit to v1.

## 6. Audition Log

- Candidates: _not yet auditioned_
- Winner: _none_
- Locked on: _not locked_
