# Do Now 8.C: Critique This Dashboard 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240814055/e94decc67aac698205c9bc605390a24096b76f78

## Goal
Critique a sample government dashboard, "Service requests resolved by month," by posting three red stickies (one thing misleading, one thing missing, one thing unclear) and one green sticky naming what is genuinely useful, then vote on the single worst issue.

**Assets:** Sample dashboard image `dashboard-sample.png` (also pinned on the Mural board).

**🧩 Pattern watch:** Design pattern, **Honest defaults**: zero baselines, defined denominators, units on every axis. Anti-pattern, **Truncated-axis drama**: an 82 to 98 climb drawn to look like a rocket.

> ℹ️ **Good to know:** Florence Nightingale's 1858 rose diagram showed Parliament that most British soldiers in Crimea died of preventable disease, not battle wounds. Her chart is credited with driving sanitation reform in the army. Honest, readable charts carried life-and-death stakes then, and your critique defends the same trust now. (Source: [Encyclopaedia Britannica](https://www.britannica.com/biography/Florence-Nightingale))

## Run steps 🪜
1. Study the sample dashboard (`dashboard-sample.png`): bars climb from 82 in January to 98 in June, an impressive-looking rise.
2. Check the axes first: the y-axis starts at 80, not 0, so a 19% real improvement looks like a fivefold visual leap, your first red sticky candidate.
3. Hunt for what is missing: total requests received (the denominator), backlog, channel, geography, and any confidence interval, without these a "resolved" count cannot answer "are we keeping up?"
4. Challenge the definitions: what does "resolved" actually mean, closed ticket, satisfied citizen, or SLA met? If it is undefined, the trend is uninterpretable.
5. Post your three red stickies (misleading / missing / unclear) and one green sticky; the month-over-month trend itself is real signal worth keeping.
6. Vote on the worst issue (the sample's caption hints the answer: no denominator); remote learners post `worst issue: ___ | one fix: ___` in chat and reply to one vote they disagree with.

## Key takeaway 💡
Every dashboard is an argument: check the axis, the denominator, and the definition before you believe the trend.

## Study further 📚
- [What is data visualization?, IBM Think](https://www.ibm.com/think/topics/data-visualization), clear overview of how visual choices shape what an audience concludes.
- [Visualization best practices in Power BI, Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-best-practices), official design guidance on honest, readable charts.
- [Calling Bullshit, University of Washington](https://callingbullshit.org/), a university course on spotting misleading data claims, truncated axes, and missing denominators.

## Common mistake to name ⚠️
Critiquing colors and layout while the y-axis starts at 80 and "resolved" stays undefined; require at least one red sticky about scale, denominator, or definition before the vote.

## If finished early ⏩
Sketch the fix in one sentence: the chart that would honestly answer "are we resolving more requests than we receive?", what is on each axis, and what is the denominator?

## ⭐ Bonus (optional)
Redesign one panel: write the title, axis range, denominator, and definition for a replacement chart, and post it as a comment on the sticky that won the "worst issue" vote.

**Solution link in master guide:** `#answer-8-c`
