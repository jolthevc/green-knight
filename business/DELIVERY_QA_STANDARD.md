# Green Knight — Finished Video Delivery QC (all business channels)

This is the **mandatory post-production acceptance protocol** when a user provides an editor's draft, revised cut, thumbnail, audio, SEO or subtitle files for a story. It is separate from the **pre-production** three-file editor instruction packet. Applies to all eight business channels and every editor; do not invent extra editor deliverables.

## Five expected deliverables per finished episode
1. **Final video:** 16:9 MP4, at least 1920x1080, with finished visuals, narration and mixed soundtrack.
2. **Thumbnail:** standalone 16:9 PNG/JPG (prefer 1280x720 or higher), readable at phone size.
3. **Clean narration audio:** the actual approved final voice in WAV or high-quality MP3, without music/SFX, synchronized in content with the video.
4. **SEO package:** a readable TXT/DOC or equivalent containing proposed YouTube title, description, relevant tags and **accurate clickable chapter timestamps derived from the finished cut**. This package is for review, not automatic publication. Chapter 00:00 and time alignment must be verified.
5. **Subtitles:** time-synchronized, accurately proofread .srt file in the narration's language. SRT is a selectable caption track; it is not a request to burn full subtitles into the picture.

Don't require editable project files, isolated music stems, production archive, full asset manifest or unrelated channel management. Genuine third-party rights concerns may still need clarification before approval; this is a compliance question, not a sixth default deliverable. On a first draft, review available items and mark missing ones PENDING rather than fabricating a complete delivery. Editor may deliver full five after final revisions as agreed.

## Canonical references and version lock
Find the named episode ID/channel in the current GitHub repository. Read and identify the **approved released** `editor-packet/01_SCRIPT.txt`, `02_NARRATION_DIRECTOR.md` and `03_VISUAL_DIRECTOR.md`; verify version/script hash against internal canonical script and QA. The three are source-of-truth for promised editorial output. Internal creative alternates and preliminary drafts do not supersede them. If missing or stale, report that comparison cannot be fully certified; never invent approval, files, viewing, reference times or voice identity. Note which supplied delivery version (v1/v2 etc.) was reviewed and its actual paths.

## QA gates, in this order
**0. Intake:** List each of five deliverables as PRESENT / PENDING / UNREADABLE. Record file access, duration/resolution/audio stream and versions when measurable. Distinguish draft review from full acceptance. Don't mark absent post-final documents as defects of a draft unless contract requires them now.

**1. Script fidelity and truth (blocking):** Compare narration with ALL approved spoken lines, in order. Note dropped/repeated/reworded sentences, numbers/units, mispronounced names, false or misleading illustrations/text, unauthorised additions. Prefer listening to actual audio; automated transcript alignment is a supplement and can mishear terms. Identify exact approved paragraph P IDs and final-cut times. Do not count the nonspoken TITLE header as narration.

**2. Narration performance:** Confirm approved channel voice and human-directed pacing; natural speech; emphasis, breaths, meaningful pauses, pronunciation, retake seams, audio clarity, consistent volume, music intelligibility. Compare section IDs/pause cues with `02`. Evaluate voice quality over sustained runtime, not just the opening. If audio could not be played or thoroughly heard, say this explicitly and issue UNVERIFIED rather than PASS.

**3. Directed picture/storytelling:** Compare film with selected title, thumbnail promise, first frame, approximate 0–5/5–15/15–30s visual beats, each S sequence, recurring environments, causal transformations/comparisons, evidence authenticity, exact labels, breaks, sound resets and ending callback from `03`. Classify essential intent met by a sensible editor-devised equivalent as COMPLIANT. Do NOT flag cosmetic deviations simply because the editor chose another technique. Inspect suspicious short defects at appropriate temporal resolution; sampled frames never prove the entire animation glitch-free. Flag malformed drawings, broken text, mismatched footage, dead stretches, misleading evidence, distracting repetition or unexplained framing shifts.

**4. Packaging/delivery:** Thumbnail composition/mobile legibility and honest alignment with title/opening; clean narration matches final cut; SRT timing, spelling, proper nouns, punctuation and synchronization; SEO title/description accuracy and clarity, chapter times actually matching meaningful final-cut divisions, tags reasonable/not spammy; exported MP4 has no corruption, incomplete tail, excessive black, abrupt audio, wrong aspect ratio or unintelligible mix. Check actual final timing rather than draft timecodes. Chapter labels should serve navigation; no requirement to print visible chapter intertitles in video.

