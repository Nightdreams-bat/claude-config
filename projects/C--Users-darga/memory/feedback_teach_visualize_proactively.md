---
name: feedback-teach-visualize-proactively
description: "In teach sessions, add a visual (mermaid/SVG via the visualize skill) at every node where the idea can be visualized, without waiting to be asked."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 126d05ef-61c8-4578-b2d1-77646d1cd78c
  modified: 2026-08-26T10:52:54.718Z
---

Whenever a concept in a teach session is visualizable (a structure, relationship, flow, cycle, geometry — anything nodes-and-edges or spatial), generate the visual immediately as part of teaching that node, rather than only doing it when explicitly requested.

**Why:** User said: "I want every time that is possible maybe we change the agent that we're using to use visualizations as much as possible... when it's possible you should do it instantly. You don't need me to tell you what to do." This happened after the user had to ask for a diagram (the agent-loop cycle) that the [[teach]] skill's own "consider a visual at each node" step should have triggered on its own.

**How to apply:** During Phase 3 of [[teach]] (or any explanation), for each node ask "is this a structure/relationship/geometry?" and if yes, invoke the `visualize` skill unprompted — don't wait for the user to notice a diagram is missing. Purely theoretical/logical points with no structure to show still don't need one — the bar (visualizable) hasn't changed, only the proactivity has.
