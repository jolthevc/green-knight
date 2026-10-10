# Instructions for AI working in business/

## Read before doing work

Read README.md, WORKFLOW.md, IDEATION.md, YOUTUBE_GUIDANCE.md, ideas/README.md and ideas/registry.json. For the selected channel also read channels/<slug>/{README,CHANNEL,STYLE,VOICE,SCRIPT_STANDARD}.md and channel.json. Read the configured idea/story prefixes; Pretty Penny uses PP, Money Moves uses MM, Fallen Angels uses FA, Changing Hands uses DH, Fool’s Gold uses FG, Silver Spoon uses SS. Also read NARRATION_STANDARD.md, EDITORIAL_REVIEW.md and LANE_ROUTING.md, plus the selected channel's narration.json. Follow the story templates when creating an episode.

This workspace implements the owner's manual ChatGPT process. Its local GitHub ledger and story artifacts are canonical here, even though the older portfolio system stores working artifacts elsewhere. Never imply that Sheets, Drive, n8n or YouTube were updated unless actually verified.

## Execute

- New chats cannot rely on memory. Fetch actual current repository files and record the branch/commit read.
- Read the entire global ledger, including rejected, archived, scripted and published ideas, before ideation. Check both topic and mechanism, not just title similarity.
- Present exactly the number of ideas requested in the documented format. Persist proposals if repository writing is available. Do not select a topic for the user unless delegated.
- Once a topic is selected, reserve its idea and story IDs, research deeply, develop a defensible thesis and internal outline, write the complete spoken draft in one go, review it, then add voice/visual directions.
- Do not require approvals for research, outline, each paragraph or routine revisions. Ask only when an unresolved decision materially changes the selected concept, budget or editorial premise.
- Browse original sources for research. Never fabricate facts, quotes, URLs, footage, analytics or source access. If browsing is unavailable, mark research blocked and explain what is missing.
- Money Moves research must establish the constraint, alternatives, information available at the time, execution, causal mechanism and competing explanations. Do not invent decisions, dialogue or hindsight certainty.
- Fallen Angels research must define the failure, reconstruct the original advantage and deterioration, distinguish fragility from trigger and symptoms from causes, and test competing explanations. Do not accept familiar downfall anecdotes without evidence.
- Changing Hands research must reconstruct positions/obligations or ownership, financing, the event timeline and the turning-point mechanism. Distinguish notional from capital, enterprise from equity value, and realized from paper results. No current investment recommendations.
- Fool’s Gold research must establish the legitimate baseline, apparent versus actual mechanism, credibility/verification gaps and exposure evidence. Distinguish allegations, admissions, established findings and unresolved issues; do not invent proof or victim anecdotes.
- Silver Spoon research must establish the relevant family relationships, wealth origins, ownership versus voting control versus leadership, transfer timeline and valuation basis. Do not invent private wealth, motives or family conflict.
- Financial mechanisms must distinguish revenue, cash flow, gross profit and net profit; dates, geography and units must travel with numbers. Label illustrative models.
- Write for the ear, keep engagement purposeful, deliver the title promise and finish within 8–10 minutes. Use actual audio duration for final approval.
- Every completed `script.txt` starts with exactly `TITLE: <metadata.title>` followed by one blank line, then spoken narration. The title header is **non-spoken**. No other headings, citations, directions or cue syntax go in this file. Count and number only narration paragraphs P001 onward, strip the title for recording/TTS, and compute SHA-256 over the entire `script.txt` including its header. No voice provider or unsupported control syntax is preselected.
- Preserve approved wording through production. Substantive changes return to the script and evidence check.
- Keep IDs stable, append history and update status only when deliverables exist. A finished script is not a published video.
- Before scripted, record an internal editorial review and populate evidence.json. Tie evidence/cues and reviews to the exact script version/hash. Do not fabricate completed listening, rendering or source-access checks.
- Reuse a versioned approved channel narrator/visual profile; material changes require new recorded versions. The initial owner selection is not a repeated per-episode approval gate.
- Run tools/validate.py before committing. Persist linked artifacts and ledger together. Re-read the branch head before writing; never force an overwrite of someone else's update.
- If write access is missing, provide a concrete patch/artifacts and state that GitHub was not updated. Do not tell the user it was saved.
- Do not send messages to editors or publish videos unless instructed.
- End with the saved story/idea IDs, links, exact stage reached and any real unresolved gap. Avoid em dashes in prose.

## Standalone script review and revision

For a user-requested cold review, review-only audit, or review-plus-revision of a completed draft, read and follow SCRIPT_REVIEW.md. Its review-only mode must not alter the canonical script or stage; revision requires user authorization and a fresh script-version/hash consistency check. Save version-specific review reports under the story's reviews/ directory when repository writing is available. The script's body stays the single spoken source; its mandatory TITLE line is non-spoken, and reviewer observations remain internal. The scripted stage's existing internal editorial gate still applies; a separate review does not replace source checks or actual production listening.

## Completion means

Ideation: cards and deduplication recorded.
Scripted: research, source/claim map, synthesis, complete clean script, directions and editorial QA saved.
Production ready: owner-selected voice audition, final script, production handoff and no blocking editorial gaps.
Published: verified public URL and publication date recorded.

## Engagement is substantive

Read ENGAGEMENT_STANDARD.md before ideation, outlining, scripting or reviewing. Use a familiar entry, earned early value and discoveries that change understanding. Apply its newcomer and informed-skeptic lenses before marking scripted; record the results in synthesis-and-outline.md and qa.md. These are internal editorial judgments unless real participants were consulted. Never substitute suspense or visual activity for missing explanation.

## Editor owns visual treatment

Read EDITOR_HANDOFF_STANDARD.md. Create narration-guide.md and research-for-editor.md matching the exact script/cues/evidence. Send the clean package only, without visual descriptions, shot lists, prompts, palettes, fonts or storyboards. Keep internal content coverage separate; visual-plan.md records editor ownership and later actual proposals.
