# Sample / solution

## Why this approach works
The verdict format works because it makes the evidence do the talking: SUPPORTED only exists with a URL and a date attached, and anything less is UNSUPPORTED no matter how often the claim has been repeated. The discipline is going to the primary source: for a savings or performance claim, that is the evaluation report with its baseline period, and a press release repeating the number is the claim restating itself, not evidence. For a dataset claim, the description page is marketing; the data dictionary, sample rows, and suppression notes are the evidence. The weaker instinct, accepting a confident-sounding citation nobody opened, is the Mata v. Avianca failure: an AI citation is a lead, not a source. In government work an unsourced claim you repeat becomes your claim, which is why the verdict travels with its evidence or not at all.

## A complete solution
Claim 1, "Agency X reduced wait times by 40% using AI." Restated as a checkable statement: there must be an evaluation or report naming the 40% figure, the before-and-after period, and what "wait time" actually measured. The search turns up a conference slide deck and a trade-press article, both repeating "40%" and both pointing back to the agency's own announcement, but no evaluation report and no baseline period anywhere. Verdict for chat:

`UNSUPPORTED, no evaluation report and no baseline period found; only secondary articles repeating the number back to the agency's own announcement.`

Claim 2, "This dataset contains no personal information." The description page says "fully de-identified," but the data dictionary lists date of birth, postal code, and a free-text notes field, and there are no suppression or de-identification notes explaining how those fields were treated. Verdict:

`UNSUPPORTED, data dictionary lists date of birth, postal code, and a free-text notes field; no suppression or de-identification notes, so the claim cannot stand as written.`

Both verdicts follow the rule that makes the format useful: one reason, and for SUPPORTED one source and one date. Note the asymmetry the exercise teaches: an honest UNSUPPORTED is cheap to post, while SUPPORTED has to be earned with a URL you actually opened, and that asymmetry is the correct default whenever the evidence is thin.
