# Narration for financial stakes

Confident, curious and precise, with controlled tension. The voice helps a general viewer follow the position or transaction. Sound conversational rather than like a trading tip, hype reel or auctioneer.

## Audition

Test 30–45 seconds containing a hook, a difficult name, an amount, an obligation and a turning point. Choose a voice that remains clear when the explanation becomes technical. The owner selects it; provider, voice/settings and supported controls go in the channel's narration.json and a versioned story metadata snapshot.

No narrator, provider or settings are selected yet.

## Timing

Plan initially at 150 spoken words per minute plus extra intentional pauses and silent holds. Roughly 1,200–1,400 words is a starting range. Actual delivery and the finished edit control the 480–600 second requirement.

Estimated seconds = word_count / assumed_or_observed_wpm × 60 + extra_pause_seconds + silent_hold_seconds.

Do not rush the hardest passage to fit duration. Count silence once, and do not add runtime for visuals that run beneath narration.

## Cue sidecar

Use delivery-cues.json. script.txt contains spoken words only, in blank-line-separated paragraphs P001, P002, etc. A cue identifies its paragraph with an exact opening anchor and matching script_version.

Supported editorial fields:
- pace: natural / slower / brisk.
- intent: curious / matter_of_fact / skeptical / amused / reflective.
- emphasis: exact phrases already in the paragraph.
- pause_after_seconds: extra silence beyond natural punctuation.
- pronunciation_notes for real names and terms.

Slow slightly when explaining who owes what. Emphasize the constraint or reversal, not every dollar amount. Use a short pause after the consequence of a price move. Let the final explanation settle without an automatic dramatic crescendo.

These fields guide the editor; they are not a provider API specification. Verify provider-specific syntax before converting. Unsupported cues require shorter takes, alternate readings or editing. Never paste sidecar instructions into an untested TTS input.

## Listening QA

Check names, currencies, amounts, abbreviations and the distinction between owned and owed. Confirm no directions or citations are spoken. Regenerate anchors and source/visual references when wording changes.

Audition approval does not approve an unseen full cut. Final runtime and audio intelligibility must be checked on the actual rendered video.

## Shared production mechanics

Follow [NARRATION_STANDARD.md](../../NARRATION_STANDARD.md) for audition, profile versioning, pronunciation, coherent takes, retakes and full listening. [narration.json](narration.json) is the canonical channel voice; metadata stores its per-episode snapshot. Reuse an unchanged approved profile without another selection step. A material change creates a new profile version.

Delivery cues now use schema_version 2 and the exact script hash as well as script_version/paragraph anchors. Optional inflection describes neutral, question or settled delivery. These shared technical rules govern abbreviated cue descriptions above.

## Channel-specific listening test

Can the listener say who owns what, who owes what and what changes at the turning point? Slow the obligation/position example. Avoid reading a sequence of huge numbers with identical dramatic emphasis.
