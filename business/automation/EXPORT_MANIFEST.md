# Export manifest v1

For each story ID, confirm approved released packet matches latest canonical script hash and final reviewed director version. The editor-facing ZIP contains **exactly the three canonical documents** at top level:
- `01_SCRIPT.txt` (nonspoken TITLE header remains intact)
- `02_NARRATION_DIRECTOR.md`
- `03_VISUAL_DIRECTOR.md`

Make optional read-only PDF mirrors under a distinct `pdf/` sibling folder and a convenience `editor-packet.zip`. Batch ZIP nests folders by stable story ID to avoid collisions. Maintain source repository path, git commit SHA, script SHA-256, export timestamp and derived-file identifiers as a metadata manifest **outside** the editor packet. No research, evidence JSON, QA logs or alternative copy inside editor handoff. Display PDFs as conveniences, never the authority for spoken text.

Drive folder: `Green Knight/<channel_slug>/<story_id>-<short-slug>/` with `editor-packet/`, `pdf/`, `production/`, `final/`. Create folders idempotently, store Drive folder/file IDs in the operational record and use checksums to avoid duplicate uploads. Keep the last valid package rather than returning broken links if a Drive upload fails, but report blocked export until verified. Do not claim PDFs or Drive exports exist until confirmed.
