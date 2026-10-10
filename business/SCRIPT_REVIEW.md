# Green Knight Script Review and Revision Protocol

Version 1.0. Applies to all six business channels. This is the canonical instruction for a standalone review or review-plus-revision of an existing script. Read it together with business/AGENTS.md, EDITORIAL_REVIEW.md, ENGAGEMENT_STANDARD.md, NARRATION_STANDARD.md, YOUTUBE_GUIDANCE.md, EDITOR_HANDOFF_STANDARD.md, the selected channel guides and the story's evidence/synthesis/packaging. It adds an independent editorial pass; it does not replace source verification or production listening.

## Mission

Judge the episode as an 8-10 minute spoken YouTube story for a curious adult with no specialist business training. Our aspiration is "Harvard MBA + Netflix": high-value, original, evidenced insight delivered as an entertaining, coherent narrative rather than a lecture. The viewer should understand the title's promise, care about the question, discover something genuinely new, and leave with a satisfying answer.

The test is not "is the writing impressive?" It is "would a real first-time viewer understand, enjoy, continue and recommend this story?" We cannot predict algorithmic success, exact retention or click-through from a text script. Make specific editorial judgments and identify testable hypotheses, never invented audience data.

## Entry point and operating modes

A user can say:
- "Review DH-V0001 against business/SCRIPT_REVIEW.md. Diagnose only."
- "Review and revise DH-V0001 against business/SCRIPT_REVIEW.md. Save the audit, revised script and linked changes."
- "Review this script using business/SCRIPT_REVIEW.md." An uploaded/pasted script is allowed; identify missing research and packaging explicitly.

REVIEW (default): Inspect and save a structured critique. Do not alter canonical script.txt or stage/status. A review is independently useful even when revisions are not requested.
REVISE: Apply an existing review to the current script, first checking that the review's script version/hash still matches. Re-review after revision.
REVIEW_AND_REVISE: Perform a cold review, revise only justified changes, then run a new independent-style final check and save both reports. This is the default if the owner requests both.

The reviewer should ideally work in a fresh context from the drafter, with no obligation to defend earlier choices. When the same model does both, explicitly state that true reviewer independence has not been established. Never claim external test viewers or actual playback without having them.

## Inputs and order

1. Read the actual complete script first, as a cold audience member. Note its opening promise, first point of confusion, middle drag, apparent ending and overall experience before consulting prior QA or proposed solutions.
2. Obtain the selected channel and its story engine, current script version and exact UTF-8 SHA-256, current working title/thumbnail promise, target audience, supporting research/evidence, and synthesis. Read the exact current GitHub files, not a memory of a prior version.
3. If packaging is unavailable, review the hook against the documented viewer promise and label packaging alignment "unverified." If research is unavailable, flag claims requiring verification instead of pretending to fact-check.
4. Estimate narration time transparently from word count, a stated plausible pace and any supplied holds/pauses. Do not report estimated time as recorded time or manufacture timing by speeding up the voice.
5. Review without relying on editor-generated visuals to rescue unclear narration. Creative visual treatment belongs to the editor.

## Diagnostic passes

### A. The decision to click and stay

- Can a stranger grasp the subject and stakes from the title/thumbnail promise? Is the proposed title truthful, legible and broad-interest rather than insider shorthand?
- In the first roughly 10, 30 and 60 seconds, respectively, what does the viewer know, want to know and already receive? Use timing estimates, not fictional stopwatch measurements.
- Does the opening start with the subject, consequential contradiction or relatable stake rather than greetings, throat-clearing, corporate history or an abstract thesis?
- Does the opening honor the package, establish the main question, and give an earned useful first payoff? Is the second question better because of that payoff?
- Compare two or three materially different hook approaches only when a hook actually needs improvement. Do not replace a good hook for variety's sake. No manufactured mystery or false promise.

### B. The story engine and causal spine

Write a one-sentence answer to each: Who or what is this about? What is wanted or puzzling? What changes? What mechanism causes the change? Why must the next beat follow? What is the final answer?

