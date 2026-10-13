# Instructions for AI working in business/

## Read before doing work

Read POPCORN_STANDARD.md first for the primary creative objective and dual-viewer test, including in fresh chats and review/revise.

Read README.md, WORKFLOW.md, IDEATION.md, YOUTUBE_GUIDANCE.md, ideas/README.md and ideas/registry.json. For the selected channel also read channels/<slug>/{README,CHANNEL,STYLE,VOICE,SCRIPT_STANDARD}.md and channel.json. Read the configured idea/story prefixes; Pretty Penny uses PP, Money Moves uses MM, Fallen Angels uses FA, Changing Hands uses DH, Fool’s Gold uses FG, Silver Spoon uses SS; First Billion uses FB; On the Map uses OTM. Also read NARRATION_STANDARD.md, EDITORIAL_REVIEW.md and LANE_ROUTING.md, plus the selected channel's narration.json. Follow the story templates when creating an episode.

This workspace implements the owner's manual ChatGPT process. Its local GitHub ledger and story artifacts are canonical here, even though the older portfolio system stores working artifacts elsewhere. Never imply that Sheets, Drive, n8n or YouTube were updated unless actually verified.

## Editor onboarding and relationship coordination
When the owner asks to find, contact, qualify, onboard or negotiate with an editor, or prepare Fiverr communications, read [EDITOR_ONBOARDING_PLAYBOOK.md](EDITOR_ONBOARDING_PLAYBOOK.md) and its linked editor templates. Treat it as the source of truth for relationship steps, terms needing confirmation, batch preparation, exactly three outgoing episode instructions, exactly five final deliverables and consolidated revisions. Owner authorizes external sending, commitments and payments. Do not invent agreement.

## Execute

- New chats cannot rely on memory. Fetch actual current repository files and record the branch/commit read.
- Read the entire global ledger, including rejected, archived, scripted and published ideas, before ideation. Check both topic and mechanism, not just title similarity.
- Present exactly the number of ideas requested in the documented format. Persist proposals if repository writing is available. Do not select a topic for the user unless delegated.
- Once a topic is selected, reserve its idea and story IDs, research deeply, develop a defensible thesis and internal outline, write the complete spoken draft in one go, then develop corresponding working narration and visual directors and underlying evidence. The editor executes the approved story treatment rather than inventing it.
- Do not require approvals for research, outline, each paragraph or routine revisions. Ask only when an unresolved decision materially changes the selected concept, budget or editorial premise.
- Browse original sources for research. Never fabricate facts, quotes, URLs, footage, analytics or source access. If browsing is unavailable, mark research blocked and explain what is missing.
- Money Moves research must establish the constraint, alternatives, information available at the time, execution, causal mechanism and competing explanations. Do not invent decisions, dialogue or hindsight certainty.
- Fallen Angels research must define the failure, reconstruct the original advantage and deterioration, distinguish fragility from trigger and symptoms from causes, and test competing explanations. Do not accept familiar downfall anecdotes without evidence.
- Changing Hands research must reconstruct positions/obligations or ownership, financing, the event timeline and the turning-point mechanism. Distinguish notional from capital, enterprise from equity value, and realized from paper results. No current investment recommendations.
- Fool’s Gold research must establish the legitimate baseline, apparent versus actual mechanism, credibility/verification gaps and exposure evidence. Distinguish allegations, admissions, established findings and unresolved issues; do not invent proof or victim anecdotes.
- Silver Spoon research must establish the relevant family relationships, wealth origins, ownership versus voting control versus leadership, transfer timeline and valuation basis. Do not invent private wealth, motives or family conflict.
- First Billion research must define the billion metric/currency/date and episode format, then reconstruct starting resources, first viable unit, expansion, capital requirements, ownership and milestone basis. Label hypothetical models, source assumptions, test downside/sensitivity and address starting advantages, timing and failed attempts. Do not promise repeatable wealth or equate company value with personal cash.
- On the Map also requires channels/on-the-map/RESEARCH_STANDARD.md. Define geography/period/outcome; establish starting conditions, first foothold, causal transitions, origin versus persistence, plausible alternatives, value capture and constraints. Test promotional origin stories and distinguish resident welfare from local output or asset wealth.
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

## Director owns visual direction
Read EDITOR_HANDOFF_STANDARD.md and DIRECTOR_PACKET_REVIEW.md. Prepare full working narration and visual directions at episode creation, then release only the three approved final editor-packet instructions after independent and integrated QA. The editor retains practical execution freedom. Research and internal reviews are not editor-facing documents.

## Network creative mandate (2026-10-11)

