# Sample / solution

## Why this approach works
Drawing the flow is the audit: prose lets an undefined rule hide inside a word like "sensitive," while boxes and arrows force every branch into the open. The real deliverable is the marked gap, because P1 never defines the rule an automated system would need.

## A complete solution
The rebuilt flow, three boxes plus one decision, matching the starter in `process-flow-start.png`:

`Intake -> Classify -> Sensitive? -> (yes) Human review / (no) Respond -> missing rule: what counts as sensitive`

That line is also the complete Zoom chat fallback post. On the Mural board the same flow is one box per step (Intake, Classify, Respond), a decision diamond labeled "Sensitive?" after Classify, and two labeled branches, "yes -> Human review" and "no -> Respond." Nothing is added that P1 does not state, and nothing P1 states is dropped.

The finding goes on a contrasting sticky or comment: "P1 never defines the rule that decides Sensitive? Without it, two reviewers will route the same inquiry differently, and no AI system can automate this branch until the rule exists." If you finish early, propose the rule yourself, for example "sensitive = contains personal identifiers or case details," and mark Human review as the box a person must always own. In the neighbor comparison, a decision placed before Classify instead of after is not a drawing error; it is a different assumption about the process, and surfacing it is the point.
