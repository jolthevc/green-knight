# Narration Standard

**Status:** Canonical portfolio-wide production standard
**Purpose:** Define how Green Knight produces canonical narration centrally, and how responsibility splits between the portfolio, the channel and the video.

---

## 1. Principle

Green Knight owns the words and narrator identity. The editor owns how the narration breathes against the picture.

Narration is a channel-level brand asset. The same channel always sounds like the same narrator.

---

## 2. Three Levels

### Portfolio (this standard + `NARRATION_PROVIDERS.yaml`)
The reusable narration system: provider abstraction, TTS integration, segmentation, file naming, master assembly, validation and Drive persistence. Workflows refer to a logical provider key (initially `elevenlabs`). Provider-specific details live only in `NARRATION_PROVIDERS.yaml` and one adapter in `VIDEO_NARRATION`.

### Channel (`channels/<channel>/narration.yaml` + `VOICE.md`)
The narrator identity: `required`, `provider`, `voice_profile`, `profile_status`, `voice_id`, `model_id`, optional `voice_settings` and `seed`. `voice_id` and `model_id` are configuration, not secrets. They stay `null` until a voice is auditioned with the channel calibration passage and the profile is `locked`. Changing the voice means a new profile version (`..._v2`), never a silent edit.

### Video (optional `NARRATION_NOTES` Google Doc in the video folder)
Delivery metadata for one video. It never changes the channel voice identity. Sections (each line is optional):

```
PRONUNCIATION
Banaszak => buh-NAZZ-ick

PAUSES
after "Into their own net." => 1.0

EMPHASIS
"primary purpose" => slight stress

SEGMENT PACING
seg03 => 0.95

SEGMENTS
start "Nothing in the rulebook said"
```

- Pronunciation respellings are applied to the text sent to the provider only. The approved script is unchanged.
- Pauses are sent to the provider only where the locked model supports break tags. Otherwise they go to the editor in the manifest.
- Emphasis notes go to the editor in the manifest.
- Segment pacing is a speed multiplier, clamped to 0.85-1.15.
- Forced splits start a new segment at a paragraph containing the quoted phrase.

Pronunciation lines in the approved script header (`Pronunciation:`) are used too. Video notes win on conflict.

---

## 3. Source Text

Narration is generated only from the approved clean script (`05_SCRIPT_vN` narration block, no script review record, built from the approved outline, with a selected packaging packet built on it). Narration generation never rewrites the script. Every segment is an exact slice of the approved narration, and the manifest records both the script text and the provider text.

---

## 4. Delivery: `Production/Narration/`

- `<video_id>_narration_seg01.mp3`, `..._seg02.mp3`, ...: segments split at natural paragraph/story boundaries, not fixed durations.
- `<video_id>_narration_master.mp3`: the segments joined in order with no added silence.
- `<video_id>_narration_manifest.json`: segment order, script text, provider text, voice profile, voice and model IDs, settings, and editor notes.

Existing narration is never overwritten. A deliberate regeneration moves the previous files to a dated `_superseded_...` subfolder.

---

## 5. Editor Latitude

The editor may trim or extend silence, reposition clips, adjust line spacing, modestly time-stretch while preserving pitch, make small pacing adjustments, make room for reveals or diagrams, and request regeneration of a line or segment.

The editor may not silently change wording, factual meaning or voice identity. Wording changes go back upstream to editorial.

---

## 6. Secrets

Provider API keys live only in the n8n credential store. Never in GitHub, Sheets, channel YAML, workflow source or prompts.
