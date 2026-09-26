# Sample / solution

## Why this approach works
No agency can mitigate all eight risks, so the two you fund first define your real security posture, and oversight will ask why you chose them. The grid forces the honest question, is it likely here and how bad here, while headline anxiety would fund cinematic attacks and leave prompt injection, which arrives with every submitted document, unfunded.

## A complete solution
One defensible board for a document-handling agency: R1 data poisoning at low-to-medium likelihood, high impact (likelihood hinges on who controls training data and labels); R2 evasion at medium likelihood, medium impact; R3 prompt injection at high likelihood, high impact; R4 model extraction at low likelihood, medium impact for an internal, rate-limited service; R5 membership inference at low-to-medium likelihood, high impact if sensitive records were in training data; R6 denial of service at medium likelihood, medium impact with quota and fallback in place; R7 insider misuse at high likelihood, high impact; R8 bias and fairness failure at medium-to-high likelihood, high impact.

Chat post: `FUND FIRST: R3, R7, because both pair high likelihood with high impact in our context: every submitted document reaches the prompt, so R3's likelihood is high and hijacked instructions make its impact high, and R7 needs no attacker at all, just one authorized user exporting data where changes are not logged.`

The tricky item is R1: ask the facilitator question before ranking. If labels come from audited case outcomes a vendor cannot touch, likelihood drops and R1 stays high-impact without making FUND FIRST; if a vendor labels data you never review, R1 jumps. Disagreement comment on a colleague who funded R1 and R4: "R4 assumes an attacker with a large query budget against a public endpoint; ours are rate-limited and monitored, so its likelihood sits below R7's, where misuse needs nothing but an account we already issued."
