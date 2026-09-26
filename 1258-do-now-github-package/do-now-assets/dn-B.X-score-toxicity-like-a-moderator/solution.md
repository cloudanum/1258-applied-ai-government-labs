# Sample / solution

## Why this approach works
Scoring against the 0–3 rubric instead of gut feel is what makes moderation consistent across reviewers: rude (1) is about tone, abusive (2) targets a person, threatening (3) implies harm. The escalation rule for the top score must survive disagreement, because the downside of missing a possible threat is a person's safety.

## A complete solution
The full placement, in the remote capture format: `P1=2, P2=1, P3=1, P4=3`. P1 "You are stupid" scores 2, a direct attack on a person, the definition of abusive on this rubric. P2 "This relationship sucks" scores 1, rude but aimed at a situation, not a person. P3 "You are acting like a jerk" scores 1, aimed at behavior rather than identity, though context and repetition could push it up. P4 "I know where you live" scores 3, threatening, with escalation.

P4 is the one to defend out loud. The wrong instinct is "no profanity, no insult, so 0 or 1," and that instinct is exactly why keyword moderation fails: the words are polite and the payload is menace. The phrase implies physical reach over the target, which is what 3 means on this rubric, and it gets escalated to a human or safety process even if it was meant as a joke, because joking intent cannot be verified from the text alone. The context comment to leave on the board: "P4 depends most on context, between close friends joking about carpooling it could be a 0, but from a stranger in a complaint thread it is a hard 3 with escalation; since the scorer cannot see the relationship, the safe default is 3 plus human review." P1 is the runner-up disagreement: among friends trading banter it can honestly drop to 1, but against an unknown target the default stays 2.