**5. Audience experience:** Independently evaluate actual first 30–60 seconds, comprehension without prior research, story momentum and mid-film retention risk, repetition, emotional rhythm, whether viewer can follow economics, and ending payoff. Compliance alone does not prove a strong video. Distinguish judgment from measurable defects. Never invent audience retention, views, comments or external feedback.

## Report format and severity
Save a dated `delivery-qa/YYYY-MM-DD-vN.md` **inside the episode folder**, outside `editor-packet/`. Include episode ID; reviewer/date; received files and paths; approved script SHA and director packet version; whether full video and audio were ACTUALLY inspected; method (full listening, frame sampling, transcript alignment etc.); status of five outputs; gate-by-gate PASS / REVISE / BLOCKED / UNVERIFIED / NOT APPLICABLE; summarized strengths; a table of findings: `timecode | P/S anchor | severity | observation vs approved brief | exact requested fix | verification status`; final acceptance verdict; and whether to ask for rework. Record findings also concisely in story `qa.md`, without overwriting prior editorial audits or misrepresenting registry stage.

Severity:
- **BLOCKER:** materially false/missing spoken claims, wrong voice, broken/corrupt export, unusable video/audio or major factual errors. Must repair.
- **MAJOR:** meaningful visual sequence not executed, repeated pacing/clarity failure, defective thumbnail/chapters/SRT, significant production defect. Fix before final approval.
- **MINOR:** localized visible/heard glitch, typo or easily corrected issue. Consolidate where warranted.
- **SUGGESTION:** subjective improvement beyond agreed instructions. Optional; do not inflate revision rounds.

When incomplete/unreadable inputs prevent verification, report **PROVISIONAL / NOT FULLY VERIFIED**, not an invented pass. If final editor packet itself is ambiguous/incorrect, mark an **internal direction issue**, not an editor failure, and correct upstream guidance via an authorized revision path.

## Editor feedback and revisions
For v1: prepare ONE respectful, concrete, consolidated Fiverr revision message with timecode, required correction, priority and reference to P/S ID where useful. Praise good execution specifically; do not dump internal audit vocabulary on the editor. Separate must-fix from optional suggestions. Avoid new creative requirements not in the approved packet unless user explicitly requests a scope change. Favor affordable technique-equivalent fixes.

For v2/v3: compare against v1 issue log; mark each FIXED / PARTIAL / NOT FIXED / REGRESSED; review changed portions plus adjacent transitions and overall continuity. Confirm changes did not shift subtitle or chapter timestamps and did not introduce new errors. Still inspect entire final export sufficiently for end-to-end acceptance; don't claim complete listening if it didn't happen. Retain reports per revision; never silently overwrite.

Approval requires verified correct film, thumbnail and the five agreed deliverables, no open blocker or major finding, and truthful declaration of the inspection performed. **Do not upload, publish, accept on Fiverr, or claim successful delivery without user instruction.**

## Commands
- `Review the editor delivery for [EPISODE-ID]. Compare the attached video and other available files with the three approved GitHub editor-packet documents. Run full delivery QA, save a timecoded report to GitHub, and draft one prioritized Fiverr revision message. Be explicit about anything you couldn't verify.`
- `Re-review [EPISODE-ID] v2 against the previous delivery QA. Check each requested fix, regressions, the five deliverables and overall acceptance. Save the updated report and give a final approve/revise verdict.`

## Popcorn-good delivery QA is mandatory
In addition to mechanical compliance, evaluate **the actual entertainment** under POPCORN_STANDARD.md: first-minute desire to continue, actual middle dead stretches and repetitive illustrations, timing of surprising evidence/strategic revelations, breath and tonal variety, clarity for newcomers, and specific payoff for viewers who already know the story. Record separately `NEWCOMER experience`, `EXPERT insight payoff`, `MOST LIKELY DROP-OFF MOMENT`, `STORY-DRIVEN VISUAL/SOUND EXECUTION`, and `CREATIVE VERDICT` with observed timestamps wherever possible. This is a genuine editorial gate, not a checkbox awarded to video that followed instructions. If the approved script itself is structurally boring, label INTERNAL CREATIVE PROBLEM, not an editor violation. Never claim observed retention, complete watch-through or listener reaction without evidence; do not add unagreed scope changes to Fiverr fixes.
