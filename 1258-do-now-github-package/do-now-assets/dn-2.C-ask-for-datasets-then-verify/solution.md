# Sample / solution

## Why this approach works
The artifact is one verified link, not a list of suggestions, because an AI assistant is a discovery engine, not an authority. Language models routinely produce plausible-looking URLs that 404 or redirect to a generic homepage, so the three checks (the page loads, it is actually a dataset or metadata page, it is current) are what turn a lead into a source you can defend in front of others. Posting in the `VERIFIED: <url>` format makes the habit auditable: anyone in the room can reopen the link and re-run the same three checks, which is exactly what step 6 asks a classmate to do. The weaker instinct, reposting the assistant's confident list with zero links opened, does not avoid the hallucination risk, it exports the risk to everyone who trusts you.

## A complete solution
A sample run on the topic "county-level air quality." Ask the approved assistant: "Find two public datasets about county-level air quality and give me the exact source URLs." Suppose it returns two links. Opening the first lands on the agency's generic homepage rather than the promised dataset page, so it fails the second check and gets discarded; naming that failure out loud is part of the exercise, not an embarrassment. Opening the second lands on EPA's AirData portal: real downloadable daily and annual county-level air quality files, documentation, and recent update dates, so it passes all three checks.

The posted artifact is a single chat line:

`VERIFIED: https://www.epa.gov/outdoor-air-quality-data (EPA AirData: county-level air quality data, daily and annual summaries, downloadable CSVs, page current)`

That line is complete because a classmate can act on it: open the same URL, confirm it loads, confirm it is a dataset page rather than a brochure, and confirm freshness, then reply with what they found. One opened link beats three suggested links every time, and the discarded first suggestion is the lesson: the assistant was confident about both.
