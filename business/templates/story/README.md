# Story template

Copy this directory, excluding README.md, into the selected channel's stories/<story-id>-short-slug/ using its story_prefix from channel.json (PP-V####, MM-V####, FA-V####, DH-V####, FG-V####, SS-V#### or FB-V#### for the currently built channels). Set metadata.channel, idea_id and story_id explicitly; the shared metadata template does not preselect a channel. Replace placeholders and populate every required file before marking scripted. Template placeholders are never production deliverables.

| File | Owner / purpose |
| --- | --- |
| metadata.json | Stable IDs, version, status, timing assumptions, actual assets and narration settings |
| brief.md | Selected question, promise, audience and duplicate distinction |
| research.md | Evidence, mechanism, counterpoints and gaps |
| evidence.json | Canonical source/claim/scene records and script hash/version |
| sources-and-claims.md | Readable evidence review consistent with evidence.json |
| synthesis-and-outline.md | Editorial thesis, beat plan and promise/payoff map |
| script.txt | First line `TITLE: <metadata.title>`, blank line, then complete clean spoken narration; the header is not spoken |
| delivery-cues.json | Non-spoken directions tied to exact script hash/version |
| voice-production.md | Pronunciations, takes, retakes and actual listening record |
| visual-plan.md | Internal editor-owned record awaiting actual proposal |
| packaging.md | Titles, thumbnails, description, chapters and CTA |
| narration-guide.md | Readable audio directions matching canonical cues |
| research-for-editor.md | Concise factual support for the editor |
| handoff.md | Clean audio/research handoff without visual descriptions |
| qa.md | Editorial checks, production checks and approval status |
| performance.md | Verified upload and post-publication learning |

Do not copy placeholder text into a voice generator. The intentionally empty template script.txt requires a real full script before status scripted. On completion, the title must be present as the very first line in **all eight channels**: `TITLE: Exact Episode Title`, then one blank line, then narration. The header is not narrated or included in word count, P001 cue references, captions or TTS input. The **entire file**, including the header, is hashed for metadata/evidence/cues. The validator rejects missing or mismatched title headers. Delivery cues do not need to exist for every paragraph; purposeful cues are sparse.

metadata.status and registry.status must agree. Increase script_version when wording changes. Record meaningful changes in metadata.revision_history and registry.history. The final recording is timed by the editor; initial word-based estimates are provisional.

Use [editorial review](../../EDITORIAL_REVIEW.md) for stage gates and [narration standard](../../NARRATION_STANDARD.md) for profiles and listening. voice-production.md is populated during production, not fabricated at scripted. evidence.json must be populated before researched; script references become mandatory at scripted.

Follow EDITOR_HANDOFF_STANDARD.md. Do not send internal visual/packaging plans or full editorial audits as mandatory editor inputs.

On the Map uses OTM-I####/OTM-V####. Keep its geographic scope, origin/persistence evidence, alternative explanation, beneficiaries and constraints in the existing brief/research/synthesis files; consult channels/on-the-map/RESEARCH_STANDARD.md. No additional storyboard is required.

## New mandatory editor packet template
Copy editor-packet/ only as internal scaffolding; its placeholders are not approved deliverables. The *final*, after revisions editor-packet has precisely 01_SCRIPT.txt, 02_NARRATION_DIRECTOR.md, 03_VISUAL_DIRECTOR.md and nothing else. Only release after separate reviews of the script, full-text performance guide, visual thumbnail/opening/sequence guide and their integration (DIRECTOR_PACKET_REVIEW.md). Former “editor owns treatment” restrictions above are superseded.
