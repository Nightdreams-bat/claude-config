---
name: project-kairo-google-oauth
description: "Kairo's Google OAuth strategy — per-client Cloud projects to dodge the CASA security audit"
metadata: 
  node_type: memory
  type: project
  originSessionId: c74d4952-8589-4832-adf0-846485303f55
  modified: 2026-08-29T20:10:56.477Z
---

Kairo ([[project-kairo]]) requests the **restricted** scope `gmail.readonly` (reads lead replies),
plus sensitive scopes `gmail.send`, `calendar.events`, `calendar.freebusy`. The restricted scope is
what forces Google's paid third-party security audit (CASA) for full verification.

**Decision (2026-08-29): Path 2 — each client runs their OWN Google Cloud project.**
Client is the project owner → no 100-user cap, no CASA audit, no 7-day token expiry. They publish
their project to production and click through the one-time "Google hasn't verified this app →
Advanced → Go to Kairo" screen. **Why:** user explicitly refuses the CASA audit; Path 2 is the only
route that's free, unlimited, and permanent.

Paths considered and rejected: Path 1 (publish the shared bundled client unverified — works but 100-user
cap + Google may still restrict `gmail.readonly` + needs a hosted privacy policy); Path 3 (drop
`gmail.readonly`, read replies via IMAP+app-password instead → standard verification with no CASA —
kept as a possible v0.2 direction if scaling past ~100 brokers).

**Shipped in v0.1.9** (commit `5ac7704`): `kairo/google_client.py` + Settings → Gmail account →
"Advanced — use your own Google project" (upload/paste `client_secret.json`, validated as a Desktop-app
client, installed to `paths.CLIENT_SECRET_PATH`, connection invalidated). Config flag
`google_client_is_custom`. Guide: `docs/own-google-project.md`.

- The bundled OAuth client's Google Cloud project is still literally named **"freight-outreach"**
  (project ID); the OAuth **consent screen display name** was renamed to **Kairo** by the user 2026-08-29.
  It's in **Testing** publishing status → hard-blocks any non-test-user with `403 access_denied`.
- Client accounts seen in testing: `goddgd5@gmail.com` (the user's account — owns the per-client
  projects, is every consent-screen contact email), `dar.gar.md@gmail.com` (test lead),
  `mt.office.broker@gmail.com` (the first real client).

**Per-client project fixed values (same every client):** app name `Kairo`; all email fields
`goddgd5@gmail.com`; home page `https://nightdreams-bat.github.io/kairo/`; privacy policy
`https://nightdreams-bat.github.io/kairo/privacy.html`; authorized domain `nightdreams-bat.github.io`;
OAuth client type **Desktop app**; publish to production but NEVER submit for verification.
The privacy/landing site is `docs/index.html` + `docs/privacy.html` on the kairo repo, served by
GitHub Pages (main `/docs`, enabled 2026-08-29, commit `92cc3ec`) — shared across all clients.

**First client — MT Office Broker — project `kairo-mt` (number 599816608916): DONE through step 5.**
APIs enabled, consent screen configured, **published to production**, Desktop OAuth client
"Kairo desktop client" created. Its `client_secret.json` is at
`C:\Users\darga\Downloads\client_secret_kairo-mt.json`. Full chain was live-tested on the user's
machine (upload via Settings→Advanced → Connect Gmail as goddgd5 → diagnostics all green → cold
email sent through kairo-mt), then the machine was reset back to the bundled shared client so
`kairo-mt` stays at 0 users for the real client.

**Runbook artifact** "Kairo Client Onboarding": https://claude.ai/code/artifact/76bafeec-2930-4a2f-a4ff-bbab21d2827c
