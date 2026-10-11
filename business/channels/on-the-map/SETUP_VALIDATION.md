# Setup verification: 2026-10-11

Base main commit: a6cf27a4c785cc4c3f1148fd0f10116d9f689f11.

Added the eighth manual channel, OTM identifiers, foundation/research/script/voice guides, editor-owned style record, starter prompt, unselected narrator configuration and three proposed candidates. Updated shared discovery, routing, review, workflow and validator registration. Existing ledger entries and all existing story artifacts are unchanged.

## Checks
- Full validator on base and changed snapshot reports exactly the same two pre-existing errors: FB-I0001 claim C011 and C026 require supporting source IDs. Both are marked inference with empty source_ids in the saved First Billion evidence packet. This setup does not relabel them or invent sources.
- Base regression suite: 26 tests, 5 failures caused by those same two errors.
- Changed regression suite: 28 tests, the same 5 failures; 23 pass.
- Both new On the Map tests pass: missing research standard is detected and an idea using another channel prefix is rejected.
- Validator reported no additional errors for On the Map, registry integration, local links, profiles or existing scripts.
- Three imported candidates remain proposed; no story, voice audition, visual pilot or publication is claimed.

Repository-wide validation is not fully green. Repair of the two First Billion evidence references requires a separate source/evidence review. These are pre-existing content issues, not failures introduced by this channel setup.
