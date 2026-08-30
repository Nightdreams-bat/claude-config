---
name: project-kairo
description: "Kairo — local AI cold-outreach platform; GitHub repo + standalone Windows .exe"
metadata:
  node_type: memory
  type: project
  originSessionId: 14f860a7-79c4-490c-a939-09611c6ca6b1
  modified: 2026-08-29T14:05:06.874Z
---

**Kairo** (renamed 2026-08-28 from "Freight Outreach" / package `outreach` / earlier UI name "Kairos").
Local single-operator cold-email + follow-up + reply-handling tool. Cold intros, multi-touch
follow-up drip, ~24h call reminders, Claude-Haiku reply classification → drafted Calendar
invite + confirmation (nothing sends/books without an Approve click). Native desktop app
(pywebview / WebView2), Flask + CLI + Windows Task Scheduler, Excel-backed, no server.

- **Folder:** `C:\Users\darga\kairo` (rename from `freight-outreach` pending — a running handle
  blocked `mv`; user finishes it after closing the app).
- **GitHub:** https://github.com/Nightdreams-bat/kairo (renamed via `gh repo rename`).
  Author `Nightdreams-bat <222636938+Nightdreams-bat@users.noreply.github.com>` only.
  **Never add any AI/cloud co-author trailer or mention to a commit or repo file.**
- **History rewrite 2026-08-28:** `git filter-branch --msg-filter` stripped all
  `Co-Authored-By: Claude` / `Claude-Session:` lines from every commit on `main`. Stale
  `critique-overhaul` branch deleted. Backup bundle: `C:\Users\darga\kairo-backup-*.bundle`.
  **Force-push still pending** — classifier blocked `git push --force origin main`; user must run it.
- **Repo layout (post-rebrand):** `kairo/` (package) · `kairo/web/` · `tests/` (361, run
  `python -m pytest tests/`) · `docs/` (SETUP, BUILD, reply-handling-design) · `packaging/`
  (`Kairo.spec`, `build.ps1`, `START_HERE.txt`, `requirements-build.txt`) · `assets/`
  (`kairo.ico`, `icon.svg`, `banner.jpg`, `make_icon.py`) · `.claude/agents/email-copywriter.md`.
  Deleted: `STATUS.md`, `docs/TEST-RESULTS.md`, `docs/img/` screenshots, `assets/banner.svg`.
- **README** rewritten: banner `assets/banner.jpg` at top, 10-feature table matching the banner,
  no screenshots. **2026-08-28:** added "Engineering highlights" section + recruiter-facing badges
  (live CI badge, tests/python/windows/MIT); dropped the defensive `database-none` / `dashboard-offline` badges.
- **CI:** `.github/workflows/tests.yml` runs `python -m pytest -q` on `windows-latest` every push/PR (green).
- **License:** MIT (`LICENSE`), copyright holder `Nightdreams-bat`. GitHub topics set (python, flask,
  gmail-api, anthropic, pyinstaller, …).
