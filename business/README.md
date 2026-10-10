# Business channels

Every channel in this business umbrella targets **8–10 minutes per finished episode**, including opening, narration, pauses, visual holds and closing.

| Channel | Viewer promise | Workspace |
| --- | --- | --- |
| Pretty Penny | Understand the money machine behind familiar things | [Built first](channels/pretty-penny/README.md) |
| Money Moves | Understand the strategic decision that changed a business | [Built second](channels/money-moves/README.md) |
| Fallen Angels | Understand how a business lost its advantage or collapsed | Planned |
| Changing Hands | Understand the stakes and mechanism of a consequential trade or deal | Planned; working name |
| Fool’s Gold | Understand how a financial deception worked and was exposed | Planned |
| Silver Spoon | Understand how family fortunes are built, inherited, kept or lost | Planned |

Names do not justify duplicate lanes. A company can feature on several channels only when each episode answers a different central question.

## Start here

1. Read [AGENTS.md](AGENTS.md), then the chosen channel's README and start-a-chat prompt.
2. Read the [workflow](WORKFLOW.md) and [shared idea registry](ideas/registry.json).
3. Generate ideas in the [standard format](IDEATION.md), then let the user select.
4. Research, synthesize, write one complete script, revise internally, and produce separate voice and visual directions.
5. Save the actual artifacts and update the registry in the same commit.

[YouTube guidance](YOUTUBE_GUIDANCE.md) separates official platform guidance from our editorial hypotheses. [Templates](templates/story/README.md) give every story the same files. [Pilot acceptance](PILOT_ACCEPTANCE.md) gives us a consistent way to compare editors before ordering batches.

## Scope and ownership

This is an explicitly scoped manual business workflow requested by the owner. Within `business/`, GitHub owns the idea registry and text story artifacts. This overrides the existing system-of-records restriction on per-video GitHub artifacts **only for this workspace**. Existing `channels/`, Sheets, Drive and n8n remain a separate system. These business channels are not yet registered there; creating these files does not create a YouTube channel, a Sheet row, an automation or a Drive folder.

Use channel-specific idea/video identifiers here (PP for Pretty Penny; MM for Money Moves), not CH identifiers allocated to the existing portfolio. A future automation migration must map identifiers, choose one canonical ledger, and migrate rather than silently dual-write. Do not create duplicate operational state in Sheets.

Keep large media, source PDFs, recordings and editable project files in external storage; commit their stable links in story metadata. Do not commit passwords, API keys, private editor contact details or licensed source files.

Pretty Penny and Money Moves are built now; their pilot details remain open. Build each remaining channel deliberately after its name, boundaries and style are confirmed.
