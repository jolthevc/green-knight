# Google Sheets Database Schema

**Status:** Canonical portfolio-wide standard  
**Purpose:** Define the lightweight operating database for Green Knight Holdings.

---

## 1. Database Philosophy

Green Knight uses one primary Google Sheets workbook as its structured operating database.

The Sheet should remain intentionally compact.

A field belongs in the main database only if it materially helps Green Knight:

- compare channel opportunities
- understand channel status
- choose or understand videos
- analyze performance
- allocate capital
- preserve structured learning
- connect structured records to canonical files

Large working artifacts do **not** belong in Sheets.

Research packets, outlines, scripts, packaging packets, production packets, source logs, QA records, and detailed postmortems belong in Google Drive.

GitHub contains the standards and channel definitions.

The Sheet stores the structured operating state.

The database should not become a substitute for every other system.

---

## 2. Workbook Structure

The initial workbook structure is:

```
00_CHANNELS
CH_TEMPLATE
CH001 - [Channel Name]
CH002 - [Channel Name]
CH003 - [Channel Name]
...
```

### `00_CHANNELS`

One row per channel concept or launched channel.

This includes ideas that have not yet launched so the portfolio can preserve the history of channel theses, including concepts that are rejected or killed.

### `CH_TEMPLATE`

Canonical blank video table.

When a channel is created, duplicate this tab and rename it using the channel ID and a short channel name.

Every channel tab must retain the same column schema.

### Channel tabs

One row per video.

A video can exist in the table before publication.

The row should develop with the video from idea through evaluation.

---

## 3. 00_CHANNELS Schema

The portfolio tab contains 23 columns.

### 1. `channel_id`

Stable identifier.

Example: `CH001`

The ID never changes even if the channel name changes.

### 2. `channel_name`

Current public or working name.

### 3. `status`

Current portfolio lifecycle state.

Initial allowed values:

- IDEA
- DILIGENCE
- APPROVED
- BUILD
- TESTING
- SCALE
- MAINTAIN
- HARVEST
- REPOSITION
- KILLED
- ARCHIVED

### 4. `concept`

Concise description of what the channel is.

This should be understandable without opening the GitHub channel folder.

### 5. `target_audience`

Concise description of the primary viewer.

Detailed psychology belongs in the channel's `AUDIENCE.md`.

### 6. `audience_opportunity`

Concise assessment of the size and breadth of the addressable viewer opportunity.

This may include market-size evidence where useful, but should not imply false precision.

### 7. `content_engine`

The repeatable mechanism that can generate many videos.

This is more useful than a generic category label.

### 8. `positioning`

What makes this property distinct from adjacent channels.

### 9. `economics_thesis`

Concise pre-launch or current view of why the channel can produce attractive economics.

May include advertiser quality, RPM expectations, production cost, affiliate potential, or other relevant characteristics.

Detailed economics can live elsewhere when needed.

### 10. `launch_date`

Date the channel begins publishing.

Blank before launch.

### 11. `cadence_per_month`

Current intended number of long-form uploads per month.

### 12. `subscribers`

Current subscriber count.

### 13. `monthly_views`

Current normalized recent monthly views.

Use a consistent trailing period once analytics automation exists.

### 14. `monthly_revenue`

Current normalized recent monthly revenue.

The exact revenue definition must remain consistent across channels.

### 15. `rpm`

Current relevant RPM.

Where multiple revenue sources become meaningful, document whether this is YouTube platform RPM or blended revenue per thousand views.

### 16. `monthly_cost`

Current direct recurring production and operating cost for the channel.

### 17. `contribution`

Monthly revenue less monthly direct cost.

### 18. `total_invested`

Cumulative direct cash invested into the channel.

### 19. `current_learning`

The single most important current conclusion about the channel.

This is deliberately concise.

Detailed analysis belongs in channel learnings or postmortems.

### 20. `next_action`

The most important current portfolio decision or action.

Examples:

- launch first slate
- continue testing
- increase cadence
- test broader topics
- reduce spend
- harvest
- kill

### 21. `github_path`

Canonical GitHub path for the channel definition.

### 22. `drive_folder`

Canonical Google Drive channel folder.

### 23. `narration_status`

Operational readiness of the channel narrator.

Allowed values:

- NEEDS_SELECTION
- READY
- NOT_REQUIRED

This field records whether the channel's narrator setup is operationally complete. It does **not** store provider voice IDs, model IDs, settings, or secrets.

The narrator definition and provider implementation belong in the channel's GitHub files.

---

## 4. Channel Video Tab Schema

Every channel video tab contains the same 27 columns.

The objective is to retain enough information to connect the **pre-publication hypothesis** to the **post-publication outcome** without putting entire development artifacts into Sheets.

### 1. `video_id`

Permanent identifier.

Example: `CH001-V0001`

### 2. `status`

Current state from the canonical video lifecycle.

Allowed values:

