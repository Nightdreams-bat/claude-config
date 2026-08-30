---
name: user-context-moldova
description: User is in Moldova; works with Moldovan (not Romanian) education/exam materials — ANCE / ance.gov.md
metadata: 
  node_type: memory
  type: user
  originSessionId: 88880533-ebd3-4f16-a815-687f4acdde3c
---

User is in the Republic of Moldova and works with **Moldovan** exam/education materials, NOT Romanian ones.

- Official source for BAC subjects is **ANCE** (Agenția Națională pentru Curriculum și Evaluare), site **ance.gov.md** — they may casually call it "ance.gov".
- Do NOT default to the Romanian `subiecte.edu.ro`. When the user says "bac" / "limba română", assume the Moldovan ANCE exam unless stated otherwise.
- ance.gov.md is frequently down; archived ANCE PDFs are recoverable via the Wayback Machine (CDX API on `ance.gov.md/sites/default/files/*`). Moldovan BAC file codes: `12_llro` = limba și literatura română (clasa 12 / BAC), `_r_`=real, `_u_`=umanist, `sb`=sesiune de bază, `ss`=sesiune suplimentară, `es`/`esant`=eșantion, `pr`=teste de exersare.

**How to apply:** Frame exam-related help around the Moldovan system. In 2026-05 helped download the full ANCE limba română BAC archive (2012–2026) to `C:\Users\darga\BAC_romana_MD`.
