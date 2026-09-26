# Sample / solution

## Why this approach works
A good observation names the gap between what you expected the service to notice and what it actually noticed, and that gap is where buy-vs-build judgment forms. "Sentiment was -0.3" is a fact; "our angriest sentence scored only mildly negative" is a finding a project team can act on.

## A complete solution
One complete run: paste an invented citizen complaint, "This is the third missed garbage pickup in a month on Willow Avenue. I have called twice and nobody is accountable. I want the collection schedule fixed and a supervisor to confirm it." The service correctly extracts "Willow Avenue" as a location entity, but the document sentiment comes back only mildly negative (roughly -0.3), because the polite, procedural wording smooths out the frustration any human reader would catch.

The chat post, following the capture template exactly:

`Surprised me: sentiment because the angriest complaint sentences scored only mildly negative, the polite procedural wording smoothed out the frustration, so a triage queue built on raw sentiment scores would under-prioritize exactly the residents about to escalate.`
