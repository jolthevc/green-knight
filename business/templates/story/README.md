# Story template

Copy this directory, excluding README.md, into the selected channel's stories/<story-id>-short-slug/ using its story_prefix from channel.json (PP-V####, MM-V####, FA-V####, DH-V####, FG-V#### or SS-V#### for the currently built channels). Set metadata.channel, idea_id and story_id explicitly; the shared metadata template does not preselect a channel. Replace placeholders and populate every required file before marking scripted. Template placeholders are never production deliverables.

| File | Owner / purpose |
| --- | --- |
| metadata.json | Stable IDs, version, status, timing assumptions, actual assets and narration settings |
| brief.md | Selected question, promise, audience and duplicate distinction |
| research.md | Evidence, mechanism, counterpoints and gaps |
| evidence.json | Canonical source/claim/scene records and script hash/version |
| sources-and-claims.md | Readable evidence review consistent with evidence.json |
| synthesis-and-outline.md | Editorial thesis, beat plan and promise/payoff map |
| script.txt | Complete clean spoken words, created after research |
| delivery-cues.json | Non-spoken directions tied to exact script hash/version |
| voice-production.md | Pronunciations, takes, retakes and actual listening record |
| visual-plan.md | Paragraph-linked scenes and factual graphics |
| packaging.md | Titles, thumbnails, description, chapters and CTA |
| handoff.md | Exact editor inputs, constraints and deliverables |
| qa.md | Editorial checks, production checks and approval status |
| performance.md | Verified upload and post-publication learning |

Do not copy placeholder text into a voice generator. The intentionally empty template script.txt requires a real full script before status scripted. Delivery cues do not need to exist for every paragraph; purposeful cues are sparse.

metadata.status and registry.status must agree. Increase script_version when wording changes. Record meaningful changes in metadata.revision_history and registry.history. The final recording is timed by the editor; initial word-based estimates are provisional.

Use [editorial review](../../EDITORIAL_REVIEW.md) for stage gates and [narration standard](../../NARRATION_STANDARD.md) for profiles and listening. voice-production.md is populated during production, not fabricated at scripted. evidence.json must be populated before researched; script references become mandatory at scripted.

Follow EDITOR_HANDOFF_STANDARD.md. Do not send internal visual/packaging plans or full editorial audits as mandatory editor inputs.
