# Business channels

**Fresh GPT or Fiverr script? [Start with continuity](CONTINUITY_HANDOFF.md), then the channel-specific standards and live registry.** Latest externally revised drafts are linked there, and [producer visual direction](PRODUCER_VISUAL_DIRECTION.md) records the hybrid references and script-writing workflow.


Business channels normally target **8–10 minutes per finished episode**, including opening, narration, pauses, visual holds and closing. **Exception: Fame & Fortune targets 10–20 minutes, ideally 15 minutes (900 seconds).** Runtime is channel-configured and must be honored by scripting and validation.

| Channel | Viewer promise | Workspace |
| --- | --- | --- |
| Pretty Penny | Understand the money machine behind familiar things | [Built first](channels/pretty-penny/README.md) |
| Money Moves | Understand the strategic decision that changed a business | [Built second](channels/money-moves/README.md) |
| Fallen Angels | Understand how a business lost its advantage or collapsed | [Built third](channels/fallen-angels/README.md) |
| Changing Hands | Understand the stakes and mechanism of a consequential trade or deal | [Built fourth; working name](channels/changing-hands/README.md) |
| Fool’s Gold | Understand how a financial deception worked and was exposed | [Built fifth](channels/fools-gold/README.md) |
| Silver Spoon | Understand how family fortunes are built, inherited, kept or lost | [Built sixth](channels/silver-spoon/README.md) |
| First Billion | Trace the steps, economics and ownership that build a defined billion-dollar outcome | [Built seventh](channels/first-billion/README.md) |
| On the Map | Discover why economic activity began here, stayed and shaped the place | [Built eighth](channels/on-the-map/README.md) |
| Hard Costs | The economics, operators and extraordinary stories behind what gets built | [Built ninth](channels/hard-costs/README.md) |
| Built to Scale | The growth playbook for construction/trade business owners and aspiring operators | [Built tenth](channels/built-to-scale/README.md) |
| House Money | Discover the businesses, financing and money flows behind where we live | [Built eleventh](channels/house-money/README.md) |
| Fame & Fortune | The surprising deals, ownership structures and fortunes behind famous entertainers and athletes | [Built twelfth](channels/fame-and-fortune/README.md) |

Names do not justify duplicate lanes. A company can feature on several channels only when each episode answers a different central question.

## Start here

1. Read [AGENTS.md](AGENTS.md), then the chosen channel's README and start-a-chat prompt.
2. Read the [workflow](WORKFLOW.md) and [shared idea registry](ideas/registry.json).
3. Generate ideas in the [standard format](IDEATION.md), then let the user select.
4. Research, synthesize and develop the script, working narration direction and working visual direction together (including thumbnail and opening); review and finalize all three before editor-packet release.
5. Save the actual artifacts and update the registry in the same commit.

[Narration production](NARRATION_STANDARD.md), [editorial stage gates](EDITORIAL_REVIEW.md) and [lane routing](LANE_ROUTING.md) govern quality and consistency. [YouTube guidance](YOUTUBE_GUIDANCE.md) separates official platform guidance from our editorial hypotheses. [Templates](templates/story/README.md) give every story the same files. [Pilot acceptance](PILOT_ACCEPTANCE.md) gives us a consistent way to compare editors before ordering batches.

## Scope and ownership

This is an explicitly scoped manual business workflow requested by the owner. Within `business/`, GitHub owns the idea registry and text story artifacts. This overrides the existing system-of-records restriction on per-video GitHub artifacts **only for this workspace**. Existing `channels/`, Sheets, Drive and n8n remain a separate system. These business channels are not yet registered there; creating these files does not create a YouTube channel, a Sheet row, an automation or a Drive folder.

Use channel-specific idea/video identifiers here (PP for Pretty Penny; MM for Money Moves; FA for Fallen Angels; DH for Changing Hands; FG for Fool’s Gold; SS for Silver Spoon; FB for First Billion; OTM for On the Map), not CH identifiers allocated to the existing portfolio. A future automation migration must map identifiers, choose one canonical ledger, and migrate rather than silently dual-write. Do not create duplicate operational state in Sheets.

Keep large media, source PDFs, recordings and editable project files in external storage; commit their stable links in story metadata. Do not commit passwords, API keys, private editor contact details or licensed source files.

All twelve business channel workspaces are built. Voice selection, integrated visual pilots, editor scope/pricing and publication schedules remain pilot-stage decisions. Changing Hands remains a working name. Start with idea selection and a reviewable pilot before purchasing repeat batches.

[Latest six-channel audit](AUDIT_2026-10-10.md) records gaps fixed, validation and decisions that require real pilots.

[Standalone script review and revision](SCRIPT_REVIEW.md) defines a critical, audio-first YouTube story audit with anchored findings, prioritized fixes and a controlled revision process for all configured business channels. Run it from a fresh chat after a full script is saved.

[Story-first engagement](ENGAGEMENT_STANDARD.md) defines the broad-audience learning experience, eight story engines and internal newcomer/skeptic review. Use it for ideation, outlines, scripts, production and learning.

[Director-owned editor handoff](EDITOR_HANDOFF_STANDARD.md): Green Knight directs the documentary's spoken and visual story; the editor executes it with technique flexibility. Only three approved instruction files are sent.

## Creative north star and October 11 audit

