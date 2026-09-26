# Sample / solution

## Why this approach works
The risk-guardrail-owner triple works because it converts anxiety into a control. "Wrong answer to a resident" is a risk you can point at, unlike "the AI might mess up," so you can actually design against it. "Grounding required plus human review before send" is a guardrail with a mechanism and a checkpoint: grounding attacks the cause, invention, and review attacks the consequence, a wrong answer leaving the building. "Program owner + communications lead" names the humans accountable, which is what makes the control auditable; a guardrail without an owner is a wish. The weaker instinct, "we will be careful" or "we will review regularly," survives no audit because it names no control, no checkpoint, and no person. The Air Canada tribunal case sits underneath the whole exercise: the organization owns what its AI says, so an unowned guardrail is not a position, it is the absence of one.

## A complete solution
The full chat post, in the capture format from the run steps:

`Risk: Wrong answer to a resident. | Guardrail: Grounding required plus human review before send. | Owner: Program owner + communications lead.`

The spoken defense: "My top risk is a wrong answer reaching a resident, because this use case touches the public. Grounding required means the model answers only from the approved permit status source, which removes most invention at the cause. Human review before send is the checkpoint that catches what grounding misses. The owner pair is deliberate: the program owner keeps the source data current, and the communications lead makes sure the review step actually happens before anything goes out." The step-6 review skill is part of the lesson: if a peer posts `Risk: bias | Guardrail: we will monitor | Owner: IT`, the one-line fix is "monitoring is not a control, name the checkpoint and the test, e.g. a monthly sample of twenty drafted answers scored for tone and accuracy, owned by the program lead." The bonus monthly test for the worked example: spot-check ten drafted responses for grounding and citation.
