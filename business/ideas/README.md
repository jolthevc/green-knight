# Shared idea and completion log

[registry.json](registry.json) is the single editable ledger for this workspace. It covers all business channels so we do not repackage the same explanation unknowingly. The five Pretty Penny, two Money Moves, five Fallen Angels and five Changing Hands sample concepts from the earlier discussion are imported as proposed, unselected and unresearched. Dates record import, not their original proposal. No completed videos have been invented.

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

Read latest head and entire ledger. Check canonical subject + mechanism + viewer promise and aliases across every status. Allocate the next idea and story IDs independently using the selected channel.json: PP-I####/PP-V####, MM-I####/MM-V#### FA-I####/FA-V#### or DH-I####/DH-V####. Write artifacts and matching ledger entries together; append history, do not erase it. Run the validator and commit with an expected-head check. If someone changed the branch, reread and merge their state before retrying.

IDs are business-workspace identifiers; they do not imply CH registration in the older system. Configured prefixes are PP for Pretty Penny, MM for Money Moves, FA for Fallen Angels and DH for Changing Hands. New channels need their own prefix assigned at setup.

After a save, report the IDs, actual status and link. After publication, add performance.md observations without changing the original story into a different episode. New follow-ups get new IDs with related_idea_ids.

## Entry shape

This is an example shape, not a saved proposal or reserved ID:

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
