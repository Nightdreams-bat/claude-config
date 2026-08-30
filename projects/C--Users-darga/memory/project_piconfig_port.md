---
name: project_piconfig_port
description: "The user's Claude Code setup ports amosblomqvist/pi-config features; what exists and where"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32d02333-0d46-4e9d-8d86-e97fc9d01a47
  modified: 2026-08-27T10:13:13.808Z
---

On 2026-08-27 we ported the base [amosblomqvist/pi-config](https://github.com/amosblomqvist/pi-config) feature set (from "Pi Setup After 6 Months", Eero Alvar) into this user's Claude Code config. The user already runs the `learn` system (teach/tutor/visualize skills).

Built:
- `~/.claude/hooks/bash-guard.py` + PreToolUse hook in `settings.json` — blocks dangerous shell commands. Toggle via `~/.claude/hooks/.bash-guard-off` or `/guard on|off|status`. Matches substrings anywhere in the command (incl. quoted text) — false positives are expected, that's the safety tradeoff.
- `~/.claude/statusline.js` — the "Π" custom header / statusline.
- Slash commands (pi's "prompt-snippets"): `/concise` `/careful` `/no-comments` `/plan-first` `/tdd` `/guard`.
- Skills: `analyze-sessions` (Python, reads `~/.claude/projects/**/*.jsonl`), `youtube-transcript` (yt-dlp), `web-debug` (playbook).
- Native equivalents documented, not built: web-fetch→WebFetch, web-search→WebSearch, ask-user-question→AskUserQuestion, browser→claude-in-chrome MCP, pdf-reader→Read, observational-memory→this memory dir, interactive-subagents→Agent/fork.

Manual: dark-mode HTML artifact generated for the user.

**Why:** user asked to replicate the video's setup for themselves.
**How to apply:** when extending this, keep the copy-a-piece philosophy; don't bundle.
