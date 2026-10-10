# Local validation

Requires Python 3 standard library only. From the repository root:

```bash
python3 business/tools/validate.py
```

Checks all six channel definitions and narrator profiles, shared registry, stable identifiers, orphan story folders, stage gates, script hashes, cue/claim anchors and visual coverage. Templates are not mistaken for completed episodes. It does not fact-check claims or replace listening to the final cut.

For a populated story, get a provisional timing calculation:

```bash
python3 business/tools/episode_check.py business/channels/pretty-penny/stories/PP-V0001-short-slug
```

Use the actual existing directory, not the illustrative name above. The checker validates cues and script cleanliness, prints the exact UTF-8 script hash and timing assumptions and checks measured runtime when metadata supplies it. Writing estimates into metadata is an explicit editorial task; the tool does not silently modify files.

Run the stage/voice integrity regression checks:

```bash
python3 -m unittest discover -s business/tools -p 'test_*.py'
```

Synthetic fixtures are built in temporary folders only. They are not real ideas, recordings, evidence or published videos. The tools do not check factual truth, listen to audio, open sources or guarantee YouTube performance. Record actual review evidence separately.
