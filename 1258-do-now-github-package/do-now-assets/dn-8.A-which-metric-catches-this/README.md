# Do Now 8.A: Which Metric Catches This? 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240812062/9a284776f839ae4d0b14178717d692959b0db7cc

## Goal
By the end of this five-minute warm-up you will have matched eight production failure stickies (M1–M8) to the metric family that would actually catch each one, **accuracy**, **fairness**, **drift**, **latency**, or **cost**, and discovered that several failures need metrics outside those five columns entirely: false-refusal rate, groundedness/citation coverage, and faithfulness. You will leave the board with all eight stickies placed plus one new sticky naming a metric your current dashboard is missing. The instinct being built is metric-failure matching: a monitoring plan is only as good as its coverage, and a single global accuracy score stays reassuringly green while fairness gaps, silent drift, doubling latency, and tripled token bills all go uncounted.

## Why it matters
You cannot fix what you do not measure, and government AI services fail in ways citizens notice long before a quarterly accuracy review does. Matching failures to metrics becomes defensible when learners must place, mark, or choose and then explain one decision.

**Assets:** Failure stickies M1–M8 (see `board-items.tsv`).

## Run steps 🪜
1. Open the Mural board and read failure stickies M1–M8 slowly, each describes a symptom observed in production, not a category, so your job is diagnosis.
2. Drag each sticky to the metric family that would catch it first: **accuracy**, **fairness**, **drift**, **latency**, or **cost**.
3. Place the operational ones early: M2 (p95 latency doubles after launch) belongs to latency, M5 (token cost 3× estimate) belongs to cost, and M3 (answers change week to week after a model update) belongs to drift/version stability.
4. Handle the slice failures: M1 (strong in English, poor in French) and M7 (one neighborhood far lower) need fairness/slice metrics, a global score hides both.
5. Identify the ones that fit no existing column: M4 (refusing too many safe requests → false-refusal rate), M6 (correct answers missing required citations → groundedness/citation coverage), and M8 (right document retrieved but wrong paraphrase → faithfulness).
6. Add one new sticky naming a metric missing from your own agency's dashboard, e.g. citation coverage, p95 latency, or cost per request, and add a Mural comment defending one of your placements.
7. Remote? Post placements in Zoom chat as `M1-fairness, M2-latency...` plus your missing metric, then reply to one placement you disagree with before the reveal.

## Key takeaway 💡
The metric that matters is the one matched to the failure mode, global accuracy stays green while fairness, drift, latency, cost, and faithfulness failures burn unnoticed.

## Study further 📚
- [Model evaluation: quantifying the quality of predictions, scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html), the standard reference for choosing the right metric for a task.
- [Introduction to model monitoring, Google Cloud](https://cloud.google.com/vertex-ai/docs/model-monitoring/overview), official overview of drift and skew monitoring in production.
- [What is model drift?, IBM Think](https://www.ibm.com/think/topics/model-drift), clear explainer of why model performance degrades and how to detect it.

## Common mistake to name ⚠️
Reaching for a global accuracy metric when the failure is slice-specific, cost, latency, or drift; require the metric to be matched to the failure's mechanism before the answer key is shown.

## If finished early ⏩
Name the dashboard alert threshold for your chosen metric and who gets paged when it trips.

## ⭐ Bonus (optional)
Pick the one metric your agency does not track today, false-refusal rate or citation coverage are strong candidates, draft its one-line definition and the data source it would need, and add it to the board as a new sticky.

**Solution link in master guide:** `#answer-8-a`
