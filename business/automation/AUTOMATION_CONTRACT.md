# Shared automation execution contract (v1)

## Scope and routing
One workflow per function, **never eight copies**: (A) generate ideas, (B) produce selected episodes including review/revise/re-review, (C) export packets, (D) production/status tracking, (E) delivery QA, (F) schedule/runway calculation. Channel routing is resolved from the live `business/channels/*/channel.json` and `business/ideas/registry.json`. Treat ids as opaque mapped via configuration and registry; reject unknown or ambiguous aliases. Never embed creative rules in n8n.

## Human decisions and noninteractive execution
The owner chooses which ideas to develop. Once authorized, production automatically completes research, evidence, synthesis, entire spoken script, complete working narration and visual directors, independent reviews of all three and integration, justified revision, re-review, validation and safe release. Do not ask for routine intermediate approvals. Final packet handoff to an editor, final film approval, scheduling and publishing remain owner decisions. For a job that cannot verify claims, fails editorial review, lacks a selected approved narrator, or cannot validate, report `blocked` with actionable reason, **not** `completed`. Do not invent external access, approved voices, video inspection or quality verdicts. Limit revision loops (default three full iterations); unresolved failure is blocked for a human.

## Canonical editorial gates
Follow `business/AGENTS.md`, `WORKFLOW.md`, `POPCORN_STANDARD.md`, selected channel's complete rules and `EDITOR_HANDOFF_STANDARD.md`/`DIRECTOR_PACKET_REVIEW.md`. Deduplicate against the full registry across all statuses and channels. Record verified sources and contrary evidence. One episode's final `editor-packet/` contains exactly `01_SCRIPT.txt`, `02_NARRATION_DIRECTOR.md`, `03_VISUAL_DIRECTOR.md`; release only after script exactness/hash, director alignment, independent review, integrated re-review and `business/tools/validate.py` succeed. Editorial audit files remain elsewhere. Package-ready is a separate gate from `scripted` and from video-final approval. Treat previously scripted work as NOT automatically packet-ready.

## Idempotency, checkpoints, concurrency
- Require caller-supplied `Idempotency-Key` for all mutating API operations; bind key to the immutable normalized request payload, reject same key with a different payload. Return existing job for duplicates.
- Issue stable `job_id` and `batch_id` values. Persist job state/stage/attempt/error/inputs/outputs/checkpoint on every durable boundary. Never depend on the lifespan of one n8n webhook execution.
- One active production job per story ID. Lease jobs with expiry and a fencing token. A worker must compare token before committing artifacts; expired leases cannot write.
- Serialize allocation of sequential idea and story IDs, and commits to shared `registry.json`, or perform optimistic head-SHA compare/retry that re-reads and merges intervening changes. A retry must reuse reserved IDs; it must not allocate again.
- On GitHub conflict reread latest branch and ledger; merge only the job's own changes and rerun checks. Never force push or overwrite approved work. Persist script hash and source commit; reject stale downstream packets.
- Resume at the last verified checkpoint using immutable input/commit refs; stage outputs are content-addressed/versioned. Do not rerun paid AI tasks unnecessarily. Clear errors and manual retry are supported.
- Allowed job states: queued, running, blocked, failed, completed, cancelled. Stages are distinct and independently recorded (researching, scripting, directing, reviewing, revising, validating, packaging). A transport success is not an editorial pass. Cancellation must not revert already committed records.

## Ownership, statuses and files
The current registry keeps its established enum (`proposed`, `selected`, `researching`, `researched`, `scripted`, `production_ready`, `in_production`, `published`, `blocked`, `rejected`, `archived`). Do not add UI-only statuses to that enum. Operational stage/job status is separately persisted; `packet_ready`, `with_editor`, `revision_requested`, `final_edit_approved`, `scheduled` are separate operational states. `published` requires actual date and verifiable URL; scheduled date never implies published. Use `PRODUCTION_SCHEMA.json` for the operational record. Avoid write-hot shared files for parallel job checkpoints.

GitHub stores originals and editorial history. Drive stores derived PDFs/ZIPs, editor drafts, final MP4, thumbnail, SRT, audio. Reference files by Drive IDs/URLs and verified hashes where feasible. Do not commit large binaries to GitHub. User-visible exports must show version and source hash; regenerate when canonical source changes.

## Failure / acceptance
Failed web research, unavailable model/Drive credentials, missing approved voice or validators: blocked/failed with explicit next action. Preserve any valid interim artifacts and source attribution. Production worker cannot self-certify actual vocal performance or rendered video. Delivery QA follows `business/DELIVERY_QA_STANDARD.md` and reports exactly what was inspected. No automatic messages to editors, acceptance of gigs, payments or publication.

## Scheduling
One video per week **per channel** is the initial configurable target, not a promise or automatic publication. Compute 4/8/12-week slot gaps and ready inventory from final-edit-approved and validly scheduled unpublished records; editor drafts and mere scripts do not count. Schedule edits are explicit user actions.
