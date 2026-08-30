#!/usr/bin/env node
/*
 * custom-header / statusline — the "big Pi" header, adapted for Claude Code.
 *
 * Claude Code feeds this script a JSON blob on stdin every time the status
 * line refreshes. We print ONE line. ANSI colour is fine; keep it short.
 *
 * Ported in spirit from amosblomqvist/pi-config's custom-header.ts.
 */
let raw = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", (d) => (raw += d));
process.stdin.on("end", () => {
  let s = {};
  try { s = JSON.parse(raw); } catch (_) {}

  const C = {
    reset: "\x1b[0m", dim: "\x1b[2m", bold: "\x1b[1m",
    cyan: "\x1b[36m", green: "\x1b[32m", yellow: "\x1b[33m",
    magenta: "\x1b[35m", grey: "\x1b[90m", red: "\x1b[31m",
  };

  const model = (s.model && (s.model.display_name || s.model.id)) || "Claude";
  const dir = (s.workspace && (s.workspace.current_dir || s.workspace.project_dir)) || process.cwd();
  const shortDir = dir.replace(/^.*[\\/]/, "") || dir;
  const branch = (s.workspace && s.workspace.git_branch) || s.git_branch || "";
  const style = (s.output_style && s.output_style.name) || "";

  // cost / usage — field names vary by version; probe a few.
  const cost = s.cost || {};
  const usd = cost.total_cost_usd ?? cost.total_cost ?? s.total_cost_usd;
  const addLines = cost.total_lines_added ?? 0;
  const delLines = cost.total_lines_removed ?? 0;
  const ctxPct = s.context && typeof s.context.used_pct === "number" ? s.context.used_pct : null;

  const parts = [];
  parts.push(`${C.magenta}${C.bold}Π${C.reset}`); // Π
  parts.push(`${C.cyan}${model}${C.reset}`);
  parts.push(`${C.green}${shortDir}${C.reset}${branch ? `${C.grey}:${C.reset}${C.yellow}${branch}${C.reset}` : ""}`);
  if (style) parts.push(`${C.grey}${style}${C.reset}`);
  if (typeof usd === "number") parts.push(`${C.grey}$${usd.toFixed(2)}${C.reset}`);
  if (addLines || delLines) parts.push(`${C.green}+${addLines}${C.reset}/${C.red}-${delLines}${C.reset}`);
  if (ctxPct != null) parts.push(`${C.grey}ctx ${Math.round(ctxPct)}%${C.reset}`);

  process.stdout.write(parts.join(`${C.grey} │ ${C.reset}`));
});
