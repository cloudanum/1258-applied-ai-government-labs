# Sample / solution

## Why this approach works
The mapping distributes responsibility across the lifecycle instead of parking it at the end: privacy and representativeness are decided in define and prepare, before any model exists. Giving every practice a named owner matters because an unowned practice is one that quietly gets skipped.

## A complete solution
A complete board, posted in chat in the template `step -> practice -> owner`, reads:

- `define -> documented purpose and affected-groups impact assessment -> program executive`
- `prepare -> de-identification and representative sampling -> data steward`
- `build -> versioned training data and documented model choices -> ML engineering lead`
- `evaluate -> fairness and explainability review -> model risk lead`
- `deploy -> human-oversight sign-off and a monitoring plan -> system owner`

Define gets the impact question because deciding whether, and for whom, the system should exist is a policy call only an executive can own. Prepare gets data decisions because the data steward controls the data. Build gets versioning and documentation because reproducibility is created, or lost, at build time. Deploy carries human-oversight sign-off because launch is the last point where a person can still say no cheaply.

The stage most often flagged as ownerless is define: projects arrive already approved, so nobody owns the question of whether the system should exist at all. The flag comment reads: "define has no owner in practice; the accountable program executive should own the purpose-and-impact sign-off before funding is released."
