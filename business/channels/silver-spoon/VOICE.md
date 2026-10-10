# Narration for dynasties and inheritance

Warm, observant and precise, with conversational curiosity and occasional dry wit. Interested in what wealth and control do to incentives, without worshipping wealth or mocking the family.

## Audition

Test 30–45 seconds containing a hook, a difficult surname, a relationship, an ownership distinction and a turning point. Choose clarity over an affected aristocratic accent or gossip-show delivery.

The owner selects the narrator. Record provider, voice ID/settings, supported controls, pronunciations and observed WPM in the channel's narration.json and a versioned story metadata snapshot. No narrator/provider is selected yet.

## Runtime

Plan initially at 150 spoken words per minute plus intentional extra pauses and silent holds. Around 1,200–1,400 words is a starting range, not a quota.

Estimated seconds = word_count / assumed_or_observed_wpm × 60 + extra_pause_seconds + silent_hold_seconds.

Ordinary punctuation pauses are already reflected in pace. Count additional silence once; a map shown beneath narration does not add runtime. Actual finished video must last 480–600 seconds including the closing.

## Non-spoken sidecar

Use delivery-cues.json with script_version matching metadata. Clean script.txt contains spoken words only, separated into blank-line paragraphs P001, P002, etc.

Each cue has an exact opening anchor, pace (natural/slower/brisk), intent (curious/matter_of_fact/skeptical/amused/reflective), exact emphasis phrases, pause_after_seconds and pronunciation_notes where needed.

Use slower delivery when distinguishing a shareholding from voting control or navigating a family branch. Mild emphasis can clarify who inherited which right. A short pause after a surprising transfer helps the meaning register.

Skepticism tests an explanation, not a surname. Humor can illuminate an absurd incentive; it should not invent conflict or mock someone for a relationship.

Cues are editor directions, not TTS API fields. Verify provider-supported syntax before conversion. Unsupported instructions require alternate takes, segmentation or editing. Do not paste untested bracket tags or invented SSML into narration.

## Listening check

Check names, generational relationships, percentages, amounts and the distinction between ownership and leadership. Confirm no cues or citation IDs are spoken. Update anchors and source/visual references after wording changes.

An audition does not approve the unseen final cut. Measure the finished video and check intelligibility with music and diagrams.

## Shared production mechanics

Follow [NARRATION_STANDARD.md](../../NARRATION_STANDARD.md) for audition, profile versioning, pronunciation, coherent takes, retakes and full listening. [narration.json](narration.json) is the canonical channel voice; metadata stores its per-episode snapshot. Reuse an unchanged approved profile without another selection step. A material change creates a new profile version.

Delivery cues now use schema_version 2 and the exact script hash as well as script_version/paragraph anchors. Optional inflection describes neutral, question or settled delivery. These shared technical rules govern abbreviated cue descriptions above.

## Channel-specific listening test

Can the listener distinguish the relevant family branches, cash interests, votes and management roles? Reorient using a role when too many surnames accumulate. Avoid an affected aristocratic accent and gossip-show certainty.
