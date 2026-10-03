# Channels

This directory contains instantiated Green Knight channel definitions.

Each real channel should be created by cloning the canonical template from:

`01_templates/channel/`

Use:

```
channels/
  CH001-channel-slug/
    CHANNEL_CORE.md
    CHANNEL.md
    AUDIENCE.md
    CONTENT.md
    VOICE.md
    PACKAGING.md
    VISUAL_STYLE.md
    PRODUCTION.md
    EXAMPLES.md
    channel.yaml
    narration.yaml              # when synthetic narration is used
    NARRATION_CALIBRATION.md    # when synthetic narration is used
```

The permanent `channel_id` anchors the folder.

Channel names and slugs may change.

Do not create channel-specific copies of shared n8n workflows or portfolio-wide standards here.