Make an internal beat map. For each beat, note the audience's belief before, meaningful new information/decision/consequence, belief after, remaining question and rough position. Examine the transitions between beats, not just isolated paragraphs. Flag facts merely appended by chronology, causal leaps, repeated setup, unnecessary detours, stacked background and sections that could be deleted without losing understanding or stakes.

A viewer should repeatedly get real value before being asked to stay for another answer. Inspect the opening, every middle stretch, the biggest reveal and ending. Use roughly 30-60 second intervals as a diagnostic for progress, not as a rigid reveal schedule or justification for rushed narration. Allow a difficult explanation time to land.

### C. First-listen, audio-only comprehension

Assume an intelligent person is listening while walking, not reading, pausing or taking notes. Identify every place a listener might reasonably ask: "Wait, who?", "Why does that follow?", "Which money?", "What year?", "Who owes whom?", or "How does that work?"

- Introduce the role, motivation and relationship before unnecessary names. Reorient briefly when a person or entity returns after a gap.
- Define unfamiliar concepts through familiar consequences before naming the technical term. Use jargon only when it buys explanatory precision.
- Audit pronouns, shifting referents, acronyms, abbreviations and timeline jumps. Avoid sentences with multiple subordinate clauses and dependent numbers.
- Say one numerical relationship at a time; put it beside an intuitive comparison. Preserve units, dates, denominators and distinctions such as revenue versus profit, paper versus realized, or ownership versus control.
- Test whether an explanation survives without a chart, screen annotation, source screenshot or facial reaction. If not, repair the words first.
- Keep repetition only when it performs a new job: reorientation, contrast or an earned callback. Remove repeated framing and redundant summaries.

Do not flatten the language to an artificial grade level, overexplain every basic word, or turn the script into an instructional list. Aim for adult clarity with real depth.

### D. Spoken performance and voice

Read problem sentences aloud if speech playback is available; otherwise explicitly perform a text-based speechability pass, not a claimed listening test. Inspect mouth-feel, sentence length, pauses, cadence, transitions, repeated grammatical patterns, quote handling, pronunciations and the rhythm of numerical passages.

The narrator should sound like an informed, warm, confident guide telling a great story, not a banker reading a memo, a hype announcer, a professor, or an AI cycling stock transitions. Prefer concrete verbs, specificity and varied but natural sentence shapes. Ensure clauses can be spoken in understandable breaths. Tone and emotion should be earned by the facts. Do not try to repair overwrought writing solely through delivery cues or sound design.

### E. Discovery, humanity and emotional investment

- What is the surprising, defensible insight that makes this more than an ordinary summary or Wikipedia timeline?
- Where does the viewer's mental model materially change? Can they repeat the core mechanism and final insight in ordinary language?
- Are stakes legible through a human goal, real cost, trade-off, conflict, risk, ambition, fairness or relatable behavior, rather than "billions" alone?
- Is complexity made interesting through a concrete illustration, counterintuitive relationship, consequential choice or tested counterexplanation?
- Check for sustained engagement without forced cliffhangers, fake villains, constant "but here's the crazy part" pivots, excessive questions or unsupported psychological motives.
- Preserve individuality across episodes. One house style must not produce six channels of interchangeable exposition.

### F. Truth, insight and fair interpretation

Check consequential historical, causal, quantitative, legal and financial claims against opened source passages and evidence.json; a search snippet or source title is not proof. Distinguish facts, inference, illustration, disputed allegations and open questions. Challenge the central thesis and strongest competing explanation.

Flag unsupported quotations, invented events/private motives, changed dates, misleading causal sequence, omitted contrary facts and figures missing critical units or context. Strengthen nuance where it changes the takeaway, without filling the voiceover with endless caveats. An unsupported claim is never made acceptable because it is more clickable.

### G. Earned payoff, ending and viewer satisfaction

Does the ending answer the actual question promised at the beginning? Is the insight more specific than "business is complicated"? Does the opening subject mean something richer after the story? Is the final emotional or intellectual beat satisfying before any CTA? Does the ending avoid rehashing every section, introducing unsupported moral lessons or teasing a payoff it never supplies?

### H. Channel-specific identity