- IDEA
- SELECTED
- BRIEFED
- RESEARCHING
- RESEARCHED
- RESEARCH_REVIEW
- OUTLINING
- OUTLINED
- OUTLINE_REVIEW
- SCRIPTING
- SCRIPTED
- SCRIPT_REVIEW
- PACKAGING
- PACKAGED
- PRODUCTION_READY
- IN_PRODUCTION
- FIRST_CUT
- REVISION
- QA
- READY_TO_PUBLISH
- PUBLISHED
- MEASURING
- EVALUATED
- KILLED

### 3. `pillar`

Channel content pillar.

This allows later performance analysis by recurring editorial territory.

### 4. `topic`

The subject.

Example: `Costco gasoline`

### 5. `thesis`

What the video is actually saying or revealing.

A topic and thesis are not the same thing.

### 6. `why_this_video`

Concise rationale for why Green Knight chose to make it.

This preserves the pre-result investment logic.

### 7. `framing`

The editorial angle used to turn the topic into a story.

### 8. `working_title`

Primary title used during development.

### 9. `final_title`

Actual published title.

Preserving both helps distinguish original conception from final packaging.

### 10. `thumbnail_concept`

Concise description of the final or primary thumbnail idea.

Detailed packaging belongs in Drive.

### 11. `publish_date`

Publication date.

### 12. `runtime_min`

Final runtime in minutes.

### 13. `production_cost`

Direct variable cost of producing this video.

### 14. `impressions_30d`

YouTube impressions during the first 30 days.

This helps distinguish a distribution problem from a click problem.

### 15. `views_30d`

Views during the first 30 days.

This is the primary normalized view comparison window initially.

### 16. `ctr_30d`

Impressions click-through rate during the first 30 days.

### 17. `avg_view_pct_30d`

Average percentage viewed during the first 30 days.

This normalizes retention better across different runtimes than raw average view duration alone.

### 18. `revenue_30d`

Revenue generated during the first 30 days under the portfolio's current revenue definition.

### 19. `rpm_30d`

Relevant RPM during the first 30 days.

### 20. `lifetime_views`

Lifetime views.

### 21. `lifetime_revenue`

Lifetime revenue.

### 22. `result_class`

Contextual result classification.

Allowed values:

- BREAKOUT
- WINNER
- ABOVE_BASELINE
- BASELINE
- BELOW_BASELINE
- MISS
- TOO_EARLY

Classification should be relative to the appropriate channel baseline rather than one universal view threshold.

### 23. `primary_learning`

The single most important structured takeaway from the video.

This should normally be one concise conclusion.

The full postmortem remains in Drive.

### 24. `learning_tags`

Compact structured tags that make cross-video analysis possible.

Examples:

`recognizable-brand, hidden-economics, consumer-anchor`

Tags should be used consistently once the taxonomy matures.

### 25. `next_action`

The most important follow-up implication.

Examples:

- repeat framing
- sequel
- retest title pattern
- avoid topic class
- no action

### 26. `drive_folder`

Canonical Drive folder for the video.

This provides access to all large artifacts.

### 27. `youtube_url`

Published YouTube URL.

Blank until publication.

---

## 5. Why We Are Not Tracking More

The initial schema deliberately excludes many potentially interesting fields.

Examples:

- 24-hour metrics
- 7-day metrics
- 90-day metrics
- detailed retention timestamps
- comments
- likes
- traffic source breakdowns
- device mix
- geography
- every title candidate
- every thumbnail candidate
- full brief
- full research
- full outline
- full script
- detailed QA results
- separate what-worked and what-failed fields
- every experimental variable
- every cost component

These may become useful later.

They should be added only when Green Knight has a concrete decision or analytical workflow that needs them.

The system should avoid collecting data merely because YouTube exposes it.

---

## 6. Normalized Performance Window

The initial comparable performance window is **30 days**.

This is a deliberate simplification.

Thirty-day metrics provide enough time for meaningful distribution while avoiding a proliferation of 24-hour, 7-day, 30-day, and 90-day columns.

Lifetime views and lifetime revenue capture long-tail asset value separately.

If experience shows that early performance windows materially improve decisions, the schema can evolve.

---

## 7. Detailed Postmortems Stay in Drive

The Sheet should preserve only:

- result classification
- primary learning
- learning tags
- next action

The detailed postmortem should contain observations, baselines, interpretations, confidence, confounders, packaging analysis, retention analysis, economics, and supporting context.

This division keeps the database analytically useful without making every row unreadable.

---

## 8. Schema Consistency

Every channel tab must use the same columns in the same order.

Do not create channel-specific synonyms such as:

- thesis vs premise
- framing vs angle
- pillar vs category

If a genuinely new portfolio-wide field becomes valuable, add it to the canonical template and migrate every channel.

The portfolio's ability to learn across channels depends on a shared ontology.

---

## 9. Evolution Rule

New columns should pass a simple test:

> What recurring decision, comparison, automation, or learning becomes materially better if this field exists?

If the answer is unclear, do not add the column.

Green Knight should prefer a small database that is reliably populated over a theoretically comprehensive database filled with inconsistent or empty fields.