- **Build:** `.\packaging\build.ps1` (cds to repo root, runs PyInstaller on `packaging\Kairo.spec`)
  → `release\Kairo\` (`Kairo.exe`, `_internal\`, `Source code\`, `START HERE.txt`), ~185 MB.
  CLI flags in `kairo/__main__.py`: `--web --cold --followup --reminders --replies --selfcheck`.
  Scheduled tasks renamed `Kairo_ReminderCheck` / `Kairo_ReplyCheck`; keyring services
  `kairo-oauth` / `kairo-anthropic` (existing installs must reconnect Gmail + re-enter the
  Anthropic key after this rename).
- **Gitignored (never committed):** `config.json`, `client_secret.json`, `*.xlsx`, `*.log`,
  `.dev/` (local design lab — ARCHITECTURE.md / DESIGN.md / liquid-glass spec), build output.
- **Anthropic API key ≠ Claude subscription** — paid key from console.anthropic.com, Haiku ~$0.001/reply.
- **This session's Gmail connector = `gargaundarius1@gmail.com`** (user's main; live tests use it as the "lead").
- **`.exe` rebuilt 2026-08-28** via `.\packaging\build.ps1` (self-check passed) carrying a UI
  pass: `style.css` global `zoom: 1.09` + looser spacing, themed `::-webkit-scrollbar` (green
  glass pill), auto-growing `textarea.field` (script in `base.html`), and a `?v=<mtime>`
  cache-bust on the stylesheet link (`asset_v` from `create_app`'s context processor).
- **2026-08-29: Templates tab.** All message-template editing moved OUT of Settings
  into a new Gmail-style **Templates** page (`/templates`, nav item between Send & Replies).
  Left rail = 6 message types (Cold intro, Follow-up, Reminder, Confirmation, Propose
  times, Decline reply) grouped Outreach/Meeting; right pane = subject + body/bodies +
  clickable `{{ var }}` chips + live preview (POST `/templates/preview`, real sandboxed
  `templates.render` with sample data Maria/Acme Logistics). Per-message Save (form POST →
  `?m=<key>`), client-side fade switch with dirty-guard (`confirmDialog`). Language selector
  + "reset all" live in the rail toolbar. Routes: `templates_page/_save/_preview/_language/_reset`
  in `web/app.py`; message model = `TEMPLATE_MESSAGES` list there. Files: `web/templates/templates.html`,
  `web/static/templates.js`, `/* Templates tab */` block in `style.css`. Settings now shows
  only an "Open Templates" pointer card. Tests: `tests/test_web_templates.py` (11). Suite 372 green.
  `.exe` NOT yet rebuilt. Tested against a throwaway dev `config.json` (excel_path `injected.xlsx`,
  gmail `me@example.com`) — restored to clean EN defaults after.
- **2026-08-29: Track B — GitHub-Releases installer (DONE, not yet tagged/tested live).**
  `kairo/__init__.py` now has `__version__ = "0.1.0"`. `.github/workflows/release.yml` fires on
  `v*` tag push (Windows): assert tag==`v{__version__}` → write `client_secret.json` from repo
  secret `CLIENT_SECRET_JSON` → PyInstaller → `--selfcheck` → `ISCC packaging/Kairo.iss` →
  publish GH Release with `KairoSetup-<ver>.exe` + `.sha256` (softprops/action-gh-release@v2).
  `packaging/Kairo.iss` = Inno Setup, per-user (`PrivilegesRequired=lowest`,
  `{localappdata}\Programs\Kairo`, changeable, no UAC), Desktop-shortcut task, "Launch now",
  AppId GUID `73247DE8-12BD-4C4B-96A9-774F8AF5EBEE`. `packaging/build-installer.ps1` = local
  build+compile. `Kairo.spec` conditionally bundles `client_secret.json` at archive root when
  present. **`kairo/paths.py` rewritten:** frozen builds now keep user data in `%APPDATA%\Kairo`
  (was next-to-exe); `data_dir()` caches `_DATA_DIR`, migrates old next-to-exe files once
  (`_migrate_from_exe_dir`), and seeds the bundled `client_secret.json` (`_seed_bundled_client_secret`).
  README: Install section + release badge (bumped "381 passing"). `docs/BUILD.md` expanded.
  Tests: `tests/test_release_packaging.py` (12). Suite **381 green**.
- **2026-08-29: Track A+B committed & pushed.** Commit `ef5ff78` "Add Templates tab and
  GitHub-Releases Windows installer" pushed to `origin/main` (local==origin, no force-push
  needed — earlier rewrite already in sync). Language switch in Templates tab now warns +
  replaces all templates with that lang's defaults (`templates_language` route +
  `data-confirm` form). `.exe` rebuilt via `build.ps1` — SELF-CHECK PASSED, frozen build
  correctly used `%APPDATA%\Kairo`. Tag `v0.1.0` created **locally, NOT pushed**.
  Folder rename `freight-outreach`→`kairo` still pending — **folder is still `C:\Users\darga\freight-outreach`** (git remote is `kairo`).
- **2026-08-29 (later): first release cut.** Repo secret `CLIENT_SECRET_JSON` set from local
  `client_secret.json` (Google *installed-app* OAuth client, project `freight-outreach` — app
  identity, ships in the EXE; NOT the per-user token which lives in Windows Credential Manager
  `kairo-oauth`). Tag `v0.1.0` pushed → release workflow run 33245729091 **FAILED** at
  `Kairo.exe --selfcheck`: `import googleapiclient.discovery: FAILED - No module named 'unittest'`
  — `packaging/Kairo.spec` `excludes` listed `unittest`; a googleapiclient transitive dep needs
  `unittest.mock` under the frozen loader. Fixed in commit `85cd95d` (removed `unittest` + `test`
  from excludes), verified with a local PyInstaller build (`--selfcheck` PASSED). Tag `v0.1.0`
  moved to `85cd95d` locally. **BLOCKED on user push:** classifier blocks `git push`; user must run
  `git push origin main && git push origin v0.1.0 --force`. NB self-check's "Connection checks"
  block (Gmail FAIL etc.) is cosmetic — does not affect exit code.
- **2026-08-29 (later still): no-console GUI build.** Client complained a black
  terminal flashed on launch. `packaging/Kairo.spec` now emits TWO exes from one
  COLLECT: `Kairo.exe` (`console=False`, GUI subsystem — no terminal ever) and
  `kairo-cli.exe` (`console=True`) for `--cold`/`--followup`/`--selfcheck` + CI.
  `kairo/__main__.py` `_ensure_std_streams()` routes None stdout/stderr → devnull
  so the windowed build never dies on a stray `print()`. `release.yml` self-check
  now runs `kairo-cli.exe`; `build.ps1` copies both exes; `Kairo.iss` globs
  `dist\Kairo\*` so it picks up both. Verified: local build self-check PASSED,
  launching `Kairo.exe` spawned msedgewebview2 with zero conhost. Commits
  `1b16789` + `0271e95` (version bump 0.1.0→**0.1.1**). User pushed;
  release run 33247877237 succeeded → **Release `v0.1.1` published**
  (`KairoSetup-0.1.1.exe` ~59 MB + `.sha256`).
- **2026-08-29 (later): popup-terminal + Leads/Find-leads overhaul (4 subagents, tests 382→404 green,
  NOT committed, `.exe` NOT rebuilt).** (a) New `kairo/win_subprocess.py` (`NO_WINDOW`=CREATE_NO_WINDOW,
  `run`/`popen` inject creationflags + hidden STARTUPINFO); `schedule_task.py` + `desktop.py` route all
  `schtasks`/browser spawns through it — kills the black console windows that flashed on every
  Settings open/save and Diagnostics run. (b) `ExcelStore._ensure_headers()` no longer writes on
  construction (was `_save()`-ing the user's workbook on link → `ExcelFileLocked` on every page if the
  file was open in Excel); STATE cols created in-memory, persisted on first real write. New
  `_select_sheet_with_email()` picks the sheet with an Email column, not just `wb.active`. New
  `get_config_and_store(readonly=True)` on GET pages → soft banner instead of hard error when locked.
  (c) Settings: editable `excel_path` text field (was Browse-only, tkinter). (d) Suppressed leads →
  dedicated `/leads/suppressed` page; main `/leads` hides them; shared `_leads_table.html` include.
  (e) `find_leads_autoimport` config default True: completed search auto-appends email-bearing new
  leads to the xlsx (`_run_lead_search`), no-email ones stay for manual pick; new
  `POST /find-leads/undo-import` + `ExcelStore.remove_rows()`. Settings has a "Find leads (beta)" toggle.
- **2026-08-29 (later): Leads follow-up fixes (client feedback, tests 404→414 green, NOT committed,
  `.exe` NOT rebuilt).** (a) Find-leads search bar no longer rolls back to the previous query mid-search
  — `find_leads()` now prefers `_LEADS_JOB["what/where"]` over the lagging `_LEADS_LAST`. (b) New config
  key `find_leads_limit` (default 25, clamp 5–75) + Settings "Leads per search" number field; `_run_lead_search`
  reads it and scales the enrich scrape budget (`enrich(budget_seconds=)`, new param). (c) Deleted leads
  file is NOT recreated: `ExcelStore(..., create_if_missing=False)` → new `ExcelFileMissing`; passed by
  web `get_config_and_store`/`_run_job`/`_run_lead_search` + `diagnostics._check_excel`. Only creation
  points now: `config.load_config()` first-run (`_seed_leads_file`) and an explicit Settings path change.
  New `excel_missing.html` + errorhandler; `/leads` etc. show a banner, Diagnostics shows a FAIL row.
  (d) Diagnostics change notification: new `kairo/diag_state.py` snapshots each run to
  `diagnostics_state.json` (gitignored); `/diagnostics/run` now returns `{checks, changes, previous_run}`
  and `diagnostics.html` shows a "N checks changed since last run" alert. Tests: `tests/test_leads_fixes.py`
  + 1 in `test_web_smoke.py`.
- **2026-08-29 (later still): 2nd Leads batch (client feedback, tests 414→424, NOT committed, `.exe` NOT
  rebuilt).** (a) **Notes-not-updating bug fixed**: `ExcelStore` compacted the header row, so a blank
  column anywhere shifted every later column and reads landed in the wrong cell (a Note typed in Excel
  showed blank). Now keeps real 1-based positions via `self._header_col` (built in new `_load_headers()`);
  `_row1_cells`/`_row1_headers`/`_col_for_header` reworked, `_select_sheet_with_email` only picks the sheet.
  `/leads` + `/leads/suppressed` also get `Cache-Control: no-store` (`_fresh()` helper) so a reopened tab
  never shows a stale bfcache copy. (b) Suppressed-leads page: per-row **Delete** (`POST /leads/<i>/delete`
  → `remove_rows`, confirm dialog) and **Block** (`POST /leads/<i>/block` → append email to
  `disallowed_emails`) buttons; gated by `suppressed_view` flag in `_leads_table.html`. (c) Find-leads now
  filters results through `lead_sourcing.drop_blocked(leads, emails, domains)` before AND after enrich;
  summary reports "skipped N on your blocklist". (d) Find-leads "City / region" field prefilled with
  `București` (template default, editable). Tests: `test_leads_fixes.py`, `test_web_leads.py`,
  `test_web_smoke.py`, `test_excel_store.py`. (e) **Settings** moved out of the main `<nav>` into
  `.side-foot` at the sidebar bottom-left, replacing the old "Online" dot indicator (`base.html` +
  `.side-foot` CSS simplified). **Committed + released:** commits `6f4d4d2` (feature) + `2d7240a`
  (bump 0.1.2→0.1.3) pushed to `origin/main`; tag `v0.1.3` pushed → release run 33251752410 **succeeded**,
  **Release `v0.1.3` published** (`KairoSetup-0.1.3.exe` + `.sha256`). tests.yml CI green. `git push` was
  NOT blocked this session (classifier let it through). README tests badge bumped 381→424.
- **2026-08-29 (later still): v0.1.3 regression fixes (client feedback: 3 bugs; tests 431 green,
  version 0.1.3→0.1.4).** (5) **"Excel can't be edited
  by hand"** — while the workbook is open in Excel, `_save()`'s `os.replace` raises
  `ExcelFileLocked` and every POST route dead-ended on `excel_locked.html`. Fix: new
  `writable_store()` + `_post_redirect()` helpers in `web/app.py` (applied to `toggle_suppress`,
  `delete_lead`, `find_leads_import`, `find_leads_undo_import`); the `ExcelFileLocked` /
  `ExcelFileMissing` errorhandlers now flash + redirect back on non-safe methods instead of
  rendering a dead-end page; `_sync_send_redirect` probes the store before starting a send job;
  `_run_job` shows `warning` not `danger` for locked/missing. (6) **"folder reappears after you
  delete it"** — frozen `paths.data_dir()` unconditionally `mkdir`-ed `%APPDATA%\Kairo` at import,
  and the hourly `Kairo_ReminderCheck` / `Kairo_ReplyCheck` tasks re-import the package. Fix:
  `data_dir()` is now pure path resolution; new `ensure_data_dir()` does the mkdir+migrate+seed and
  is called only from real write entry points (`kairo/__main__.py`); `--replies`/`--reminders`
  early-out with a print when `CONFIG_PATH` is absent (`_is_configured()`); `config.save_config`
  mkdirs its parent on demand; `logging_setup` uses `delay=True` + best-effort parent mkdir. Also:
  Settings "Save path" only creates the file when the path **actually changed** (was: whenever the
  candidate didn't exist, so re-saving the prefilled path rebuilt a just-deleted file). (7) **"can't
  import leads"** — same dead-end as bug 5 for a missing/locked configured path. Fix: covered by
  the `writable_store()` helper; `find_leads_import` redirects to `/find-leads` keeping
  `_LEADS_LAST` intact for a retry; `_run_lead_search` sets `_LEADS_JOB["write_blocked"]` and
  `find_leads` GET flashes the summary. Tests: `test_main_entry.py` (new), `test_web_leads.py`,
  `test_web_settings.py`, `test_web_smoke.py`, `test_release_packaging.py`. Plan file:
  `C:\Users\darga\.claude\plans\lazy-churning-lobster.md`. **Committed + released:** commits
  `27849dc` (fix) + `62019fe` (bump) on `origin/main`; tag `v0.1.4` → release run 33253533948
  **succeeded**, **Release `Kairo 0.1.4` published** (`KairoSetup-0.1.4.exe` + `.sha256`).
  tests.yml green. README badge 424→431.
- **2026-08-29 (later still): v0.1.5 — empty-workbook / "couldn't read headers" fix. RELEASED.**
  Client log (0.1.4) showed `excel_store: Couldn't read headers from ...Book 7.xlsx: tuple index out
  of range` ×20 — operator kept making blank `.xlsx` files by hand in Excel on the Desktop and linking
  them; a sheet with no header row broke `sheet_headers()` AND left `add_lead()` with nowhere to write
  (→ "Added 0, skipped 15 (duplicates / no email)"). Fixes: `sheet_headers()` reads row 1 via
  `iter_rows` (empty → `[]`, no error); `ExcelStore._ensure_data_headers()` seeds `DATA_COLUMNS` when
  the sheet has none (also repairs STATE-only sheets); `ExcelStore.initialize()` persists a pending
  header row; Settings "Save path" initializes an existing-but-empty file on link; Find-leads only
  imports email-bearing leads (no-email rows show "no email found" tag, not a checked box) and the
  import summary splits "already in your sheet" / "no email address" / "Kairo couldn't write".
  Product decision (user): do NOT let no-email leads import. Commits `684cfb3` (fix) + `ea6912a`
  (bump 0.1.4→0.1.5) on `origin/main`; tag `v0.1.5` → release run 33254790607 **succeeded**,
  **Release `Kairo 0.1.5` published** (`KairoSetup-0.1.5.exe` + `.sha256`). tests.yml green.
  README badge 431→434. Local `.exe` also rebuilt via `build.ps1` (SELF-CHECK PASSED).
  `git push` NOT blocked. Tests: `test_excel_store.py`, `test_web_leads.py` (434 total).
- **2026-08-29: v0.1.6 — manual-Excel-edit not reflected / lost + nicer delete confirm. RELEASED.**
  Client: types Notes by hand in the .xlsx, saves, Leads page doesn't show them. Root causes &
  fixes in `kairo/excel_store.py`: (a) a store loaded earlier (hourly reminder/reply batch, or a
  long request) would `_save()` its stale in-memory copy over the operator's fresh edits →
  **silent data loss**. Now records a disk signature (`st_mtime_ns`, size) at load; `set_value` /
  `add_lead` / `remove_rows` call `_sync_if_changed()` → `refresh()` (re-reads workbook) when the
  file changed underneath. `__init__` tail split into `_read_from_disk()`. `_save()` refreshes the
  sig after writing. (b) `_row1_cells` now `.strip()`s header text so `"Notes "` from Excel maps to
  logical `Notes`. Web: `/leads` + `/leads/suppressed` pass `synced_at`; `_leads_table.html` shows
  "synced HH:MM:SS · reload from file" and auto-`location.reload()`s when the tab regains focus
  after >2s hidden. Delete-lead confirm now uses the in-app `confirmDialog` modal (base.html) via
  `data-confirm`/`data-confirm-title`/`data-confirm-ok`, not the native "127.0.0.1 says" box.
  Tests: `test_excel_store.py` (merge-preserves-note, trailing-space header) — **436 total**.
  Commits `05556b6` + `df903f7` (bump 0.1.5→0.1.6); tag `v0.1.6` → release run 33255674946
  **succeeded**, **Release `Kairo 0.1.6` published**. tests.yml green. README badge 434→436.
- **2026-08-29: v0.1.7 — "mailto:" emails + "delete looks broken". RELEASED.** Client screenshot: 6
  Leads rows all showing `mailto:osibgn@gmail.com`, and deleting/suppressing "does nothing". Findings:
  (1) delete/suppress **work correctly** (verified via web test client) — the confusion is identical
  email on every row + blank names + suppressing-then-deleting-from-suppressed-page leaves the
  `/leads` count unchanged (row was already hidden). (2) Real bug: `mailto:` prefix (copy-pasted /
  scraped from `mailto:` hrefs) shown verbatim, counted as its own address, would be emailed. Fixes:
  new `lead_fields.clean_email()` (strips `mailto:`, `<>`, `?subject=`, list tail); `valid_email()`
  runs it first; `ExcelStore._read_row()` returns the cleaned address (client's cell left as typed);
  `ExcelStore.rows()` now skips rows whose email is invalid *after* cleaning (logged, still shown on
  Leads with a "check address" chip via `email_ok` flag in `_lead_rows`); delete/block use
  `_post_redirect()` to land back on the page you were on. Commits `6cb8b96` + `b3c725e` (bump
  0.1.6→0.1.7); tag `v0.1.7` → release run 33256505692 succeeded, **Release `Kairo 0.1.7` published**.
  tests.yml green. Tests: `test_lead_fields.py` (clean_email table), `test_excel_store.py`
  (mailto read, invalid-email skip) — **447 total**. README badge 436→447.
- **2026-08-29 (superseded by v0.1.5 above): "blank sheet → all leads skipped as duplicates" fix.** Client linked a hand-made empty `.xlsx` (no headers); it has
  no Name/Email column so `ExcelStore.add_lead()` had nowhere to write → returned None for every
  lead → import flashed "skipped N (duplicates / no email)". Fixes in `kairo/excel_store.py`: new
  `_ensure_data_headers()` (called in `__init__` before `_ensure_headers`) seeds `DATA_COLUMNS` when
  the sheet has zero client columns (also recovers files already broken into STATE-only); new
  `initialize()` persists a pending header row. `web/app.py`: Settings save-path now calls
  `ExcelStore(...).initialize()` when linking an existing-but-empty file; `find_leads_import` splits
  the skip count into "already in your sheet / no email / Kairo couldn't write" instead of the
  misleading "duplicates / no email". Tests in `test_excel_store.py`.
- Default email templates (`kairo/templates.py`) are freight-broker copy, RO-primary
  (`template_language`, formal `dumneavoastră` + diacritics); English pinned by `test_templates.py`.
  `email-copywriter` subagent maintains this copy.
