---
name: project_claude_checkup
description: "claude-checkup skill — 3-phase audit/plan/repair of the local Claude Code config + credit usage, approval-gated"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6ca28523-a36e-4607-9054-4ab1f2809cfe
  modified: 2026-08-29T10:02:16.033Z
---

Built 2026-08-29. `/claude-checkup` runs a 3-phase performance review of `~/.claude/`:

1. **Audit** — `config-auditor` agent (Sonnet, read-only, the orchestrator) grades each
   area A/B/C/F against `references/rubric.md`, returns a tier chart + ranked remediation
   plan. Each plan row tagged `mechanical` (Haiku-safe) or `judgment` (Sonnet).
2. **Approval gate** — user picks which plan items to apply; nothing happens otherwise.
3. **Apply + verify** — `config-fixer` agent (Haiku by default, Sonnet for judgment items;
   one item per run, routes content never deletes) applies approved items, then
   `config-verifier` agent (Sonnet, read-only) confirms each landed, JSON/frontmatter
   valid, pointers resolve, and re-grades.

Hard rule in the rubric: if any always-loaded file (CLAUDE.md, MEMORY.md) is oversized or
holds situational detail inline, plan item #1 is **always** "convert to an index" (pointers
in the loaded file, detail routed to docs/ or a skill) — the biggest token/credit saving.

Credit rollup uses the existing `analyze-sessions/scripts/analyze.py` called directly
(that skill is `off` in skillOverrides — override only blocks model-invocation).
Related: [[project_piconfig_port]].

Published 2026-08-29 as a public repo: **github.com/Nightdreams-bat/simple-claude-audit**
(MIT). The repo version is portable (`~/.claude/...` paths) and bundles its own copy of
`analyze.py` under `skills/claude-checkup/scripts/`. The user's local install keeps the
absolute `C:\Users\darga\...` paths and points at the separate analyze-sessions skill.
Keep the two in sync when the skill changes. No NIGHT/ASCII attribution anywhere (removed
2026-08-29) — repo has a `assets/banner.png` header only; keep it clean/minimal.

First run (2026-08-29, pre-3-phase version): overall ~C — 0 HIGH / 4 MED / 3 LOW. Main
issues: web-debug disabled but Chrome tools heavily used; bulk OCR/scrape on Sonnet not
Haiku; Kairo memory file bloated to 89L with transient state; marathon sessions.