Before proposing ideas or reviewing any of the eight business channels, also read [NETWORK_CREATIVE_CHARTER.md](NETWORK_CREATIVE_CHARTER.md), [CREATIVE_GREENLIGHT.md](CREATIVE_GREENLIGHT.md) and the chosen channel's `CREATIVE_CONTRACT.md`. These add a demanding mass-audience premise and creative greenlight to the existing evidence, editorial and production gates. They never authorize invented conflict, unsupported claims or changes to approved script wording. Reject merely worthy ideas with weak broad-audience appeal. Record a short evidence-grounded creative verdict before deep research and again before marking scripted. Existing scripts remain unchanged until a requested or otherwise authorized revision.

## Current governing director-led release standard
The former **Editor owns visual treatment** section is superseded. Mandatory: read EDITOR_HANDOFF_STANDARD.md and DIRECTOR_PACKET_REVIEW.md at topic selection, production and review/revise. Green Knight owns title/thumbnail/visual cold open, visual story treatment and narrator direction. Always evaluate 01 canonical script, 02 full-text narrated performance direction, 03 visual direction and their cross-file integration when asked to review/revise. Do not leave an editor with an unguided script. Release only the three reviewed final files under the specific story's editor-packet/; maintain canonical script and research/evidence hashes, QA and registry status. Existing stories do not inherit packet approval.

## Editor clarity override
Read the **Editor clarity and decision hierarchy** section of EDITOR_HANDOFF_STANDARD.md. Internal exploration can contain alternatives; final 03 must contain ONE selected title, thumbnail and cold open, not creative options requiring the Fiverr editor to decide. Final 02 must identify the approved voice, separate non-spoken cues from full verbatim copy and tell editor to feed only 01 spoken body to TTS. Every visual scene must specify what starts on screen, what visibly changes, how it ends, relevant paragraph IDs, verified text/assets and editor freedom. Review packets as a fresh editor would, without access to our internal reasoning.

## Finished editor delivery QC (mandatory)
For a submitted editor video, thumbnail, narration audio, SEO or SRT, read [DELIVERY_QA_STANDARD.md](DELIVERY_QA_STANDARD.md) and the approved story editor-packet. Check the five agreed deliverables, audit exact speech/voice, executed visuals, technical issues, subtitles and upload chapters, and save versioned timecoded QC results. Distinguish inability to listen/view from a passing grade. This post-production gate does not add files to the three-document **instruction packet**. Consolidate one Fiverr revision request and verify subsequent cuts against it.

## One-command operating triggers (all eight channels)
An instruction to **create an episode / write the script** after an idea is selected means do the research and complete initial development of all three creative components: exact canonical script, a full **working** narrator director (verbatim spoken text and usable non-spoken performance instructions), and a **working** visual director (one selected title/thumbnail concept, concrete first frame and opening, scene-by-scene P/S transformations, factual asset/text limits and sound/transition cues). Save these drafts outside the final `editor-packet/`; no separate user prompt for narration and visual direction is needed. An explicit script-only request overrides this default.

A command to **review and revise** means cold-review script, narration director, visual director and their integration; implement justified changes, re-review and synchronize version/hash/anchors. Release exactly three final `editor-packet/` files only after all gates pass. **Unselected voice is a release blocker**, not an excuse to skip preparing thorough working drafts. State NOT READY and the precise blocker rather than silently releasing placeholders.

A command to **review editor delivery** means compare available MP4/thumbnail/clean narration/SEO chapters/SRT against the released three-file packet under DELIVERY_QA_STANDARD.md; log findings with actual timestamps and inspection methods, write one clear editor revision request, and recheck revisions. Film acceptance and publishing are distinct from editor-packet approval and require owner direction.

For batch operation, the owner may prepare all ten approved packets at once and negotiate two five-video milestones. Do not assume a daily script-send cadence, production deadlines, revision count, overlapping work, payment terms or ElevenLabs sharing until agreed. The first film should establish alignment before parallel production.



## Noninteractive automation mode (Green Knight Studio)

When a job explicitly specifies `automation_mode=true`, follow [automation/AUTOMATION_CONTRACT.md](automation/AUTOMATION_CONTRACT.md) and its versioned schemas/API contract. This changes orchestration only, never lowers editorial, evidence, channel, voice or QA standards. Route dynamically from live channel config/registry based on channel slug or ID; use one shared function workflow across channels. After an owner selects ideas, complete entire research, full script, both directors, independent review, justified revision, integration re-review and validation without routine chat approvals. Publish exactly the three approved editor-facing packet files only on a verified pass. Stop with a truthful BLOCKED state for source, approval, voice, factual, creative or validator blockers; a partial attempt is not a finished package. Preserve the existing registry status enum; track queue progress and editor/calendar state separately. Use idempotency, reserved identifiers, durable checkpoints, version-aware commits and concurrency-safe registry updates. Do not send Fiverr messages, approve payment, hand off, approve final edits, schedule or publish without appropriate user authorization.
