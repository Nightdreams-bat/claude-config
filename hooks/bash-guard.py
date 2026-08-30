#!/usr/bin/env python3
"""bash-guard — catch dangerous shell commands before Claude Code runs them.

Ported in spirit from amosblomqvist/pi-config's bash-guard extension.

Wired as a PreToolUse hook on Bash (and PowerShell). Reads the hook JSON on
stdin. If the command matches a dangerous pattern it exits 2, which tells
Claude Code to block the call and feed the reason back to the model.

Toggle OFF:  create file  ~/.claude/hooks/.bash-guard-off   (or /guard off)
Toggle ON :  delete that file                               (or /guard on)
"""
import json
import re
import sys
from pathlib import Path

OFF_FLAG = Path.home() / ".claude" / "hooks" / ".bash-guard-off"

# (regex, human explanation). Kept deliberately conservative: block only
# things that are almost never intentional in an agent session.
RULES = [
    (r"\brm\s+(-[a-z]*\s+)*-[a-z]*r[a-z]*f|\brm\s+-[a-z]*f[a-z]*r", "recursive force delete (rm -rf)"),
    (r"\brm\s+-[a-z]*r[a-z]*\s+(/|~|\$HOME|\.)(\s|$)", "recursive delete of a top-level / home path"),
    (r":\(\)\s*\{\s*:\|:&\s*\}\s*;", "fork bomb"),
    (r"\bmkfs(\.\w+)?\b", "filesystem format (mkfs)"),
    (r"\bdd\b.*\bof=/dev/(sd|nvme|disk|hd)", "raw disk write with dd"),
    (r">\s*/dev/(sd|nvme|disk|hd)\w*", "redirect straight onto a disk device"),
    (r"\b(shutdown|reboot|halt|poweroff)\b", "power state change"),
    (r"\bgit\s+.*\bpush\b.*\s(-f|--force)(\s|$)", "git force-push"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard (discards uncommitted work)"),
    (r"\bgit\s+clean\s+-[a-z]*f", "git clean -f (deletes untracked files)"),
    (r"\bchmod\s+-R\s+0?777\b", "recursive chmod 777"),
    (r"\bcurl\b[^|]*\|\s*(sudo\s+)?(ba)?sh\b", "curl | sh (pipe remote script to shell)"),
    (r"\bwget\b[^|]*\|\s*(sudo\s+)?(ba)?sh\b", "wget | sh (pipe remote script to shell)"),
    (r"\bsudo\s+rm\b", "sudo rm"),
    (r"\bnpm\s+publish\b", "npm publish"),
    (r"\bgit\s+push\b.*\s--tags\b.*\s(-f|--force)", "force-push tags"),
    (r"\bDROP\s+(TABLE|DATABASE)\b", "SQL DROP TABLE/DATABASE"),
    (r"\bTRUNCATE\s+TABLE\b", "SQL TRUNCATE"),
]

def main() -> int:
    if OFF_FLAG.exists():
        return 0
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    ti = payload.get("tool_input", {}) or {}
    cmd = ti.get("command") or ti.get("script") or ""
    if not isinstance(cmd, str) or not cmd.strip():
        return 0
    for pattern, why in RULES:
        if re.search(pattern, cmd, re.IGNORECASE):
            sys.stderr.write(
                f"bash-guard blocked this command: {why}.\n"
                f"Command: {cmd}\n"
                "If this is genuinely intended, tell the user to run `/guard off` "
                "or to run the command themselves with the `! ` prefix.\n"
            )
            return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
