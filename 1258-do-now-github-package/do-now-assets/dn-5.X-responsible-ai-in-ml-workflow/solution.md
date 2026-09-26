# Sample / solution

## Why this approach works
The mapping works because it distributes responsibility across the lifecycle instead of parking it at the end. Privacy and representativeness are decided in define and prepare, before any model exists, so a review that starts at evaluate inherits whatever the data already baked in. Giving every practice a named owner is the second half of the discipline: an unowned practice is a practice that quietly gets skipped, and frameworks like the NIST AI RMF and GAO's accountability framework ask agencies to demonstrate exactly this stage-practice-owner mapping. The weak version of this exercise puts every sticky under evaluate or deploy; that is the anti-pattern the activity is designed to expose. Flagging the stage where your own agency names no owner turns a classroom grid into a finding you can act on.

## A complete solution
A complete board, posted in chat in the template `step -> practice -> owner`, reads:

- `define -> documented purpose and affected-groups impact assessment -> program executive`
- `prepare -> de-identification and representative sampling -> data steward`
- `build -> versioned training data and documented model choices -> ML engineering lead`
- `evaluate -> fairness and explainability review -> model risk lead`
- `deploy -> human-oversight sign-off and a monitoring plan -> system owner`

Read the lines aloud and each one survives scrutiny. Define gets the impact question because deciding whether, and for whom, the system should exist is a policy call rather than a technical one, and only an executive can own it. Prepare gets de-identification and representative sampling because those are data decisions and the data steward controls the data. Build gets versioning and documentation because reproducibility is created, or lost, at build time. Evaluate carries the fairness and explainability review under the model risk lead, the pairing most learners find intuitive. Deploy carries human-oversight sign-off, because launch is the last point where a person can still say no cheaply.

The stage most often flagged as ownerless is define: projects arrive already approved, so nobody owns the question of whether the system should exist at all. The flag comment reads: "define has no owner in practice; the accountable program executive should own the purpose-and-impact sign-off before funding is released." Note what the grid deliberately avoids: all five practices did not land on evaluate and deploy, because responsible AI lives inside the workflow, not after it.
