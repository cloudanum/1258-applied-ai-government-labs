# Sample / solution

## Why this approach works
A monitoring plan only catches what it measures, and a single global accuracy score stays green while fairness gaps, silent drift, doubling latency, and tripled token bills go uncounted. Three of the eight stickies, M4, M6, and M8, fit none of the five supplied columns, and recognizing that the dashboard itself is incomplete is part of the lesson, not a placement error.

## A complete solution
The full placement: M1 to fairness (a language-slice metric, English versus French, because a global score averages the gap away); M2 to latency (p95 doubling after launch is an operational regression); M3 to drift (week-to-week answer changes after a model update); M4 to false-refusal rate, outside the five columns; M5 to cost (cost per request or a token budget metric); M6 to groundedness/citation coverage, outside the five columns; M7 to fairness (a geographic slice metric); M8 to faithfulness, outside the five columns.

M6 shows the matching logic: the answers are correct, so accuracy never trips, but the failure is compliance with the sourcing rule, and only citation coverage, the percent of published answers carrying a valid citation to an approved source, can see it. M8 follows the same logic: retrieval returned the right document, but the paraphrase is not supported by it, and a faithfulness metric, does every claim trace to the retrieved text, catches the class without needing a labeled answer key in production.

The remote chat post reads: "M1-fairness, M2-latency, M3-drift, M4-false-refusal rate, M5-cost, M6-groundedness, M7-fairness, M8-faithfulness. Missing metric on our dashboard: cost per request (monthly token spend divided by requests served); we track uptime and a global satisfaction score, so a 3x token bill at flat usage would reach us only through the finance office." If a neighbor insists M1 is an accuracy problem, the defense is the mechanism: a global accuracy number can hold steady while the French slice fails, so only a per-slice fairness metric catches it first.
