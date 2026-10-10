# Investigative narration

Calm, engaging and humane. Sound interested in the evidence, not pleased that someone failed. Intrigue comes from the contradiction, timeline and mechanism.

Do not imitate a sensational true-crime narrator. Avoid whispered accusations, sneering, doom on every sentence and a constant rising build.

## Audition and settings

Request a 30–45 second audition with an opening contradiction, a difficult name, a financial number and a measured counterpoint. The owner chooses the voice. Record provider, voice ID, settings, supported controls, pronunciations and observed WPM in the channel's narration.json and a versioned story metadata snapshot.

The voice must remain stable across Fallen Angels episodes. No provider, narrator or settings are selected during setup.

## Timing

Plan initially at 150 spoken words per minute plus intentional extra pauses and silent holds. Around 1,200–1,400 words is a starting range, not a quota or proof of duration.

Estimated seconds = word_count / assumed_or_observed_wpm × 60 + extra_pause_seconds + silent_hold_seconds.

Count only extra silence beyond natural punctuation. A document shown beneath narration does not add runtime. Measure the actual finished video, including closing; it must last 480–600 seconds.

## Non-spoken cue sidecar

Use delivery-cues.json alongside clean script.txt. Blank-line-separated script paragraphs are P001, P002, etc. Each cue has:
- paragraph_id and exact opening anchor.
- pace: natural, slower or brisk.
- intent: curious, matter_of_fact, skeptical, amused or reflective.
- emphasis: exact words present in the paragraph.
- pause_after_seconds: intentional extra silence.
- pronunciation_notes where needed.

Use curious delivery for the opening puzzle, matter-of-fact delivery for financial evidence, slower delivery for the mechanism and reflective delivery for consequences. Skepticism questions an explanation, not a person's character. Humor is occasional and should not target harmed employees or customers.

A small pause before a timeline reversal can help. Do not convert uncertainty into ominous emphasis or emphasize every amount as a shock.

These are instructions for the editor, not provider API fields or text to feed into TTS. Verify supported controls before converting. Unsupported cues require alternate takes, segmented narration or editing. No unsupported bracketed tags or invented SSML.

## Final listening check

Check that no direction or citation was spoken. Confirm names, numbers, tone, pacing and intelligibility over music. If the script changes, update anchors and evidence/visual references before regenerating audio. An estimate cannot satisfy measured-runtime approval.

## Shared production mechanics

Follow [NARRATION_STANDARD.md](../../NARRATION_STANDARD.md) for audition, profile versioning, pronunciation, coherent takes, retakes and full listening. [narration.json](narration.json) is the canonical channel voice; metadata stores its per-episode snapshot. Reuse an unchanged approved profile without another selection step. A material change creates a new profile version.

Delivery cues now use schema_version 2 and the exact script hash as well as script_version/paragraph anchors. Optional inflection describes neutral, question or settled delivery. These shared technical rules govern abbreviated cue descriptions above.

## Channel-specific listening test

Can the listener distinguish weakness, warning and trigger? Keep the causal passages clear and settled. Avoid an ominous rise at every date; tragedy should not replace explanation or imply every warning made failure predictable.
