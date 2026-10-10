# Voice and non-spoken directions

A warm, curious, confident adult narrator. Conversational rather than promotional; interested rather than breathless. Small moments of dry humor. Let a surprising mechanism earn the emphasis.

## Calibration

Choose the narrator through an owner-reviewed 30–45 second audition containing a puzzle, money figure, difficult name and quiet payoff. Test comprehension and naturalness, then record provider, voice ID, supported controls, pronunciation choices and observed speaking speed in metadata.json. No provider is chosen yet.

As a planning assumption, try 150 spoken words per minute plus explicit pauses and silent visual holds. Actual delivery can differ. Around 1,200–1,400 words often provides a workable starting draft, but calculate and then measure the episode; this is not a requirement or guarantee.

Estimated seconds = word_count / observed_or_assumed_wpm × 60 + extra_pause_seconds + silent_hold_seconds.

The pace already includes ordinary punctuation pauses. Add only extra intentional pauses, and do not count a visual hold twice if narration continues over it. At 150 WPM, 1,300 words plus 25 seconds of extra pauses and 10 seconds of silence is about 555 seconds.

## Cue format

script.txt is authoritative spoken text. Blank-line-separated paragraphs are P001, P002, etc. delivery-cues.json stores:
- paragraph_id and anchor: an exact opening phrase identifying the paragraph.
- pace: natural / slower / brisk.
- intent: curious / matter_of_fact / skeptical / amused / reflective.
- emphasis: exact phrases inside that paragraph, sparingly.
- pause_after_seconds: extra silence beyond natural punctuation, normally short.
- pronunciation_notes: only actual names/terms that need help.

Use directions where they make comprehension or the reveal better. Slower for a key contrast, a short pause after a surprising figure, mild upward inflection for a real question, settled downward delivery for the answer. Raising emphasis should not mean shouting. No “dramatic” instruction on every sentence.

The cues are a production sidecar, not text to paste wholesale into TTS. If a provider supports controls, convert them using verified documentation. If not, split takes, select alternate readings and edit timing. Do not invent SSML syntax or assume bracketed tags are silent.

## Handoff and revision

Provide the clean script, cues, pronunciation notes and paragraph-linked visual plan. A reading copy may display clearly separated NON-SPOKEN direction blocks, but it must be generated from the authoritative script and must not be the untested TTS input.

Check an early voice take before generating the full episode. Final QA checks that no directions were spoken, names/numbers sound right, emotion is restrained and the finished video lasts 8–10 minutes. Edits to spoken wording update the script and claim map first.

## Example sidecar cue

For a hypothetical paragraph beginning “Someone still has to pay.”:

```json
{
  "paragraph_id": "P004",
  "anchor": "Someone still has to pay.",
  "pace": "slower",
  "intent": "curious",
  "emphasis": ["still"],
  "pause_after_seconds": 0.5,
  "pronunciation_notes": []
}
```

This example does not correspond to an existing script. Direction fields describe intent for the editor; they are not a provider's API parameters.
