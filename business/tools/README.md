# Local validation

Requires Python 3 standard library only. From the repository root:

```bash
python3 business/tools/validate.py
```

Checks the shared registry, stable identifiers, story links/status, required editorial files and cue anchors. Templates are not mistaken for completed episodes. It does not fact-check claims or replace listening to the final cut.

For a populated story, get a provisional timing calculation:

```bash
python3 business/tools/episode_check.py business/channels/pretty-penny/stories/PP-V0001-short-slug
```

Use the actual existing directory, not the illustrative name above. The checker validates cues and script cleanliness, prints timing assumptions and checks measured runtime when metadata supplies it. Writing estimates into metadata is an explicit editorial task; the tool does not silently modify files.
