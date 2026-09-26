# Sample / solution

## Why this approach works
An AI assistant is a discovery engine, not an authority: it routinely produces plausible URLs that 404, so the three checks are what turn a lead into a source you can defend. The `VERIFIED: <url>` format makes the habit auditable, since anyone can reopen the link and re-run the same checks.

## A complete solution
A sample run on the topic "county-level air quality." Ask the approved assistant: "Find two public datasets about county-level air quality and give me the exact source URLs." Suppose it returns two links. The first lands on the agency's generic homepage rather than the promised dataset page, so it fails the second check and gets discarded. The second lands on EPA's AirData portal: real downloadable daily and annual county-level files, documentation, and recent update dates, so it passes all three checks.

The posted artifact is a single chat line:

`VERIFIED: https://www.epa.gov/outdoor-air-quality-data (EPA AirData: county-level air quality data, daily and annual summaries, downloadable CSVs, page current)`

That line is complete because a classmate can act on it: open the same URL, confirm it loads, confirm it is a dataset page, and confirm freshness. The assistant was confident about both links; only one survived being opened.
