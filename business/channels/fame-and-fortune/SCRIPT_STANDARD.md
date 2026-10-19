# Fame & Fortune: long-form script standard

## Runtime
- Minimum finished length: **10 minutes / 600 seconds**.
- Preferred finished length: **15 minutes / 900 seconds**.
- Maximum finished length: **20 minutes / 1,200 seconds**.
- These targets are channel-specific and override the shared 8 to 10 minute defaults, including in automated duration checks. Actual voice and rendered film duration must be measured. Provisional estimate = narrated word count / observed or assumed words per minute + deliberate pauses + silent image holds.
- For 15 minutes, a practical **starting** estimate is roughly 1,900 to 2,250 spoken words at 140 to 155 WPM with appropriate holds. Calibrate to an actual voice sample, not word count alone.

## Script must tell an addictive story
Treat as a dramatic factual documentary, not a Wikipedia summary. **The premise should be juicy and provocative, the evidence sober and defensible.** Prioritize an immediate dramatic event, revealed incentives, opposing constraints, documented power shifts, and a consequential surprise. No unsupported scandal, invented private thoughts, fabricated quotes or unsupported personal net worth.

## Eight practical segments (flexible timing, never filler)
See SCRIPT_SEGMENT_TEMPLATE.md for the default 15-minute storyboard.
A. COLD OPEN / HOOK (0:00-0:35): star, tension and impossible-looking contrast.
B. PROMISE / SETUP (0:35-1:30): immediate partial truth and larger question.
C. ACT I: THE IMAGE VERSUS THE BUSINESS (1:30-3:20).
D. ACT II: THE BET / DEAL / CONTRACT (3:20-6:00).
E. ACT III: FOLLOW THE MONEY (6:00-9:00).
F. ACT IV: THE TWIST / COST / STRUGGLE (9:00-12:00).
G. ACT V: WHAT ACTUALLY HAPPENED (12:00-14:15).
H. CLOSER / FINAL REVEAL (14:15-15:00).
Adjust duration to the story; segment names describe narrative jobs, not mandatory on-screen chapter cards.

## Canonical script file
For compatibility with Green Knight validation and sound production: `script.txt` begins EXACTLY `TITLE: <metadata.title>`, then one blank line, followed by the full word-for-word spoken narration with ordinary blank-line paragraph breaks. No spoken headings, timestamps, editor directions, square-bracket cues, source footnotes, sound directions or TTS markup. The TITLE header is non-spoken.

Number narration paragraphs P001 onward in the *non-spoken* cue/evidence map, not in the canonical script. Compute exact SHA256 over the entire file. Script title change or changed voiceover wording requires version bump, evidence and sidecar resync and packet re-review.

## Mandatory segmented drafting companion (internal)
Prepare `segment-map.md` with segment ID, title, approximate timeline, first/last P IDs and exact opening/closing anchor phrases, question, dramatic objective, answer/reveal, next-question transition, narrator tone, music/hold cue and visual objective. A separate `segmented-readthrough.md` may display the **unchanged** words beneath explicitly NOT-SPOKEN segment headings for convenient approval. Neither file enters `editor-packet/`.

## Three-file final editor-facing packet
Only after evidence, voice audition, owner script approval and director integration QA:
1. `01_SCRIPT.txt` is byte-identical to canonical `script.txt`. TITLE non-spoken; all following text spoken.
2. `02_NARRATION_DIRECTOR.md` reproduces the COMPLETE unchanged narration body and marks NON-SPOKEN segments A-H with approximate timing, P anchors, dramatic intent, pronunciation, emphases, pauses, energy shifts and retake guidance. Directives are clearly separate from SPOKEN COPY. If segmenting for ElevenLabs or another engine, paste ONLY the spoken words.
3. `03_VISUAL_DIRECTOR.md` gives ONE chosen title, one thumbnail, first frame, first 45-second sequence, then matching A-H scene boundaries, exact P ranges, concrete pictures and transformations, evidence and rights status, limited screen text, music resets and closing callback.

Do not introduce a fourth outgoing document. Every three-file packet must be read cold as an editor and pass the main network's EDITOR_HANDOFF_STANDARD and DIRECTOR_PACKET_REVIEW.

## Evidence and reputational safeguards
For every meaningful dollar figure distinguish valuation, stake value, enterprise sale price, realized gross proceeds, net personal proceeds, royalties, revenue, profit and cash. Verify dates, partners, percentages, legal documents and whether a claim is alleged/disputed/proven. Identify when press estimates differ. No unsupported crime, betrayal, fraud or personal relationship allegations. Avoid reproducing copyrighted song, interview, social or broadcast footage unless rights justify use.
