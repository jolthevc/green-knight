# Narration Standard

**Status:** Canonical portfolio-wide production standard  
**Purpose:** Define narrator ownership, channel voice configuration, and the production handoff for narration.

---

## 1. Principle

Green Knight owns the words and narrator identity. The editor owns how the narration is generated, performed, timed, and integrated against the picture.

Narration is a channel-level brand asset. The same channel should sound recognizably like the same narrator across videos.

Green Knight should standardize the narrator identity without over-automating the production step.

---

## 2. Source of Truth

### Channel identity

`channel.yaml` points to the channel's stable Green Knight narrator profile.

Example:

```yaml
voice:
  narrator_profile: "Dry, understated, slightly mischievous"
  synthetic_voice_allowed: true
  voice_profile_id: "loophole_narrator_v1"
```

### Provider implementation

`narration.yaml` records how that narrator profile is implemented:

- whether narration is required
- provider
- internal voice profile ID
- candidate or locked status
- provider voice ID
- baseline model ID
- baseline voice settings
- pace guidance

Provider voice IDs and model IDs are configuration, not secrets.

### Human calibration

`NARRATION_CALIBRATION.md` contains:

- narrator brief
- voice-design / search prompt
- calibration passage
- scorecard
- audition log
- lock instructions

The human operator chooses the actual channel voice once. Voice selection is a taste decision and should not be automated merely because it can be.

### Operational readiness

Google Sheets may track whether the channel narrator is:

- `NEEDS_SELECTION`
- `READY`
- `NOT_REQUIRED`

Sheets does not store provider voice IDs.

---

## 3. Production Handoff

For a synthetic-narration channel, Green Knight provides the editor with:

- approved final script
- locked channel narrator profile
- the approved provider voice
- baseline model/settings where applicable
- pronunciation notes
- channel voice guidance
- revocable access to the approved voice-generation platform where supported

The editor generates narration as part of production while working against the actual picture.

Do not require a finished narration file before `PRODUCTION_READY`.

Where direct editor platform access is impractical, Green Knight may generate and provide narration manually. This is a fallback production method, not a required automated workflow.

---

## 4. Editor Latitude

The editor may:

- generate and regenerate approved script passages with the locked channel voice
- split narration into useful production-sized passages
- adjust pauses and spacing
- change delivery pace within reasonable channel bounds
- regenerate a line with different emphasis or restraint
- modestly time-stretch audio while preserving pitch
- create silence for visual reveals, diagrams, or emotional beats
- choose the exact timing of narration against the picture

The editor should use the locked model/settings as the baseline where one has been recorded.

Material changes to the underlying provider model or narrator identity require Green Knight approval.

The editor may not silently:

- change the spoken wording
- alter factual meaning
- remove qualifications
- rewrite story structure
- substitute a different narrator identity

If wording needs to change, the issue returns upstream to editorial.

---

## 5. Production Files

Narration created during production should be retained in the video's `Production/` folder when useful for continuity, transferability, or revision.

A recommended location is:

`Production/Narration/`

The exact internal file layout is an editor-production choice. Green Knight does not require automated segmentation, manifests, master assembly, or narration version machinery unless operating scale later makes those controls valuable.

The final edit remains the canonical audiovisual product.

---

## 6. Access and Secrets

Editors should receive revocable provider workspace / seat access where the provider supports it.

Never share raw API keys with editors.

Provider API keys, if retained for future automation or administration, stay only in the approved secret / credential system.

Do not store secrets in GitHub, Sheets, channel YAML, production packets, or prompts.

---

## 7. Automation Boundary

Narration generation is intentionally **not** part of the initial automated video lifecycle.

Do not build or maintain automated TTS segmentation, generation, joining, Drive upload, regeneration archives, or narration manifests unless production volume proves that the manual editor step is a meaningful cost or bottleneck.

The system should earn this complexity.

The narrator-definition and voice-selection infrastructure remains canonical because it protects channel consistency regardless of who edits the video.