Pretty Penny: make the hidden money machine and incentives comprehensible through familiar behavior.
Money Moves: establish the real constraint, alternatives, choice and competing causal interpretations.
Fallen Angels: separate original advantage, fragility, warnings, trigger and outcome.
Changing Hands: clarify who owned/owed what, financing, leverage, timing, deal mechanics and actual outcome.
Fool's Gold: distinguish appearance from reality, credibility mechanism, verification failure, evidence and consequences.
Silver Spoon: distinguish family relationships, financial ownership, voting/control rights, transfer and valuation caveats.

Do not force one channel's preferred narrative shape onto another. If the topic belongs in a different lane or lacks 8-10 minutes of defensible story, say so rather than padding.

### I. Production feasibility and originality

Check that the narration alone carries essential meaning, that difficult numbers and names can be spoken naturally, and that needed context has supporting references for the editor. Do not create shot lists, visual prompts, palettes, graphics directions or fictional archival evidence. The editor owns execution.

Ask what distinguishes this piece from generic mass-produced AI explainers. Specific primary evidence, a coherent question, fresh synthesis and a distinctive finding matter more than theatrical prose or artificial retention tricks. Respect copyright, attribution, allegations and platform originality/disclosure requirements.

## Review decision and severity

Report each dimension as STRONG, NEEDS WORK or BLOCKING, with a short cited observation from the script; do not produce a deceptive universal quality percentage or forecast watch-time/virality.

Dimensions: (1) click/packaging promise; (2) opening and first payoff; (3) causal narrative/continuity; (4) middle momentum and discovery; (5) first-listen accessibility; (6) spoken voice; (7) meaningful insight; (8) emotional stakes; (9) factual integrity; (10) payoff and production readiness.

Issue severities:
- P0 BLOCKER: material factual or legal misrepresentation; unsupported central thesis; fundamental incoherence; failure to deliver title promise; unusable runtime/premise. Re-research or reframe, not a quick polish.
- P1 MUST FIX: likely first-listen confusion, weak opening, sluggish middle, broken transition, key missing context, unearned payoff, or widespread unspoken/unwieldy prose.
- P2 POLISH: localized cadence, trim, reorientation or clearer word choice that improves a fundamentally viable story.
- KEEP: unusually good moments or structural choices to protect in revision.

Prioritize at most the five biggest high-leverage interventions in the executive diagnosis. Cite exact paragraph IDs or short unique opening words when IDs are unavailable. Distinguish evidence defects from editorial preferences. For each intervention give problem, listener consequence, suggested structural or sentence-level change, evidence impact and importance. A review may recommend "do not revise" when no material improvement is justified.

Verdict:
- BLOCKED_RESEARCH: evidence or thesis/premise gaps prevent trustworthy rewriting.
- REVISIONS_REQUIRED: one or more P0/P1 issues remain.
- EDITORIALLY_READY: no P0/P1, central promise delivered, audio-only comprehension credible, facts checked where source access is available; actual audio/cut and channel pilot approvals still may be outstanding.

## Required review output

Save a version-specific Markdown report under the story's reviews/ directory when GitHub access is available, e.g. reviews/script-v2-review-2026-10-10.md. For uploaded scripts, provide the complete report without claiming it was saved.

The report contains:
1. Story ID/channel/title, review date, mode, script_version and exact script_sha256 (or "unavailable"), source access status, packaging supplied, and whether any actual audio was heard.
2. Three-sentence cold-viewer experience, specific strongest moment, precise weakest stretch and overall verdict.
3. Ten-dimension diagnostic with concrete script evidence and classifications.
4. Opening audit (approximately 0-10, 10-30, 30-60 seconds) and package/promise match.
5. Internal beat-by-beat map showing new understanding, transitions, question/payoff and rough timing; explicitly identify the longest weak stretch.
6. P0/P1/P2 issue register with paragraph anchors, listening consequence and actionable proposed fix; top five prioritized first, plus KEEP elements.
7. Accessibility/audio-only test, causal-integrity and source-risk assessment, and transparent word count/runtime assumptions.
8. Minimum change plan: structural moves before line edits; what must stay unchanged; unresolved source questions and review limitations.

Do not put review labels or delivery instructions into script.txt. Review reports are internal, not default editor inputs.

