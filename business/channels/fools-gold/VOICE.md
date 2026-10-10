# Curious, precise narration

A curious adult narrator with restrained intrigue and occasional dry wit. The voice makes the mechanism intelligible without glorifying the perpetrator or mocking victims.

## Audition

Test 30–45 seconds with an apparent promise, a financial amount, a difficult name, a reveal and a qualified finding. Select a narrator who can sound natural while distinguishing a claim from an established fact.

The owner chooses the voice. Record provider, voice ID, settings, controls, pronunciations and observed WPM in metadata.json. No provider or narrator is selected yet.

## Runtime

Plan initially at 150 spoken words per minute plus extra intentional pauses and silent holds. Around 1,200–1,400 words is a starting range, not a quota.

Estimated seconds = word_count / assumed_or_observed_wpm × 60 + extra_pause_seconds + silent_hold_seconds.

Ordinary punctuation pauses are already reflected in observed pace. Count extra silence once. The finished video, including closing, must last 480–600 seconds and be measured.

## Non-spoken cues

Use delivery-cues.json beside clean script.txt. Script paragraphs separated by blank lines are P001, P002, etc. Each cue has an exact opening anchor and the current script_version.

Editorial fields:
- pace: natural / slower / brisk.
- intent: curious / matter_of_fact / skeptical / amused / reflective.
- emphasis: exact words in the identified paragraph.
- pause_after_seconds: intentional extra silence.
- pronunciation_notes as needed.

Use curiosity for the puzzle, slower delivery for an important money-flow distinction and a brief pause after the reveal. Use matter-of-fact delivery for legal status and documented consequences. Humor can target an absurd claim; it should not target a harmed person's intelligence.

Do not whisper allegations as if suspense establishes truth. Avoid constant sinister delivery, shouting and a dramatic sting in every line.

These are editor directions, not TTS provider API parameters. Verify provider-supported controls before converting. Unsupported cues require alternate takes, segmented narration or editing. No untested bracketed tags or invented SSML in the spoken input.

## Listening QA

Check names, amounts, distinction between alleged and established conduct, tonal restraint and comprehension. Confirm no directions or citations were spoken. Update anchors and source/visual references after wording changes.

A good audition does not approve the whole cut. Listen to the actual finished narration with the music and inspect rendered duration.