[Network creative charter](NETWORK_CREATIVE_CHARTER.md) defines the viewing experience: premium, cinematic, accessible entertainment with rigorously earned insight. [Creative greenlight](CREATIVE_GREENLIGHT.md) raises the bar at concept, research, outline, script and actual production stages. Every channel now also has a `CREATIVE_CONTRACT.md` defining its unique narrative pleasure, hook types, story motor and rejection tests. [The October 11 creative audit](CREATIVE_AUDIT_2026-10-11.md) examines the original eight lane definitions and six canonical scripted pilot episodes, with candid areas needing improvement. No existing script, story stage, narration selection or publishing state was changed by that audit.

## Director-owned three-file packet (current rule)
The old editor-owned visual handoff summary above is superseded. Green Knight directs story, thumbnail, first frame, cinematic opening, performance and visual narrative; the editor executes. See EDITOR_HANDOFF_STANDARD.md and DIRECTOR_PACKET_REVIEW.md. Each fully revised, individually and jointly approved video delivers exactly three editor-facing files in story/editor-packet/: 01_SCRIPT.txt, 02_NARRATION_DIRECTOR.md and 03_VISUAL_DIRECTOR.md. Working evidence, research, packaging, QA and registry remain separate. Legacy scripted episodes must pass the new gate before editor packet release.

## Operational command shortcut
See [OPERATIONS_QUICKSTART.md](OPERATIONS_QUICKSTART.md) for create → review/revise → editor delivery QA and the five agreed final deliverables. Voice Design prompts are exploratory; `narration.json` must actually be approved before a packet ships.

## Primary creative success criterion: popcorn-good
Read [POPCORN_STANDARD.md](POPCORN_STANDARD.md) at **every** channel-idea, episode-idea, research, scripting, review/revise and final-video QA gate. A novice should be riveted without homework; a veteran should still get surprising, defensible economics/strategy analysis built into a real story. Correctness and beautiful prose do not compensate for dullness. Scripts, 02 performance directions and 03 visual direction must *jointly* earn attention. The reviewer must name and structurally repair the weakest middle rather than stamp APPROVED.

## Editor sourcing, onboarding and managing the relationship
Use [Editor Onboarding & Management Playbook](EDITOR_ONBOARDING_PLAYBOOK.md) and the companion [intake record](templates/editor/EDITOR_INTAKE_RECORD.md) and [Fiverr message patterns](templates/editor/FIVERR_MESSAGES.md) when engaging a new editor, scoping a pilot, negotiating a ten-video batch, or reviewing revision terms. This is the agent's internal relationship protocol, separate from the three editor-facing episode files.

## Hard Costs (ninth channel, 2026-10-14)
The construction channel uses HC-I#### / HC-V####, 19 editorial categories, a working Industrial Editorial visual brief and unselected narrator profile. [Read its setup](channels/hard-costs/README.md). Shared evidence, story, popcorn-good and director-owned three-file packet requirements apply. It has 12 unselected **proposed ideas**, not approved video production or a public YouTube channel.

## Built to Scale (tenth channel, 2026-10-14)
Built to Scale investigates better business operations, growth, critical decisions and performance differences. It uses distinct BTS-I#### and BTS-V#### IDs and a proposed Operator's Blueprint, infographic-forward documentary visual identity. See [its workspace](channels/built-to-scale/README.md). The 12 initial ideas are proposed only; no video, narrator, editor, account or production asset is approved.

### Built to Scale growth charter update (2026-10-14)
The revised channel emphasizes how to acquire customers, hire and delegate, finance work with debt/credit/equity, win large contracts, systematize operations, open branches, acquire firms and grow without breaking. Four story formats include operator playbooks, real company histories, major growth decisions and growing pains. Read [its channel brief](channels/built-to-scale/CHANNEL.md), [company leads](channels/built-to-scale/CASE_STUDIES.md) and [producer approval plan](channels/built-to-scale/EDITOR_WORKFLOW.md). BTS-I0013–BTS-I0026 are new, proposed growth-first ideas; earlier 12 remain in history. No episodes or editor commitments are approved.

## House Money (eleventh channel, 2026-10-15)
[House Money — The Business of Housing](channels/house-money/README.md) covers homebuilders, mortgages and servicing, renters/landlords, home transactions, ownership insurance/HOAs, land-to-housing supply and newer housing business models. Unlike Hard Costs' construction project/industry economics or Built to Scale's contractor growth playbooks, House Money tracks the economic machinery behind residential property and the people who live in it. See its [seven lanes](channels/house-money/EDITORIAL_LANES.md), [creative constitution](channels/house-money/CHANNEL.md), [initial slate](channels/house-money/PILOT_SLATE.md). Proposed seeds HM-I0001–HM-I0014; no approved narrator, editor, pilot or selected episode.

## Fame & Fortune (twelfth channel, 2026-10-18)
[Fame & Fortune](channels/fame-and-fortune/README.md) is the celebrity business-entertainment lane with FF-I#### and FF-V#### identifiers. Its channel-specific runtime is **600–1,200 seconds, targeting 900 seconds**. Its priority is exceptionally clickable but evidenced celebrity money stories, with a first-15-second impact, a concrete first-45-second payoff, and a clear non-spoken A-H segment map for a 15-minute documentary. Read [hook standard](channels/fame-and-fortune/CLICK_AND_HOOK_STANDARD.md) and [script segment template](channels/fame-and-fortune/SCRIPT_SEGMENT_TEMPLATE.md). Sixteen opening ideas are **proposed only**; no selected script, voice, editor, production or publication. Shared clean spoken script and exact three editor-director handoff files still apply.
