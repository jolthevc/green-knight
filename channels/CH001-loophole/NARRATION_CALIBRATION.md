# Loophole Narration Calibration (loophole_narrator_v1)

**Status:** Audition material. Not a video script and not for publication.  
**Purpose:** Compare candidate voices on the same passage before locking `loophole_narrator_v1`.

## 1. Narrator Brief

The narrator should sound interested in clever exploitation, not emotionally hyped by the event.

- Smart, dry, understated, slightly mischievous.
- Conversational, with crisp diction.
- Neutral American accent, medium vocal register.
- Confident but not theatrical.
- Not a sports-announcer voice. Not a movie-trailer voice.
- Humor is underplayed: let the line land, don't sell it.
- Mechanisms are explained patiently.
- Default pace roughly 145-155 spoken words per minute. This is a guide, not a hard rule.

## 2. Audition Rules

- Generate the exact passage below, unedited, with every candidate voice.
- Use the same model, the same settings and the same output format for every candidate.
- Prefer stable, production-quality voices you own or have saved to your library. Avoid temporary or default voices.
- Listen on speakers and on headphones.
- Select for full-episode durability, not the most impressive ten-second demo.

## 3. Calibration Passage

The facts below are calibration material. The quoted rule is a paraphrase written for audition, not verified rule text. Nothing here should be reused in a video without the normal research workflow.

> In 1978, the fastest car at the Swedish Grand Prix had a fan on the back. A big one.
>
> Here's how it worked. Formula One had banned moving aerodynamic devices, the flaps and wings that pushed a car into the road. But the rules still allowed a fan, as long as its job was cooling the engine. So Brabham fitted a fan that cooled the engine. It also pulled air out from under the car, and sucked the whole thing onto the track.
>
> The rule, roughly, said this: "Any device whose primary purpose is aerodynamic, and which moves while the car is in motion, is prohibited."
>
> Primary purpose. Brabham's position was that the fan's primary purpose was cooling. Its secondary purpose was winning.
>
> And it did win. Niki Lauda took the race by more than half a minute. Rival teams protested, and within weeks the car was withdrawn. It never raced again. Not because it broke the rule, but because everyone agreed it was about to.

About 165 words: roughly 65-70 seconds at the target pace.

## 4. What Each Part Tests

1. **Opening hook** (paragraph 1): does the voice make a strange fact interesting without hype? "A big one." should be dry, not a joke.
2. **Mechanism** (paragraph 2): patience and clarity. Can a listener follow cause and effect at one listen?
3. **Quoted rule language** (paragraph 3): a shift into precise, slightly slower reading. Quotation should be audible without sounding like a different person.
4. **Understated humor** (paragraph 4): "Its secondary purpose was winning." must land flat and dry. Reject any take that winks or punches it.
5. **Serious factual passage** (paragraph 5): calm authority. The final line should feel considered, not dramatic.

## 5. Scorecard (1-5 per candidate)

| Criterion | What good sounds like |
|---|---|
| Brief fit | Smart, dry, slightly mischievous |
| Not announcer / not trailer | No hype, no booming |
| Mechanism clarity | Easy to follow at one listen |
| Rule quotation | Precise, clearly a quotation |
| Humor delivery | Understated, punchline at the end of the sentence |
| Serious register | Calm, credible |
| Diction and accent | Crisp, neutral American |
| Pace | Close to 145-155 wpm without sounding rushed |
| Consistency | Same character across all five parts |
| Artifacts | No glitches, odd breaths or mispronunciations |

## 6. Locking the Voice

When a winner is chosen, update `narration.yaml`:

- `voice_id`: the winning provider voice ID.
- `model_id`: the baseline model used in the audition.
- `voice_settings`: the baseline settings used in the audition, if relevant.
- `profile_status`: `locked`.

Then set the channel's operational `narration_status` to `READY`.

The locked profile is the voice the production editor receives access to. The editor generates narration in-platform during the edit, using the approved script and this profile as the baseline.

A later narrator-identity change is a new profile (`loophole_narrator_v2`), not a silent edit to v1.

## 7. Production Handoff

The editor should receive:

- the approved script
- access to the locked Loophole voice
- the baseline model/settings recorded here
- pronunciation notes
- the Loophole voice and production standards

The editor may iterate delivery against picture, but may not change script wording or substitute a different narrator without approval.

## 8. Audition Log

- Candidates: _not yet auditioned_
- Winner: _none_
- Locked on: _not locked_
