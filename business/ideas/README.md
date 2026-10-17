# Shared idea and completion log

[registry.json](registry.json) is the single editable ledger for this workspace. It covers all business channels so we do not repackage the same explanation unknowingly. The five Pretty Penny, two Money Moves, five Fallen Angels, five Changing Hands, five Fool’s Gold and one Silver Spoon sample concepts from the earlier discussion are imported as proposed, unselected and unresearched. Dates record import, not their original proposal. No completed videos have been invented.

## Fields

schema_version; updated_at; ideas array. Each entry has:
- id, channel, title, aliases, subject, mechanism, viewer_promise.
- status, related_idea_ids, story_id, story_path.
- created_at, updated_at, rejection_or_block_reason, published_url, published_at.
- history: dated events with stage, note and actor.

Allowed statuses: proposed, selected, researching, researched, scripted, production_ready, in_production, published, blocked, rejected, archived.

Normal progression is proposed → selected → researching → researched → scripted → production_ready → in_production → published. Revisions can return to an earlier stage; append the reason. blocked/rejected/archived retain the last artifacts and history.

Use ISO dates or UTC timestamps consistently. Null means unknown/not applicable, never invented. A proposed entry has no story ID/path. A selected entry has a story ID/path and real metadata. A published entry needs a verified upload URL and date. Do not infer publication from delivery to the editor.

## Update protocol

Read latest head and entire ledger. Check canonical subject + mechanism + viewer promise and aliases across every status. Allocate the next idea and story IDs independently using the selected channel.json: PP-I####/PP-V####, MM-I####/MM-V####, FA-I####/FA-V####, DH-I####/DH-V####, FG-I####/FG-V####, SS-I####/SS-V####, FB-I####/FB-V#### or OTM-I####/OTM-V####. Write artifacts and matching ledger entries together; append history, do not erase it. Run the validator and commit with an expected-head check. Use EDITORIAL_REVIEW.md for explicit researched/scripted/production/published gates; never promote status from file existence alone. If someone changed the branch, reread and merge their state before retrying.

IDs are business-workspace identifiers; they do not imply CH registration in the older system. Configured prefixes are PP for Pretty Penny, MM for Money Moves, FA for Fallen Angels, DH for Changing Hands, FG for Fool’s Gold, SS for Silver Spoon, FB for First Billion and OTM for On the Map. New channels need their own prefix assigned at setup.

After a save, report the IDs, actual status and link. After publication, add performance.md observations without changing the original story into a different episode. New follow-ups get new IDs with related_idea_ids.

## Entry shape

This is an entry-shape illustration, not a new proposal. PP-I0001 is already in the live registry; allocate the next available ID rather than copying it:

```json
{
  "id": "PP-I0001",
  "channel": "pretty-penny",
  "title": "Working title",
  "aliases": [],
  "subject": "Familiar object or service",
  "mechanism": "Specific economic mechanism to explain",
  "viewer_promise": "The question the viewer will understand",
  "status": "proposed",
  "related_idea_ids": [],
  "story_id": null,
  "story_path": null,
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD",
  "rejection_or_block_reason": null,
  "published_url": null,
  "published_at": null,
  "history": [
    {
      "date": "YYYY-MM-DD",
      "status": "proposed",
      "note": "Presented in an idea batch; not yet researched",
      "actor": "ChatGPT"
    }
  ]
}
```

On selection, story_path uses a repository-relative path such as business/channels/pretty-penny/stories/PP-V0001-short-slug. Use real dates and available IDs, not the example placeholders.

## Hard Costs ninth channel
HC-I#### / HC-V####. Its first 12 examples (2026-10-14) are **proposed, unselected and unresearched** seeds, not story commissions. See channels/hard-costs/PILOT_SLATE.md, apply ordinary history/duplicate/selection gates and only allocate HC-V on owner selection.

## Built to Scale
Tenth business channel, BTS-I#### / BTS-V####. Its 2026-10-14 proposed topic bank is not fact-checked, selected or scripted. See channels/built-to-scale/EDITORIAL_FRAMES.md and PILOT_SLATE.md. Follow live global ledger selection, source/evidence, history and cross-channel deduplication protocols.

## Built to Scale growth focus (2026-10-14)
The original BTS-I0001–BTS-I0012 remain proposed for provenance, but the **current preferential topic bank** is BTS-I0013–BTS-I0026: customer acquisition, management hires, bonding/bigger contracts, working capital and credit, regional service scale, acquisitions, expansion risk and documented company histories. Their statuses are still proposed/unselected/unresearched. See channels/built-to-scale/PILOT_SLATE.md and CASE_STUDIES.md. Dedupe by mechanism against both Hard Costs and earlier BTS proposals. The shift in programming is not authority to invent selected stories or completed scripts.

## House Money eleventh channel (2026-10-15)
HM-I#### / HM-V####. Its initial 14 episode ideas are all **proposed**, unresearched and not yet selected or in production. The initial list covers the seven editorial pillars of the housing economy: homebuilding, mortgage finance, renting, home transactions, ownership costs, land/supply and new models. Read channels/house-money/PILOT_SLATE.md, CHANNEL.md and LANE_ROUTING.md before selecting. Cross-reference HC-I0006 land buildability, FA-I0033 developer collapse and other shared concepts; create a House Money episode only if the final economic question is independently distinctive.

## House Money producer shortlist (2026-10-16)
The ranked 10-topic Fiverr proposal is recorded at [channels/house-money/PRODUCER_SHORTLIST_2026-10-16.md](../channels/house-money/PRODUCER_SHORTLIST_2026-10-16.md). All are existing HM-I ideas with producer-facing title variants stored as aliases in this registry. **Deduplicate across the alias and central mechanism, not only canonical titles.** No additional HM-I IDs were minted and no stories selected.
