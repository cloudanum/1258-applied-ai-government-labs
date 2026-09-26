# Sample / solution

## Why this approach works
The exercise is calibrated surprise, so a good observation names what you expected the service to notice and what it actually noticed. That gap is where buy-vs-build judgment forms: an agency that knows a managed API already extracts entities and sentiment from its text can buy that capability instead of building it, and an agency that knows where the API is blind knows what it would still have to build itself. Reporting a bare score with no surprise attached skips the judgment entirely; "sentiment was -0.3" is a fact, while "our angriest sentence scored only mildly negative" is a finding a project team can act on. The second discipline is the invented text: the demo is a third-party service, so real case data never goes in, and practicing that habit on a harmless warm-up is the point. Twenty learners pasting different texts produce a crowdsourced map of the service's blind spots faster than any documentation page.

## A complete solution
One complete run: paste an invented citizen complaint, "This is the third missed garbage pickup in a month on Willow Avenue. I have called twice and nobody is accountable. I want the collection schedule fixed and a supervisor to confirm it." The service correctly extracts "Willow Avenue" as a location entity, but the document sentiment comes back only mildly negative (roughly -0.3), because the polite, procedural wording ("I want the schedule fixed and a supervisor to confirm it") smooths out the frustration any human reader would catch immediately.

The chat post, following the capture template exactly:

`Surprised me: sentiment because the angriest complaint sentences scored only mildly negative, the polite procedural wording smoothed out the frustration, so a triage queue built on raw sentiment scores would under-prioritize exactly the residents about to escalate.`

That observation names the detection, the reason, and the consequence for a real government use case, which is what separates a finding from a score report. Keep the mental note the README asks for: this API is the "buy" option you will compare against train-your-own in the NER lab.
