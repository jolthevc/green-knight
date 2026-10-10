# From a new chat to a finished episode

## 1. Load context

Read the business instructions, selected channel rules/narration.json, NARRATION_STANDARD.md, EDITORIAL_REVIEW.md, LANE_ROUTING.md and full registry. Fetch the current main branch, not a stale summary. State the lane and task briefly. The user can ask for ideas, choose an existing idea, resume research, revise a script or prepare a handoff.

## 2. Ideate and select

Use IDEATION.md and LANE_ROUTING.md. Search for exact and near duplicates across all six lanes. A new title for the same explanation is a duplicate. A genuinely new mechanism, audience question or updated fact pattern can justify a revisit; explicitly reference the earlier ID and explain the difference.

Persist proposed ideas with stable IDs. The user chooses unless selection is delegated. On selection read the chosen channel.json, allocate the next ID using its story_prefix, copy templates/story/ to channels/<slug>/stories/<story-id>-short-slug/, set metadata.channel and the actual identifiers, fill metadata.json, and update the registry to selected. Pretty Penny uses PP-V####; Money Moves uses MM-V####; Fallen Angels uses FA-V####; Changing Hands uses DH-V####; Fool’s Gold uses FG-V####; Silver Spoon uses SS-V####. No stock script or completed pilot is seeded.

## 3. Research deeply

Start with the central question and an unproven hypothesis. Search primary documents, filings, official data, relevant research and strong reporting. Open sources and inspect the actual supporting passage; a search snippet is a lead, not evidence.

Build research.md, evidence.json and sources-and-claims.md. evidence.json owns source/claim/scene IDs and access status; the Markdown is its readable review. For every consequential claim record source ID, URL, publisher, publication and access dates, period/geography, supporting section/page, reliability, caveats and whether it is verified, inferred or illustrative. Trace script claims to exact paragraph anchors. Quotes stay short and accurate.

Check the strongest counterargument, competing explanations, historical changes and incentives on each side. Reconstruct the money mechanism: who pays whom, why, cost drivers, margins, timing, risk and where value accumulates. Build a unit-economics table when the question needs one. For Money Moves, additionally document the constraint, available alternatives, information known then, decision/execution timeline and competing causes of the outcome. For Fallen Angels, define what failed and build the failure timeline, warning/response sequence, fragility-versus-trigger analysis and competing explanations. For Changing Hands, build the position/ownership map, funding and obligations, event timeline and precise outcome measures. For Fool’s Gold, build the appearance/reality map, verification-gap analysis, exposure timeline and claim-by-claim evidence status. For Silver Spoon, build the relevant family/ownership map and transfer timeline, distinguish control from economic ownership, and document valuation dates/methods and private-information limits. Do not use a company's total net income as a product margin.

Depth ends when the central mechanism and necessary claims are supported, credible counterevidence has been examined, and additional searching is unlikely to change the view. There is no mandatory source count. If a crucial claim is unresolved, research further, reframe honestly or mark blocked. Update to researched only once the research and synthesis are defensible.

## 4. Develop the view and story

Write synthesis-and-outline.md before scripting. Include one-sentence thesis, viewer takeaway, causal chain, evidence against the thesis, limits, stakes, and why the answer differs from the obvious explanation.

Create the internal beat outline and two or three hook alternatives. Choose the best supported hook. Record what each open question promises and where it is answered. Find a concrete everyday entry, one understandable economic or strategic mechanism, a complication and a satisfying payoff. The owner does not need to approve each intermediate document.

## 5. Write the whole script

Produce the full spoken draft in one pass using the channel script standard. Do not stop after the hook or deliver an outline as a script. Inspect it for speech, then revise for factual accuracy, comprehensibility, momentum, repetition and payoff. Script length follows the timed delivery, not an arbitrary word quota.

In all six channels, `script.txt` begins with exactly `TITLE: <metadata.title>` on its first line, followed by a blank line and then narration. This is the **one permitted non-spoken line**. Narration lives only in the body of `script.txt`; strip the title header before recording, TTS, word counts or estimating runtime. After the wording stabilizes, number only the body's blank-line-separated paragraphs P001, P002, etc. Store cue anchors in delivery-cues.json and paragraph references in evidence.json and sources-and-claims.md. If the title, wording or formatting changes, increment script_version and regenerate affected references. Record SHA-256 of the **full exact script.txt bytes including title** in metadata, cues and evidence.json; opening anchors alone do not detect all revisions.

