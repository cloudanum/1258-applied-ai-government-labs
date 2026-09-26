# Do Now 6.A: Six Dimensions on Ten Rows 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured directly on the Mural board (or in Zoom chat if you are remote).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240804045/16b2e2ffdea384025b2dc3d886d6bc5250b61336

## Goal
Scan a ten-row extract of 311 service-request data and tag every data-quality issue you find with the dimension it violates: accuracy, completeness, consistency, timeliness, validity, or uniqueness. You leave the board with a tag on every dirty row and a star on the worst offender, defended in one sentence.

**Assets:** Ten-row sample grid (`ten-rows.png`; row-by-row detail in `board-items.tsv`).

**🧩 Pattern watch:** Design pattern, **Quality dimensions checklist**: validity, uniqueness, completeness, consistency, timeliness, accuracy, checked per column. Anti-pattern, **Clean it later**: later never comes; downstream models learn the dirt.

> ℹ️ **Good to know:** The US Census Bureau publishes federal data quality guidelines built on dimensions like relevance, accuracy, timeliness, and accessibility. They are the professional version of the six tags you just applied to ten messy rows. Data quality was a formal government discipline long before AI made it fashionable. (Source: [US Census Bureau](https://www.census.gov/about/policies/quality/guidelines.html))

## Run steps 🪜
1. Open the Mural board linked above (or follow along in Zoom chat) and pull up the ten-row grid, `ten-rows.png`.
2. Scan ROW1–ROW10 column by column: are dates valid and consistently formatted, ward values in range, coordinates plausible, statuses standard, request IDs unique?
3. Tag each dirty row with the dimension it violates, e.g. ROW3's `2026-13-03` fails validity, ROW5's repeated `311-10485` fails uniqueness, ROW6's blank ward fails completeness, ROW7's latitude `999` fails accuracy. Remote? Post tags in Zoom chat, e.g. `ROW2: consistency, 01/03/26 and "Ward five"`.
4. Mark the single worst offender with a star or color tag and be ready to defend your pick in one sentence.
5. Compare your worst-row pick with a neighbor; where you disagree, each side gives a one-sentence argument.
6. Initial or color-tag your annotations before the instructor reveals the full issue list (see `board-items.tsv` for the key).

## Key takeaway 💡
Data-quality problems are patterned, not mysterious, six dimensions (accuracy, completeness, consistency, timeliness, validity, uniqueness) will catch almost everything wrong in a small government extract before it breaks a join, a dashboard, or a model.

## Study further 📚
- [What is data quality?, IBM Think](https://www.ibm.com/think/topics/data-quality), plain-language tour of the classic data-quality dimensions and why they matter.
- [Quality Guidelines, U.S. Census Bureau](https://www.census.gov/about/policies/quality/guidelines.html), how a federal statistical agency defines and enforces information quality.
- [Resources.data.gov, U.S. federal data playbook](https://resources.data.gov/), federal standards, tools, and playbooks for managing and publishing quality data.

## Common mistake to name ⚠️
Treating "Ward five" vs. "Ward 5" as cosmetic: inconsistent category labels break joins, filters, and dashboards just as surely as missing values do.

## If finished early ⏩
Write one validation rule for ward and one for status that would reject bad rows automatically, e.g. "ward must be an integer 1–10" and "status must be one of open/closed/pending."

**Solution link in master guide:** `#answer-6-a`
