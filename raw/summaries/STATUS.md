# Summary Integration Status

Tracks which summaries have been integrated into the wiki.
Agents should read this file before running any pipeline stage to avoid reprocessing.

**Per-summary stages**: `facts_done` → `routed` → `written` → moved to `integrated`.
Crashed runs resume from each summary's last completed stage.

---

```yaml
integrated: []

in_progress: []

pending: []
```