## Optional standalone script review and revision

After a complete draft exists, an independent fresh chat can review it using SCRIPT_REVIEW.md. REVIEW mode produces a paragraph-anchored critique without modifying canonical script.txt or stage. REVIEW_AND_REVISE mode repairs structural problems before sentence-level polish, re-reviews the new full script, and synchronizes version/hash/evidence/cues/metadata. This is an audio-first editorial diagnosis, not a predictive algorithm score, actual narration listening, or another routine owner approval gate.

## 6. Add delivery and production directions

Use VOICE.md and NARRATION_STANDARD.md for sparse instructions: pace, emphasis, pauses and intent. Provide a human-readable guide plus a machine-readable sidecar. Do not assume that an AI voice can follow emotional commands or SSML. The editor verifies the chosen provider's supported controls, auditions a short passage and records the selected provider/model/settings in versioned channel narration.json with a per-episode snapshot. Reuse approved profiles; complete voice-production.md with actual takes and listening during production. Unsupported cues are implemented through shorter takes, timing and editing.

Follow EDITOR_HANDOFF_STANDARD.md. Prepare narration-guide.md from the exact cues and pronunciation record, plus research-for-editor.md from the evidence map. The editor owns visual treatment. Do not prescribe shots or send internal visual/packaging proposals. Maintain paragraph/content coverage without visual execution instructions; visual-plan.md records that treatment awaits the editor. Review factual integrity of the actual delivered imagery later.

Complete packaging.md, handoff.md and qa.md. Give an estimated runtime with assumptions; never present it as measured audio. Mark scripted when the entire editorial package is saved and metadata.editorial records a passed internal review of the current script hash with no blocking issues. Production ready additionally requires the owner's voice/style selection and closed blocking editorial issues.

## 7. Produce and check

The editor generates narration, creates visuals, edits, mixes and delivers a reviewable cut. Check the rendered runtime is 480–600 seconds including closing and silent holds. Listen to the entire assembled narration at normal speed, compare beginning/middle/end against the channel reference, and check pronunciations, omissions/repeats, retake joins and cue artifacts. Inspect the final mix on headphones and a phone speaker, plus audio/visual sync, captions, readability and licensed assets. Record exact cut/audio URLs and script hash in metadata.production_review.

If too long, remove redundancy or simplify structure. If too short, add meaningful evidence/examples or choose a stronger bounded angle. If the concept cannot support 8–10 minutes, reframe or stop it; a shorter cut is not compliant. Do not rush the voice or add filler to manufacture duration. Preserve script integrity; recheck changed claims.

Deliverables: final review cut, clean narration audio and completed voice-production.md, caption file if commissioned, thumbnail, metadata and agreed editable project/source assets. The actual editor quote controls what is commissioned. No unagreed production budget is locked.

## 8. Save and learn

Each material stage saves the story files, registry status and dated history event together. Keep rejections with reasons, blocked ideas with dependencies, and published videos with verified URL/date. Preserve abandoned titles as aliases.

At roughly 48 hours, 7 days and 28 days after publication, record available impressions, CTR by traffic source, 30-second retention, average view duration/percentage viewed, significant dips/spikes and end-screen clicks. These are review windows, not automated jobs. Record missing data as unavailable.

Use the first several comparable episodes to establish channel baselines. Do not chase a universal CTR/retention target or treat a small sample as proof. Write one testable change per follow-up episode and retain the explanation in performance.md. Promote only supported repeated lessons into channel rules.

## Engagement throughout the workflow

Read ENGAGEMENT_STANDARD.md at context loading. Add the broad-audience entry and changed-understanding promise to candidate cards. During outlining, map each beat's viewer belief before/after, concrete reveal and reason to continue; choose the honest hook and locate the first useful payoff. During internal review, apply the newcomer and informed-skeptic lenses and repair the weakest middle stretch. During production, preserve breathing room and intelligible visual/audio handoffs. Record actual pilot feedback and later scene-level analytics separately from editorial predictions.
