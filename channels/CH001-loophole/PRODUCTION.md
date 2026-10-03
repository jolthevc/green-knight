# Production Standard

This extends EDITOR_CREATIVE_STANDARD.md, VISUAL_QUALITY_STANDARD.md, and EDITOR_BRIEF_TEMPLATE.md.

## 1. Model
**AI-assisted (Green Knight):**
- Ideation and backlog mining.
- Research, including sourcing the exact rule text.
- Outline and script.
- Packaging concepts.
- The production packet, with diagram specifications.
- Canonical narration audio, generated centrally from the approved script and the channel voice profile.

**Human:**
- One editor with motion-graphics ability.
- Thumbnail execution by the editor or a designer.
- Rights review.
- Fact QA.
- Final approval.

Judgment concentrates in diagram design, archival selection, and pacing. Research is finished before the edit, so the editor never rediscovers the story.

## 2. Format
- Long-form, 16:9, 1080p minimum (4K preferred), 24 or 30 fps.
- Runtime of 11-18 minutes, with a target of 14.
- Proposed calibration cadence of 2 videos per month.
- Narration: AI voice, generated centrally by Green Knight (see section 3).
- Narration readiness: REQUIRED. A video cannot reach PRODUCTION_READY until the canonical narration package exists.

## 3. Narration
Green Knight generates the canonical narration centrally. It is built from the approved script and the channel voice profile. Editors do not generate the voice themselves. The aim is a consistent voice and lower production cost, without making the edit rigid.

**Delivery.** Narration is delivered in `Production/Narration/` inside the video folder:
- One master narration file.
- Segmented clips or stems, one per logical script section or passage. Segments follow natural script and story boundaries, not a fixed duration.
- Eventually, a small machine-readable manifest giving segment order, text, and version.

The editor receives these files as production inputs.

**The editor may:**
- Trim or extend silence.
- Reposition narration clips.
- Adjust spacing between lines.
- Modestly time-stretch clips while preserving pitch.
- Make small pacing adjustments.
- Create room for visual reveals or diagrams.
- Request regeneration of an individual line or segment when a materially different delivery is needed.

**The editor may not** silently change the spoken wording, the factual meaning, or the voice identity. If a line needs different wording, it returns upstream to editorial.

Green Knight owns the words and narrator identity. The editor owns how the narration breathes against the picture.

## 4. Inputs Before the Edit
- Approved script.
- Canonical narration package: master file plus segmented clips, in `Production/Narration/`.
- Production packet.
- Source log with rule-text extracts and clipping provenance.
- Diagram specifications.
- Licensed assets, or a list of assets to license.
- Thumbnail brief with 2-3 concepts.
- Pronunciation notes.

## 5. Packet
The packet is organized by section. Each section contains:
- Narration block.
- Visual objective.
- REQUIRED diagram specification: actors, sequence, and the highlighted exploiter.
- Exact old and new rule text for the Amendment, with the year.
- Preferred archival items.
- Pacing notes.

Secondary visuals are marked OPEN.

## 6. Responsibilities
**Editor:**
- Diagram animation.
- Sourcing from approved libraries.
- Pacing, music, and sound, including narration timing within the latitude in section 3.
- Typography within the brand kit.
- Flagging any visual that could misstate a play or rule.

**Green Knight:**
- Thesis, research, script, and canonical narration (words and voice identity).
- Rule verification.
- Brand kit: fonts, palette, token library, and Amendment template.
- Rights decisions.
- Final approval.

## 7. Thumbnails
The thumbnail is executed after the first cut, from the packaging concepts. It requires Green Knight approval.

## 8. Revisions
- Two rounds.
- Notes are tagged MUST FIX, STRONG PREFERENCE, or OPTIONAL THOUGHT.
- Script or claim changes return to editorial. This includes any change to narration wording.

## 9. Channel QA
- Diagrams match documented sequences.
- Amendment text and year match the real rule.
- On-screen scores and dates are correct.
- Recreations and archival material are labeled.
- No unlicensed league footage or logos.
- The package promise lands by 30 seconds.
- Multi-cause rule changes are acknowledged.

## 10. Rights
- No league broadcast footage by default. Any fair-use clip requires explicit rights review.
- Stills from licensed agencies or the public domain.
- Clipping provenance recorded.
- Licensed music only.
- AI assets follow VISUAL_STYLE.md.

## 11. Delivery
Files:
- CH001-V0001_cut_v1.mp4
- CH001-V0001_master.mp4
- CH001-V0001_thumb_final.png
- CH001-V0001_captions.srt

The editor also delivers project files, diagram sources, and additions to the reusable token and Amendment library, which is a channel asset.

Access is revocable at Drive folder level. No credentials are shared.

## 12. Cost
Target cost is set during calibration of the first five videos. Track editor, thumbnail, centrally generated voice, and archival licensing separately. Licensing and graphics hours are the variables to watch. The reusable library should reduce diagram time over successive episodes.

## 13. Failure Modes
- Generic diagrams where the exploiter isn't highlighted.
- Random sports stock.
- Broadcast-clip shortcuts.
- A formulaic Amendment.
- Graphics scope creep inflating cost.
- Narration wording or voice silently changed in the edit.