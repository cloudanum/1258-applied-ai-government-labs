# Sample / solution

## Why this approach works
The risk-guardrail-owner triple converts anxiety into a control: the risk is specific enough to design against, the guardrail has a mechanism and a checkpoint, and the named owner makes it auditable. "We will be careful" names no control, no checkpoint, and no person, so it survives no audit.

## A complete solution
The full chat post, in the capture format from the run steps:

`Risk: Wrong answer to a resident. | Guardrail: Grounding required plus human review before send. | Owner: Program owner + communications lead.`

The spoken defense: "My top risk is a wrong answer reaching a resident, because this use case touches the public. Grounding required means the model answers only from the approved permit status source, which removes most invention at the cause. Human review before send is the checkpoint that catches what grounding misses. The owner pair is deliberate: the program owner keeps the source data current, and the communications lead makes sure the review step actually happens before anything goes out." If a peer posts `Risk: bias | Guardrail: we will monitor | Owner: IT`, the one-line fix is "monitoring is not a control, name the checkpoint and the test, e.g. a monthly sample of twenty drafted answers scored for tone and accuracy, owned by the program lead." The bonus monthly test for the worked example: spot-check ten drafted responses for grounding and citation.
