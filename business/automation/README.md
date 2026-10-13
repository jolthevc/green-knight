# Green Knight automation integration

This directory defines the contract for a single shared workflow per function, routed dynamically by channel slug and canonical IDs. It is a specification for n8n and the lightweight console, **not a claim that n8n or the console has been deployed**.

Read in order:
1. `business/AGENTS.md`, `business/WORKFLOW.md`, `business/POPCORN_STANDARD.md` and channel-specific rules.
2. [AUTOMATION_CONTRACT.md](AUTOMATION_CONTRACT.md) for noninteractive execution, gates and concurrency.
3. [JOB_SCHEMA.json](JOB_SCHEMA.json) and [PRODUCTION_SCHEMA.json](PRODUCTION_SCHEMA.json) for example validated record shapes.
4. [API_CONTRACT.yaml](API_CONTRACT.yaml) for the console/backend interface.
5. [EXPORT_MANIFEST.md](EXPORT_MANIFEST.md) for handoff packaging.

GitHub is canonical for editorial output. A small durable queue/state backend is required for reliable asynchronous jobs; Google Drive is for large production assets. Credentials stay on a server, not GitHub Pages. Production QA and actual listening/viewing remain independent approval gates.

Implementation sequencing: provision state and secure API, implement one-channel end-to-end execution, run validators, verify write-safe two-channel batch, then editor intake, calendar and analytics. No automatic Fiverr actions, payments, uploads or publication.
