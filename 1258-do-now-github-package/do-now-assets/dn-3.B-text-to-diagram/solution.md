# Sample / solution

## Why this approach works
Drawing the flow is the audit: prose lets an undefined rule hide inside a single word like "sensitive," while boxes and arrows force every step and every branch into the open. Labeling both exits of the decision is non-negotiable on a government process, because an unlabeled arrow is where unexamined assumptions live. The real deliverable is not the diagram but the marked gap: process text P1 never defines what counts as sensitive, and that missing rule is exactly what would get automated wrong if the flow were handed to a system as-is. The weaker instinct, transcribing the text into neat boxes and stopping, produces a pretty picture of an undefined process, and an AI-drafted diagram adds a second risk on top: steps the model silently invented that nobody diffed against the source.

## A complete solution
The rebuilt flow, three boxes plus one decision, matching the starter in `process-flow-start.png`:

`Intake -> Classify -> Sensitive? -> (yes) Human review / (no) Respond -> missing rule: what counts as sensitive`

That single line is also the complete Zoom chat fallback post. On the Mural board the same flow is one box per step (Intake, Classify, Respond), a decision diamond labeled "Sensitive?" placed after Classify, and two labeled branches: "yes -> Human review" and "no -> Respond," with Human review then closing the case. Nothing is added that P1 does not state, and nothing P1 states is dropped.

The finding goes on a contrasting sticky or comment: "P1 never defines the rule that decides Sensitive? Without it, two reviewers will route the same inquiry differently, and no AI system can automate this branch until the rule exists." That comment is the artifact that matters, because it is the one thing the prose was hiding. If you finish early, propose the rule yourself, for example "sensitive = contains personal identifiers or case details," and mark Human review as the box a person must always own. When comparing with a neighbor, a decision placed before Classify instead of after is not a drawing error; it is a different assumption about the process, and surfacing it before the answer reveal is the point of the exercise.
