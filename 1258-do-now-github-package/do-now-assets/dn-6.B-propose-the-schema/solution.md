# Sample / solution

## Why this approach works
Writing the schema before cleaning works because it converts "clean the data" from a vibe into a testable contract. Every field carries a name, a type or constraint, and a one-line justification, so each cleaning step can be validated programmatically: a date either parses as ISO or it does not, a ward is either an integer in range or it is not. The weak version, a list of column names with no types, tells the next team nothing and lets every cleaner invent private rules; the justification line is what forces each field to earn its place. Doing it in chat, line by line, makes the reasoning visible and correctable before a single row is touched. The schema also becomes the bridge to the next activity: the cleaning prompt's rules section is this same contract restated as imperatives.

## A complete solution
Posted in chat, one line per field as `name: type, why needed`:

```
request_id: string, unique per request; deduplication key, catches the repeated 311-10485
created_date: ISO date YYYY-MM-DD; valid timeline, rejects 01/03/26 and the impossible 2026-13-03
issue_type: enum graffiti/pothole/noise/water/lights/garbage/snow/tree; consistent categories, folds "pothole" and "Pothole" into one group
ward: integer 1-10; valid geography, rejects blanks and out-of-range values
status: enum open/closed/pending; workflow state, rejects nonstandard values like "Closed?"
latitude: float, city-plausible range; mapping and geospatial joins, flags impossible values like 999
longitude: float, city-plausible range; pairs with latitude so a bad coordinate cannot slip through alone
```

Read the lines aloud and each justification points at a concrete failure from 6.A. The first five fields are the minimum viable core: identity, time, category, geography, state. The coordinate pair is the natural extension, and giving each a plausible numeric range is what turns ROW7's latitude 999 from a silent map error into a rejected row. A good reply to a peer's schema, per the run steps: "add a rule for what happens when a row fails a constraint, reject, flag, or quarantine, because a constraint with no consequence is documentation, not enforcement."
