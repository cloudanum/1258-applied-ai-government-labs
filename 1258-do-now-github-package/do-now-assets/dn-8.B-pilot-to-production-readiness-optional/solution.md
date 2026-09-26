# Sample / solution

## Why this approach works
Scoring against evidence, not effort, is what makes the checklist defensible: a 2 means you could hand an auditor the artifact today, and a plan to build monitoring is honestly a 1. The score's only value is forcing each gap to carry a next action and a named owner before production is discussed.

## A complete solution
A strict sample scoring, for a pilot chat assistant answering citizen questions about benefit programs: monitoring scores 1 (a dashboard exists but no weekly drift report with a named owner); evaluation scores 1 (demoed on twenty hand-picked questions but never scored against a versioned answer key); escalation path scores 0 (nothing documents who a citizen contacts after a wrong answer or who can take the assistant offline); cost controls score 2 (a monthly token budget with alerts is live in the finance system and could be shown to an auditor today); human review scores 1 (informal spot-checks with no sampling plan or log).

The lowest item is the escalation path at 0, also the one that would hurt most in public if it failed on day one. The gap sticky reads: "lowest item: escalation path (scored 0, no documented route for a citizen who gets a wrong answer) | next action: publish a one-page escalation SOP naming who can take the assistant offline and how a citizen reaches a human, then tabletop-test it once before launch | owner: the service delivery manager for the benefits portal."

Two defenses for the debrief. Monitoring at 1, not 2: the dashboard's existence is effort, and the bar for a 2 is a running weekly drift report with a named owner. Cost controls at 2, not 1: the budget and alerts are live and inspectable, which is the auditor-artifact standard. If a neighbor's lowest item is monitoring instead, that is a finding, not a mistake; compare what evidence each score rested on.
