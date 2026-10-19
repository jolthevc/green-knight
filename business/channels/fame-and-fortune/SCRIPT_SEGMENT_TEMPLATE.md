# Fame & Fortune: 15-minute episode planning and editor segment template

These timecodes are **planning estimates**, not permission to stretch or rush. Story decisions and actual playback dictate the final cut.

| Segment | Approximate time | Editorial job | Editor/narrator job |
| --- | --- | --- | --- |
| **A. Cold Open / Hook** | 00:00-00:35 | A documented, shocking-looking contrast; make the title's stakes real. | Start on strongest verified image; clipped, intrigued delivery, purposeful silence after one major line. |
| **B. The Promise** | 00:35-01:30 | Immediate partial answer, then the *bigger* question that makes the video necessary. | One memorable fact/number; clear image-to-document transition; do not add a logo intro. |
| **C. Act I: Public Image, Private Economics** | 01:30-03:20 | Only the celebrity background required to explain commercial leverage. | Limited archival montage; show public perception versus underlying ownership. |
| **D. Act II: The Bet** | 03:20-06:00 | The deal/partnership/contract, costs, constraints and alternatives. | Transition to actual headline/contract/brand; clarify what each party contributes. |
| **E. Act III: Follow the Money** | 06:00-09:00 | Explain who earns, controls, owns, dilutes, funds and takes risk; complicate easy narrative. | Simple cap table, royalty/equity/valuation graphic or cash-flow sketch; slower voice on mechanism. |
| **F. Act IV: The Catch** | 09:00-12:00 | Authentic complication, reversal, conflict or challenge. | Pivot in visual motif/music; make consequences concrete; source caution where disputed. |
| **G. Act V: The Real Outcome** | 12:00-14:15 | What the sources show happened; contrast public story with nuanced economics. | Revisit visual from A; expose decisive document and credible counterargument. |
| **H. Closer / Payoff** | 14:15-15:00 | Pay off the title promise and deliver one memorable, non-obvious commercial insight. | Slower, confident final line; final-image callback; no lengthy subscribe monologue. |

## Required section-map row for every finished script
`SEGMENT_ID | SEGMENT_TITLE | APPROX_IN | APPROX_OUT | P_START-P_END | FIRST_SPOKEN_WORDS | LAST_SPOKEN_WORDS | VIEWER_QUESTION | EARNED_PAYOFF | NEXT_BRIDGE | PERFORMANCE_INTENT | VISUAL_START-CHANGE-END | EVIDENCE_STATUS | SOUND/HOLD`

Example, **illustrative only, not a factual claim**:
`E | Who owns the upside? | 06:00 | 09:00 | P025-P039 | "The headline said..." | "...but that wasn't cash." | Did the star pocket the reported valuation? | Explain stake versus valuation | Why did the deal still create risk? | Measured on ownership numbers | press headline -> equity pie -> vested/locked shares | Needs filing | Hold after key distinction`

## Internal writing layout (NOT FOR TTS)
```text
TITLE: [selected researched title]
STORY_ID: FF-V#### (only after actual selection)
TARGET: 15:00 (acceptable final 10:00-20:00)

[A | COLD OPEN / HOOK | approximate 00:00-00:35 | NOT SPOKEN]
P001: [exact spoken text]
P002: [exact spoken text]
EDITOR: [first frame, asset, transformation, hold, music]
VOICE: [tension, emphasis, pauses]
PAYOFF: [what specific question is asked or partly answered]

[B | PROMISE / SETUP | approximate 00:35-01:30 | NOT SPOKEN]
P003: [exact spoken text]
...

[H | CLOSER / FINAL REVEAL | approximate 14:15-15:00 | NOT SPOKEN]
P0XX: [exact spoken text]
```
When canonicalizing, remove ALL internal markers, paragraph labels and director notes from `script.txt`; preserve the narration words exactly. In the final editor packet, segment headings and P anchors live in files 02 and 03, where they cannot be mistaken for spoken copy.
