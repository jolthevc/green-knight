# Shared narration production standard

Channel VOICE.md sets personality. This file owns the shared process, profile fields and cue mechanics. Its technical rules take precedence over abbreviated descriptions in individual voice guides.

## 1. Approve a channel voice once, then preserve it

Each channel's narration.json is the canonical versioned narrator profile. channel.json stores the profile link and descriptive personality only, not a second set of provider/settings fields. Record synthetic/human kind, provider and model where applicable, voice ID or performer, locale/accent, settings, pronunciation entries, measured WPM and an approved reference recording.

Keep status unselected and version 0 until a real audition is selected. Approval requires a reference_audio_url, approved_by and approved_at. No invented default voice or guessed settings.

Copy the approved profile into each story's metadata.narration snapshot, with profile_id/profile_version. An unchanged approved channel profile can be reused without another approval request for every episode. A material narrator/model/accent/settings change needs a new profile version and audition; preserve old story snapshots. Before replacing a profile, archive it as narration-history/v####.json in the channel folder. Archive a replaced approved visual_profile as visual-history/v####.json too, so older completed episodes retain verifiable references.

Changing providers or models can change delivery even when the advertised voice is the same. Keep a short reference clip for side-by-side comparison and record per-episode retakes in voice-production.md.

## 2. Audition delivery, not just timbre

Compare a small set of voice candidates on the same passage within a channel. Include the opening, a number/name-heavy explanation, a real question, a counterpoint and a quiet payoff. A 30–45 second sample is a first screen.

Before batch purchase, listen to one full 8–10 minute pilot. A short attractive sample cannot establish long-form consistency, sustained pacing or the quality of joins. Check early, middle and closing passages against the reference.

Judge naturalness, comprehension, tonal fit, pronunciation and endurance. A different voice for each channel is optional; consistent identity within each channel is required. No universal provider settings or “most expressive” model is prescribed.

## 3. Make the text recordable

Read the complete draft for speech before adding cues. Mix short and medium sentences, use concrete referents, explain unfamiliar terms in context and avoid chains of names/numbers. Put the most important idea where it can receive natural stress.

Write intended spoken amounts and acronyms clearly. Keep the exact figure in the source map. Decide whether a term is pronounced as a word or letter by letter. Do not add random ellipses, capitals, filler sounds or misspellings throughout the canonical script to manufacture emotion.

Maintain pronunciation entries with term, intended_spoken_form, authoritative_source_url when available, notes and tested_with_profile_version. Verify important names through reliable pronunciation evidence; if uncertain, flag and test rather than invent phonetics. Caption and on-screen spellings retain the correct name.

Text inspection is not audio listening. Do not report a read-aloud or pronunciation test as completed unless audio was actually produced and inspected.

## 4. Produce an engine-specific reading input deliberately

script.txt is canonical spoken wording. delivery-cues.json is non-spoken intent. An optional tts-input.txt is a derived production file with only verified provider/model controls and documented pronunciation substitutions. Record its relation to the canonical script and inspect the output for spoken tags or altered meaning.

Check current provider documentation before implementing pause, emphasis or inflection syntax. ElevenLabs' current documentation distinguishes model-specific controls, and some models do not support SSML breaks. Do not transfer a tag recipe between engines/models blindly.

No provider is selected for these channels. [Official ElevenLabs guidance](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices), checked 2026-10-10, is a reference example: punctuation, text structure, pronunciation and supported controls matter. Test actual behavior with the chosen voice.

## 5. Generate coherent takes and fix locally

A script written in one go does not require audio generated in one request. Use a provider's supported long-form workflow or coherent paragraph/scene blocks. Respect its actual input limits. Avoid both sentence-by-sentence choppiness and oversized requests that prevent economical retakes.

Keep the same voice/model/settings across takes. Where supported, use surrounding context to preserve continuity. Record paragraph range, take number, settings, selected audio URL and reason for any retake. Regenerate the smallest coherent block that fixes the problem; listen to the join and neighboring lines.

Do not patch in another voice to fix one pronunciation. Regeneration can vary, so select and inspect the actual take. Do not strip all breaths, swallow consonants at edits or change delivery speed enough to sound unnatural.

## 6. Cue mechanics and script identity

Use schema_version 2 delivery-cues.json, with script_version and SHA-256 of the exact UTF-8 script.txt bytes. Paragraphs are split by blank lines and identified P001, P002, etc.

A cue has paragraph_id, exact opening anchor, pace, intent, emphasis, pause_after_seconds and pronunciation_notes. Optional inflection is neutral / question / settled. These are editorial fields, not provider API parameters.

Use few purposeful cues. A question need not be raised artificially; emphasis is not shouting. “Slower” is an intent, not a measurable WPM adjustment. A paragraph opening can stay the same while the rest changes, so anchors alone are insufficient; the script hash detects that revision.

Use tools/episode_check.py to report the hash/count/timing. Enter the hash in metadata, delivery cues and evidence.json after versioning the final script. Do not overwrite mismatches merely to obtain a pass: first regenerate affected directions, claims and scenes.

## 7. Estimate, then measure

The 150 WPM default is only an assumption until calibrated. Use the exact voice on representative material to estimate delivery. Text normalization and number/acronym expansion can make token-based word counts imperfect.

Estimated seconds = approximate_word_count / assumed_or_observed_wpm × 60 + extra_pause_seconds + silent_hold_seconds.

The WPM sample includes ordinary punctuation pauses; add only extra planned silence, once. Pace variation is not modeled precisely by this estimate. Final audio and edited-video duration outrank the estimate. The finished video must be 480–600 seconds.

If short, deepen the evidence/example or choose a more substantial angle. If the selected concept cannot support the runtime, reframe or stop it; do not declare a shorter cut compliant. If long, remove redundancy before rushing delivery.

## 8. Full listening and final mix

Listen to the entire assembled narration at normal playback speed, then check the finished mix on headphones and a phone speaker. Compare beginning/middle/end to the reference for accent, timbre, pace and volume drift.

Check omissions, repeated lines, added words, cues spoken aloud, pronunciation, numerical meaning, clipping, abrupt joins and unintended noises. Automatic transcription can help locate discrepancies but does not prove correctness.

Keep music below clearly intelligible speech, especially beneath evidence and calculations. Avoid pumping levels and mask-free claims without listening. Supply a clean voice track and agreed master/export formats; do not pretend upsampling adds recorded detail.

Record actual audio/video URLs, duration, script hash, reviewer/date and corrections in metadata and voice-production.md. Final approval is tied to the exact cut and script, not to an earlier audition.
