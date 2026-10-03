# Google Drive Architecture

**Status:** Canonical portfolio-wide storage standard  
**Purpose:** Define where Green Knight stores channel working files, per-video artifacts, production files, and published assets.

---

## 1. Role of Google Drive

Google Drive is the canonical home for large, video-specific working artifacts and production files.

Drive answers:

> Where is the actual work product for this channel and video?

Drive should contain:

- video briefs
- research packets
- source logs
- outlines
- scripts
- packaging packets
- production packets
- narration files
- source assets
- graphics
- thumbnails
- edit project files where retained
- first cuts and revisions
- final video files
- captions
- QA records
- postmortems

Drive should **not** become the canonical home for:

- portfolio governance
- reusable standards
- reusable prompts
- schemas
- channel definitions
- structured performance data

Those belong in GitHub or Google Sheets according to the system-of-record standard.

---

## 2. Root Structure

The current Green Knight Drive root is:

```
Green Knight Holdings/
  Green Knight - Portfolio Database
  Channels/
    _CHANNEL_TEMPLATE/
      Unpublished/
        _VIDEO_TEMPLATE/
          Assets/
          Production/
          Final/
      Published/
```

The template folders define the expected shape for every future channel.

The template itself is not a real media property and should not be used for production work.

---

## 3. Channel Folder Standard

When a channel is approved for build, create:

```
Channels/
  CH001 - Channel Name/
    Unpublished/
    Published/
```

Use the permanent `channel_id` at the beginning of the folder name.

The public channel name may change.

The channel ID should not.

Example:

```
CH003 - Hidden Systems/
```

If the channel later rebrands, the folder may become:

```
CH003 - How It Really Works/
```

The ID preserves continuity.

---

## 4. Unpublished vs Published

Every channel has two primary operating folders.

### `Unpublished`

Contains videos that are:

- selected
- in research
- being outlined
- being scripted
- being packaged
- in production
- in QA
- scheduled but not yet published

### `Published`

Contains videos that are live on the primary platform.

When a video publishes, move the entire canonical video folder from `Unpublished` to `Published`.

Do not create a second copy.

The folder should retain its permanent Drive folder ID where possible.

The Sheet's `drive_folder` reference should therefore continue pointing to the same video folder after publication.

---

## 5. Video Folder Naming

A selected video receives a permanent `video_id`.

Recommended folder naming:

```
CH001-V0001 - Working Video Title
```

The video ID is canonical.

The descriptive title is for human navigation.

The folder name may be updated if the working title changes materially, but the video ID must remain unchanged.

Do not use the final YouTube title as the sole identifier.

---

## 6. Canonical Video Folder Structure

A normal video folder should look like:

```
CH001-V0001 - Working Video Title/
  01_VIDEO_BRIEF
  02_RESEARCH_PACKET
  03_SOURCE_LOG
  04_OUTLINE
  05_SCRIPT
  06_PACKAGING_PACKET
  07_PRODUCTION_PACKET
  08_QA_RECORD
  09_POSTMORTEM

  Assets/
  Production/
  Final/
```

The artifact numbers represent logical order, not workflow state.

Files may be created only when the video reaches the relevant stage.

A newly selected video should not contain empty placeholder documents simply to match the structure.

---

## 7. Artifact File Types

### Working editorial artifacts

Prefer native Google Docs for:

- video brief
- research packet
- source log when text-first
- outline
- script
- packaging packet
- production packet
- QA record
- postmortem

A different format is acceptable when the artifact's needs justify it.

For example, a structured source log may eventually be better represented as a Sheet or another machine-readable format.

The artifact standard matters more than the file type.

### Binary and production assets

Use normal Drive files for:

- audio
- images
- video
- PDFs
- downloaded source material
- design files
- editing project files
- subtitle files
- exports

---

## 8. Assets Folder

`Assets/` contains source material used in production.

Examples:

- licensed stock
- archival images
- source PDFs
- screenshots
- diagrams
- maps
- raw graphics
- logos
- supplied brand assets
- music where applicable

Where rights status matters, preserve enough context to understand how an asset may be used.

Do not treat the existence of a file in `Assets/` as proof that it is licensed for publication.

---

## 9. Production Folder

`Production/` contains intermediate edit work.

Examples:

- narration audio generated during production when retained
- editor project files
- first cuts
- review exports
- revision exports
- temporary graphics
- rendered sequences
- production handoff files

The exact content may vary by editor or production tool.

The folder should preserve enough source material to make contractor replacement possible where economically practical.

Do not require retention of enormous disposable caches or render files that have no future value.

---

## 10. Final Folder

`Final/` contains the approved publishable package.

At minimum, where applicable:

- final video master
- final thumbnail
- captions / subtitle file
- final narration if retained separately
- other platform-ready exports

The final folder should not contain abandoned drafts.

A future system should be able to identify the current canonical output without guessing among files called:

- final
- final2
- final-final
- final-v7

Use explicit versions during review and one clear approved master at completion.

---

## 11. Artifact Naming

Recommended pattern:

```
01_VIDEO_BRIEF_v1
02_RESEARCH_PACKET_v1
03_SOURCE_LOG_v1
04_OUTLINE_v1
04_OUTLINE_v2
05_SCRIPT_v1
05_SCRIPT_v2
06_PACKAGING_PACKET_v1
07_PRODUCTION_PACKET_v1
08_QA_RECORD_v1
09_POSTMORTEM_v1
```

The filename should communicate:

- artifact type
- sequence
- version

Do not include changing titles in every artifact filename.

The containing video folder already provides video identity.

---

## 12. Versioning

Create a new version when a change is materially useful to preserve.

Examples:

- outline structure changes
- thesis changes
- major script rewrite
- packaging direction changes
- substantial production packet revision

Do not create a new version for every typo correction.

When a new version becomes canonical, downstream systems should reference the latest approved version.

Old versions remain historical.

---

## 13. Approved vs Working State

Drive may contain several versions.

The database should not attempt to list every file.

The workflow should maintain knowledge of which artifact version is currently approved.

Until a dedicated artifact registry is justified, this may be represented through:

- deterministic naming
- workflow state
- the latest approved artifact link in n8n execution state
- document metadata or a simple manifest where necessary

Do not add an artifact-level database merely because it is theoretically cleaner.

Add one only if operational complexity makes it valuable.

---

## 14. Post-Publication Folder Behavior

When a video publishes:

1. confirm the final package is in `Final/`
2. confirm publication metadata is written to Sheets
3. move the entire video folder from `Unpublished` to `Published`
4. preserve the same `video_id`
5. preserve the same folder identity where possible
6. add/update the postmortem as performance matures

Published does not mean immutable.

Postmortems, source corrections, or updated platform assets may still be added.

---

## 15. Killed Videos

Do not automatically delete killed video folders.

A killed video may contain valuable research or evidence about a failed thesis.

Initially, leave the folder in `Unpublished` and rely on the Sheet status `KILLED`.

If killed-volume becomes operationally noisy, Green Knight may later introduce an `Archived` folder.

Do not add that folder until there is a real need.

---

## 16. Channel-Level Shared Assets

Do not create many channel-level subfolders before they are needed.

If a channel begins accumulating reusable assets, it may add a small number of clearly justified folders such as:

- `Brand Assets`
- `Reusable Graphics`
- `Reference`

These should sit beside `Unpublished` and `Published`.

Do not create them by default if they are empty.

---

## 17. Links Back to Sheets

Every active channel row in `00_CHANNELS` should contain its canonical Drive channel folder.

Every selected video row should contain its canonical Drive video folder.

The Drive link is the bridge from structured database record to large working artifact.

The Sheet should not duplicate the artifact contents.

---

## 18. Links Back to GitHub

Drive artifacts should be created using the standards in the `green-knight` repository.

The Drive folder does not need copies of GitHub governance files.

A production workflow should load the relevant GitHub standards and channel definitions before generating or evaluating Drive artifacts.

This avoids divergent copies of the same rules.

---

## 19. Contractor Access

Contractors should generally receive access only to the folders required to perform their work.

Prefer revocable permissions over transferring ownership.

Where possible:

- Green Knight retains ownership
- Green Knight retains source files
- final assets are returned to the canonical video folder
- contractor-specific storage is not the only copy of valuable work

The system should support replacing a contractor without losing the channel's operating history.

---

## 20. Folder Creation Automation

When a video moves from `IDEA` to `SELECTED`, n8n should eventually:

1. assign the permanent video ID if not already assigned
2. create the canonical video folder under the channel's `Unpublished` folder
3. create:
   - `Assets`
   - `Production`
   - `Final`
4. write the resulting Drive folder link into the video row
5. create downstream artifacts only when required by lifecycle stage

When a channel is created, n8n should eventually:

1. create the channel folder
2. create `Unpublished`
3. create `Published`
4. write the channel Drive folder into `00_CHANNELS`
5. duplicate the canonical video Sheet tab
6. clone the canonical GitHub channel template

The detailed automation implementation will be defined later.

---

## 21. Design Principle

The Drive architecture should remain boring.

Its job is to make every asset easy to locate, transfer, audit, and hand to a human or machine.

Do not add folder depth because it feels organized.

Add structure only when it reduces ambiguity or operational friction.
