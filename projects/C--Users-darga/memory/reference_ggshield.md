---
name: reference-ggshield
description: ggshield (GitGuardian secret scanner) install on this machine + the scan-before-publish skill
metadata: 
  node_type: memory
  type: reference
  originSessionId: 63040f03-8b56-4597-a804-a868a057acd7
  modified: 2026-08-27T11:17:58.043Z
---

ggshield 1.54 installed via `pip install --user ggshield` (Python 3.12). The
working command is **`ggshield-py`** (shimmed into `C:\Users\darga\.local\bin`);
the plain `ggshield.exe` is broken because pip doesn't ship the co-located
bundle it expects. Fallback: `python -m ggshield`.

Auth token is global, stored once via `ggshield-py auth login` (browser) or
`--method oob`. Check with `ggshield-py api-status`.

Skill **[[scan-before-publish]]** (`~/.claude/skills/scan-before-publish/`) runs
`secret scan repo .` + `secret scan path -r .` and reports leaks. Use before
pushing/open-sourcing [[project-freight-outreach]].
