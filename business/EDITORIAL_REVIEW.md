# Editorial readiness and change control

A completed text package is an editorial result. An approved voice is a channel asset. Approved historical narration/visual versions stay in the channel's narration-history/visual-history directories when a newer version replaces them. A reviewed final cut is a production result. Keep these states distinct.

## State gates

| Stage | Required result |
| --- | --- |
| proposed | Saved card with canonical subject/mechanism/promise and duplicate assessment |
| selected | User-selected topic, stable IDs and real story metadata |
| researching | Active evidence gathering; unresolved gaps visible |
| researched | Research, populated evidence source/claim records and defensible synthesis; the script can still be unwritten |
| scripted | Complete clean script, current evidence/cue/scene references, packaging, handoff and recorded internal editorial review |
| production_ready | Scripted requirements plus reusable approved narrator snapshot and visual reference, with no blocking editorial issues |
| in_production | The editor has begun the agreed production scope |
| published | Verified public upload/date, actual 8–10 minute runtime and exact final-cut/audio review |

The initial voice/style choice is the owner's decision. Reusing an approved channel voice/reference does not create another mandatory user gate. Internal research, outline and text review do not require separate user approvals.

## Internal editorial review

Before scripted, review evidence, causal reasoning, narrative promises, spoken clarity, numbers, production feasibility and duplicate distinction. Record reviewer/date, passed status, reviewed_script_sha256 and blocking_issues in metadata.editorial.

For each consequential claim, evidence.json links the claim to source records and exact script paragraphs. Mark verified, inference or illustrative accurately. Review whether the source actually supports the claim; a structurally valid link does not establish truth.

Read the draft as an informed skeptic. Check the strongest contrary evidence, missing denominator, unearned certainty and whether the title overstates the research. Remove unsupported quotes and avoid copied prose. Brief relevant source excerpts are preferable to republishing source material.

## Revise coherently

Any spoken wording **or script title header** change increments script_version and changes the full-file SHA-256. The `TITLE: <metadata.title>` first line is non-spoken; paragraph and cue numbering begins with narration after its blank separator. Revisit cue/claim/scene anchors, timing, title promise and pronunciation. Update all affected files together. A punctuation/line-break change also changes the byte hash; review the impact rather than pretending the old audio automatically matches.

Clear editorial.passed and reviewed_script_sha256 until the revision is reviewed. Clear production review if the approved cut/audio is affected. Preserve revision history and the reason. Recheck freshness-sensitive claims immediately before production/upload.

## Evidence ownership

evidence.json owns source/claim/scene IDs and machine-checkable script links. sources-and-claims.md is the readable review/synthesis of that map; do not maintain a contradictory second ledger. visual-plan.md expands the scene records with creative direction.

Sources need access date/status and a supporting locator. A lead-only source cannot support a consequential non-illustrative claim. Every spoken paragraph needs visual coverage. Claims and scenes are tied to the script hash/version.

The validator catches missing records, stale references and false stage readiness. It cannot assess source truth, originality, emotional quality, actual audience interest or whether someone really listened.

## evidence.json record shape

Source IDs use S001, claim IDs C001 and scene IDs SC001.
- Source: id, publisher, title, url, accessed_at, locator, access_status. published_at and limitations can add context.
- Claim: id, paragraph_id, anchor, claim, source_ids, status, basis. At researched, paragraph references can be null because no script exists yet.
- Scene: id, paragraphs (an array of paragraph_id/anchor objects), purpose, evidence_type, source_ids. A scene can cover several paragraphs; multiple scenes can cover a paragraph.

At scripted, all claim and scene references must match real paragraphs. Source URL formatting is checked, but source existence and meaning still require opening and reviewing the document.

## Story-first audience review

Apply ENGAGEMENT_STANDARD.md during the existing internal editorial review, not as another owner approval gate. Inspect the lead, first payoff, beat-by-beat changed understanding, the weakest middle stretch and the earned final insight. Record newcomer comprehension risks and informed-skeptic objections with fixes in synthesis-and-outline.md and qa.md. Structural validation cannot establish engagement; no viewing results are claimed before a real pilot or publication.

## Handoff ownership

Apply EDITOR_HANDOFF_STANDARD.md. Content coverage is not an approved storyboard. A script-stage visual-plan.md may explicitly await the editor's proposal. Narration-guide.md must match canonical cues; research-for-editor.md must match evidence. Sending visual descriptions is outside the default handoff.
