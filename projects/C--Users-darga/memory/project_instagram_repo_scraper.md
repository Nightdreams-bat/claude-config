---
name: project_instagram_repo_scraper
description: Tool that scrapes Instagram accounts posting GitHub repos into a searchable Excel file
metadata: 
  node_type: memory
  type: project
  originSessionId: 90dfadd0-13bd-441f-9d33-275f1ea95fea
  modified: 2026-08-29T08:13:07.604Z
---

Located at `C:\Users\darga\instagram-github-repos\`. Scrapes IG accounts **gittrend.io**
and **marc.kaz** (both showcase open-source GitHub projects) into `github-repos.xlsx`
(one row per repo, GitHub-API-enriched: stars, language, topics, last-updated, archived).

Built 2026-08-29. Pipeline: `harvest.py` (Instagram private web API `/api/v1/feed/user/<id>/`
+ Chrome cookies via browser_cookie3) → `make_ocr_montages.py` → fill `raw/ocr_results.json`
by reading the montages with vision (gittrend hides the repo URL inside the post image;
marc.kaz puts it in the caption) → `build_dataset.py` (enrich + dedupe + write xlsx/csv).

Key gotcha: IG `web_profile_info` rate-limits fast (429) so numeric user IDs are hard-coded
(gittrend.io=14603871140, marc.kaz=173823625). instaloader got blocked; the v1 feed
endpoint from a logged-in session works. GitHub enrichment uses `gh auth token`.

First run: 252 unique repos from ~260 repo-posts, 7 on both accounts.
