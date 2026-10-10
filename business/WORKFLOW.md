# From a new chat to a finished episode

## 1. Load context

Read the business instructions, selected channel rules and full registry. Fetch the current main branch, not a stale summary. State the lane and task briefly. The user can ask for ideas, choose an existing idea, resume research, revise a script or prepare a handoff.

## 2. Ideate and select

Use IDEATION.md. Search for exact and near duplicates across all six lanes. A new title for the same explanation is a duplicate. A genuinely new mechanism, audience question or updated fact pattern can justify a revisit; explicitly reference the earlier ID and explain the difference.

Persist proposed ideas with stable IDs. The user chooses unless selection is delegated. On selection read the chosen channel.json, allocate the next ID using its story_prefix, copy templates/story/ to channels/<slug>/stories/<story-id>-short-slug/, set metadata.channel and the actual identifiers, fill metadata.json, and update the registry to selected. Pretty Penny uses PP-V####; Money Moves uses MM-V####. No stock script or completed pilot is seeded.

## 3. Research deeply

Start with the central question and an unproven hypothesis. Search primary documents, filings, official data, relevant research and strong reporting. Open sources and inspect the actual supporting passage; a search snippet is a lead, not evidence.

Build research.md and sources-and-claims.md. For every consequential claim record source ID, URL, publisher, publication and access dates, period/geography, supporting section/page, reliability, caveats and whether it is verified, inferred or illustrative. Trace script claims to exact paragraph anchors. Quotes stay short and accurate.

Check the strongest counterargument, competing explanations, historical changes and incentives on each side. Reconstruct the money mechanism: who pays whom, why, cost drivers, margins, timing, risk and where value accumulates. Build a unit-economics table when the question needs one. For Money Moves, additionally document the constraint, available alternatives, information known then, decision/execution timeline and competing causes of the outcome. Do not use a company's total net income as a product margin.

Depth ends when the central mechanism and necessary claims are supported, credible counterevidence has been examined, and additional searching is unlikely to change the view. There is no mandatory source count. If a crucial claim is unresolved, research further, reframe honestly or mark blocked. Update to researched only once the research and synthesis are defensible.

## 4. Develop the view and story

Write synthesis-and-outline.md before scripting. Include one-sentence thesis, viewer takeaway, causal chain, evidence against the thesis, limits, stakes, and why the answer differs from the obvious explanation.

Create the internal beat outline and two or three hook alternatives. Choose the best supported hook. Record what each open question promises and where it is answered. Find a concrete everyday entry, one understandable economic or strategic mechanism, a complication and a satisfying payoff. The owner does not need to approve each intermediate document.

## 5. Write the whole script

Produce the full spoken draft in one pass using the channel script standard. Do not stop after the hook or deliver an outline as a script. Read it aloud internally, then revise for factual accuracy, comprehensibility, momentum, repetition and payoff. Script length follows the timed delivery, not an arbitrary word quota.

Narration lives only in script.txt. After the wording stabilizes, number its blank-line-separated paragraphs P001, P002, etc. Store cue anchors in delivery-cues.json and paragraph references in visual-plan.md and sources-and-claims.md. If paragraphs change, regenerate these references and recheck them.

## 6. Add delivery and production directions

Use VOICE.md for sparse instructions: pace, emphasis, pauses and intent. Provide a human-readable guide plus a machine-readable sidecar. Do not assume that an AI voice can follow emotional commands or SSML. The editor verifies the chosen provider's supported controls, auditions a short passage and records the settings. Unsupported cues are implemented through shorter takes, timing and editing.

Plan purposeful visuals by paragraph, not just a stock-photo list. Every chart carries source/date/unit and every reconstruction is distinguishable from actual evidence. Keep the reusable visual vocabulary stable while scenes remain original.

Complete packaging.md, handoff.md and qa.md. Give an estimated runtime with assumptions; never present it as measured audio. Mark scripted when the entire editorial package is saved. Production ready additionally requires the owner's voice/style selection and closed blocking editorial issues.

## 7. Produce and check

The editor generates narration, creates visuals, edits, mixes and delivers a reviewable cut. Check the rendered runtime is 480–600 seconds including closing and silent holds. Spot-check pronunciations, numbers, cue artifacts, audio/visual sync, captions, readability, music levels and licensed assets.

If too long, remove redundancy or simplify structure. If too short, add meaningful evidence/examples or shorten the episode concept before padding. Do not rush the voice or add filler to manufacture duration. Preserve script integrity; recheck changed claims.

Deliverables: final review cut, clean narration audio, caption file if commissioned, thumbnail, metadata and agreed editable project/source assets. The actual editor quote controls what is commissioned. No unagreed production budget is locked.

## 8. Save and learn

Each material stage saves the story files, registry status and dated history event together. Keep rejections with reasons, blocked ideas with dependencies, and published videos with verified URL/date. Preserve abandoned titles as aliases.

At roughly 48 hours, 7 days and 28 days after publication, record available impressions, CTR by traffic source, 30-second retention, average view duration/percentage viewed, significant dips/spikes and end-screen clicks. These are review windows, not automated jobs. Record missing data as unavailable.

Use the first several comparable episodes to establish channel baselines. Do not chase a universal CTR/retention target or treat a small sample as proof. Write one testable change per follow-up episode and retain the explanation in performance.md. Promote only supported repeated lessons into channel rules.
