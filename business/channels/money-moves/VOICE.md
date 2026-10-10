# Narration and delivery

Curious, direct, lightly witty and confident without pretending the outcome was obvious. Give the decision and trade-off room to register. Keep the energy conversational, with contrast between the setup, choice and consequence.

## Voice selection

Audition 30–45 seconds containing a constraint, two alternatives, a difficult brand/name and a consequential reveal. The owner chooses the narrator. Record provider, voice ID/settings, supported controls, pronunciation notes and observed speaking speed in story metadata. No voice or provider is selected yet.

Do not assume the same narrator as Pretty Penny. Channel identity should be consistent within Money Moves.

## Timing

Start planning at 150 spoken words per minute plus extra pauses and silent holds. Around 1,200–1,400 words is a useful starting range, not a fixed quota.

Estimated seconds = word_count / assumed_or_observed_wpm × 60 + extra_pause_seconds + silent_hold_seconds.

Ordinary punctuation pauses are already reflected in observed pace. Count extra silence once; visuals running under narration do not add runtime. Actual rendered video must be 480–600 seconds including the closing.

## Non-spoken cues

Use the shared delivery-cues.json template. Its script_version must match metadata. Blank-line-separated paragraphs in script.txt are P001, P002, etc.

Each purposeful cue contains paragraph_id, an exact opening anchor, pace (natural/slower/brisk), intent (curious/matter_of_fact/skeptical/amused/reflective), emphasis phrases present in that paragraph, pause_after_seconds and pronunciation_notes.

Use:
- Curious delivery for a real strategic question.
- Slightly slower delivery when comparing options or explaining a constraint.
- A short extra pause after the choice or surprising result.
- Mild emphasis on a contrast such as cost versus control.
- Reflective delivery for a limit or counterargument.

No shouting, sales pitch or repeated theatrical build-up. A skeptical reading should test the claim, not mock the people involved.

The clean script is the only spoken input. These directions are for the editor. Verify provider-specific controls before converting them into TTS syntax. Unsupported cues require shorter takes, alternate readings or editing, not invented tags that may be spoken aloud.

## Acceptance

Listen to an early take before full generation. Check naturalness, comprehension, numerical pronunciation and tonal restraint. After wording revisions regenerate cue anchors and claim/visual references. An estimated duration does not replace timing the final video.
