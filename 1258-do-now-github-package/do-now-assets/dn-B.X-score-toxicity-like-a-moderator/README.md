# Do Now B.X: Score Toxicity Like a Moderator 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240820053/24834b9fd44bd04eddb7749c2a3f9453804164bf

## Goal
By the end of this five-minute warm-up you will have scored four phrase stickies (P1–P4) on a 0–3 toxicity rubric, 0 fine, 1 rude, 2 abusive, 3 threatening, the way a human content moderator would. You will place each sticky at its score on the Mural board, compare with a neighbor, and mark the one phrase whose score depends most on context. The artifact is your four placements plus one visible comment explaining what context would change a score. The instinct this builds is the human judgment behind moderation tooling: automated scorers produce numbers, but people define what the numbers mean and where the escalation line sits, and that is exactly the judgment you will need when your agency buys or supervises one of those tools.

## Why it matters
Automated moderation tools output scores, but humans define the rubric, the thresholds, and the escalation rules. Practicing the judgment by hand, placing, marking, choosing, and then defending one decision, makes you a better buyer and supervisor of those tools.

**Assets:** Phrase stickies P1–P4 + 0–3 rubric (see `board-items.tsv`).

**🧩 Pattern watch:** Design pattern, **Rubric-based moderation**: a 0 to 3 scale with an escalation rule for the top score. Anti-pattern, **Moderation by gut feel**: borderline calls that change with the reviewer.

> ℹ️ **Good to know:** The Perspective API, built by Jigsaw (a Google unit), launched in 2017 to score comment toxicity for publishers. It remains one of the most widely used production moderation models. Your 0 to 3 rubric is the human version of the same task, context problems included. (Source: [Perspective API](https://perspectiveapi.com))

## Run steps 🪜
1. Open the Mural board linked above and find the phrase stickies P1–P4 and the 0–3 rubric: 0 = fine, 1 = rude, 2 = abusive, 3 = threatening.
2. Read each phrase slowly: P1 "You are stupid," P2 "This relationship sucks," P3 "You are acting like a jerk," P4 "I know where you live."
3. Drag each sticky onto the rubric column matching your score, or add a comment with your score as `P# = score`. Remote? Post one line in Zoom chat, e.g. `P1=2, P2=1, P3=1, P4=3`.
4. Compare scores with a neighbor or the room: find one phrase where you disagreed and hear the other argument, P1 between friends and P4 meant as a joke are the classic disagreements.
5. Mark the one phrase whose score depends most on context (who said it, to whom, how often) with a Mural comment explaining what context would move your score up or down.
6. Note which phrase you would escalate to a human or safety process regardless of the debate, P4 "I know where you live" is the case where a possible threat overrides any joking intent.

## Key takeaway 💡
Moderation scores are judgments about context and pattern, not just words, "I know where you live" can be a joke between friends or a genuine threat, which is exactly why automated toxicity scores always need a human escalation path.

## Study further 📚
- [Perspective API, Jigsaw / Google](https://perspectiveapi.com/), the widely used free API that scores comment toxicity, the automated counterpart to this exercise.
- [toxic-bert model card, Hugging Face](https://huggingface.co/unitary/toxic-bert), a documented open toxicity classifier, showing how models are trained and labeled for this task.
- [What is content moderation?, IBM Think](https://www.ibm.com/think/topics/content-moderation), overview of human and automated moderation approaches and where each breaks down.

## Common mistake to name ⚠️
Scoring by gut feel without referencing the rubric. Require at least one score to be defended against the 0–3 definitions, not "it feels like a 2", before comparing answers.

## If finished early ⏩
Add one edge case of your own, a phrase whose score would flip entirely with context, and explain the flip in one Mural comment.

## ⭐ Bonus (optional)
Write a fifth phrase P5 from your own agency's domain (for example, a heated constituent comment) on a fresh sticky, score it against the rubric, and add one comment predicting whether an automated scorer would likely agree with you.

**Solution link in master guide:** `#answer-b-x`
