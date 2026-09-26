# Sample / solution

## Why this approach works
"High-impact" under OMB M-25-21 describes consequences for people, not the sophistication of the technology, and the label is the gate that triggers impact assessment, testing, and human oversight. The screening question is deliberately crude so the gate actually gets applied to the small use cases that quietly need it.

## A complete solution
Full screen: YES gets H1 (housing-benefits eligibility: touches rights and benefits) and H3 (child-welfare hotline triage: safety and rights, a human must decide). NO gets H2 (internal meeting-notes summarizer: no decisions automated from it) and H6 (code-comment autocomplete: low rights impact). MAYBE gets H4 (public FAQ drafter: content risk, not high-impact by itself) and H5 (fire-safety inspection flagging: resource allocation with a safety effect). Chat post: `YES: H1, H3 | NO: H2, H6 | MAYBE: H4, H5`, with the trigger sentence `H1: Yes, affects rights/benefits; needs strong review`.

H5 is the sticky worth arguing: it looks internal, but if the model ranks a dangerous building low, the safety effect lands on occupants, so it is a Maybe leaning Yes, flipping fully if the flags determine inspection order. H4 flips to Yes the day the FAQ answers benefit-eligibility questions. My edge-case comment on the board: "H2 flips to high-impact if summaries feed a personnel decision."