## Revision protocol

Only rewrite when authorized by the user or when they explicitly request REVIEW_AND_REVISE. The review and its script hash must match the current source before applying changes.

1. Snapshot the original through Git history; make an explicit change plan and preserve KEEP elements. Fix P0 evidence/thesis issues before restructuring; never invent a missing fact.
2. Revise in passes: (a) promise, chronology, causality and beat order; (b) opening, first payoff, middle stretch and ending; (c) paragraph transitions, accessible examples and first-listen clarity; (d) spoken rhythm, precision and trims.
3. Prefer the least intrusive revision that meaningfully fixes the issue. Do not automatically rewrite every paragraph or make the script louder, more juvenile, more suspenseful or more generic. Keep the distinct channel voice and author's defensible discoveries.
4. If a sentence is cut or moved, re-evaluate how adjacent paragraphs connect. Preserve exact facts, numbers, quotation meaning, qualification and the relationship between evidence and interpretation. Trace consequential additions back to sources; reopen sources as needed.
5. Re-run the cold-review diagnostic on the *new full script*, including the opening, weakest middle, ending, key financial mechanism and audio-only comprehension. Do not self-certify because changes were made. Record remaining P0/P1, or state why no further edits are justified.
6. Re-estimate spoken duration using explicit pace and pauses. The final target is 480-600 seconds including closing; only an actual rendered cut can establish actual runtime. Do not pad or speed-read.
7. Increment metadata.script_version for any change to script.txt bytes, recompute its exact SHA-256 and rebuild paragraph IDs/anchors. Update evidence.json, sources-and-claims.md, delivery-cues.json, narration-guide.md, research-for-editor.md, packaging.md, handoff.md, qa.md and relevant metadata/revision history where affected. Clear obsolete editorial approval and production review until the new version is actually reviewed. Keep registry.status and metadata.status consistent; do not mark production or publication complete.
8. Run the repository validator and correct any genuine consistency issues. Use current branch state and safe GitHub writes; do not overwrite concurrent edits. Save the revised script, version-specific before/after change report and final re-review together insofar as tools support it.
9. End with exact saved paths, script version/hash, verdict, improvements made, open blockers, and whether audio was actually auditioned. If GitHub cannot be written, supply patch/revision artifacts and state they were not saved.

The revision report should compare the important changes by issue and location, not dump every altered line. Include a brief "did the revision make anything worse?" examination.

## Stop rule

Do not chase an inflated score through endless self-rewrites. Stop when the central promise is satisfied, no P0/P1 defects remain, the audio-only story is coherent, the insight is original and supported, the pacing is credible and further changes are merely subjective. Reopen for new facts, real pilot listening or actual viewer data.

## Pilot learning

Before publication, real listeners can be asked: "What was the video about? Where did you get lost or feel bored? What was the most surprising thing? Why did you keep watching or stop?" Report actual participant feedback separately from internal simulated judgments.

After publishing, connect YouTube audience-retention dips, top moments, intro retention and comments to specific script passages, alongside traffic source, package and audience context. A replay spike may reflect confusion. Compare similar-length episodes and build channel baselines rather than impose universal CTR or retention thresholds. Turn repeated findings into documented changes, with dated evidence, not mythology about the algorithm.

Official reference: https://support.google.com/youtube/answer/9314415?hl=en
Official title/thumbnail reference: https://support.google.com/youtube/answer/12340300?hl=en

## Short instruction for a fresh reviewer chat

"Read the current jolthevc/green-knight repository, business/AGENTS.md and business/SCRIPT_REVIEW.md, then the selected channel rules and complete story package for [STORY_ID or path]. Perform a genuinely critical first-listen YouTube story review. Identify the strongest and weakest passages, diagnose hook/promise, causal flow, middle momentum, accessibility, speechability, originality, factual support and final payoff. Use exact paragraph anchors and specific fixes, not vague praise or predictive retention numbers. MODE=[REVIEW or REVIEW_AND_REVISE]. When revision is authorized, update the complete canonical package, version/hash/anchors and review records, validate, and give exact saved links. Do not prescribe visual treatment or claim real listening/audience tests unless they happened."