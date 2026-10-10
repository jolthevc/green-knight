# Source and claim map

Template: replace all placeholders. URLs alone are not a claim audit.

## Sources
| Source ID | Publisher / title | URL | Published / accessed | Relevant page/section | Source class | Access status / limitations |
| --- | --- | --- | --- | --- | --- | --- |

Use S001 etc. Mark opened, partial, paywalled or lead_only honestly. A lead_only source cannot be the sole support for a consequential claim.

## Claims
| Claim ID | Exact claim / calculation | Script paragraph + exact anchor | Source IDs | Period / scope | Verified / inference / illustrative | Caveat / editorial handling |
| --- | --- | --- | --- | --- | --- | --- |

Use C001 etc. Paragraph IDs follow script.txt blank-line paragraphs P001 etc. Update anchors after revisions. Support consequential facts, figures, quotes and causal assertions. Track numbers rounded for speech against the exact source value.

## Adversarial check
What would an informed skeptical viewer dispute? Which authoritative sources disagree? Which assertions were removed because they could not be supported?

## Freshness check
Record research date and which facts need rechecking immediately before production/upload.

## Canonical structured map
Populate evidence.json for sources, claims and scene/paragraph references. It owns the IDs, script hash/version and source access status. This document is the readable review of that map; keep it consistent instead of operating a second source ledger.

Source records: id, publisher, title, url, accessed_at, locator and access_status (opened / partial / lead_only). Claim records: id, paragraph_id, exact opening anchor, claim, source_ids, status (verified / inference / illustrative) and basis. Scene records: id, paragraphs (paragraph_id + opening anchor pairs), purpose, evidence_type (illustration / document / data / reconstruction) and source_ids. Document/data scenes require supporting sources. Cover every spoken paragraph with a scene.
