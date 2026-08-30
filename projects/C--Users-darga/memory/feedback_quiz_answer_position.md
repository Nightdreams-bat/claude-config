---
name: feedback-quiz-answer-position
description: "When running graded quizzes (teach/tutor skills) via AskUserQuestion, randomize which option holds the correct answer — don't default to always listing it first."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 126d05ef-61c8-4578-b2d1-77646d1cd78c
  modified: 2026-08-26T10:12:14.315Z
---

Never place the correct answer in the same position (especially always first) across quiz questions in a graded quiz (teach skill Phase 1a/3, tutor skill). Vary it — sometimes first, sometimes last, sometimes middle.

**Why:** User caught that across a batch of AskUserQuestion quiz questions, the correct answer was option 1 every time. A learner (or the user themselves) can notice the pattern and pick "first option" without engaging with the content, which defeats the purpose of a diagnostic quiz — it stops measuring understanding.

**How to apply:** Any time building an AskUserQuestion call that is a graded quiz (not an open fork), consciously shuffle which index holds the correct answer before sending. This applies across a single batch of parallel questions too — don't let all of them land on the same position.
