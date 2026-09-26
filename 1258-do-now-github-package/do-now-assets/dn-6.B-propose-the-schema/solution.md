# Sample / solution

## Why this approach works
Writing the schema before cleaning converts "clean the data" from a vibe into a testable contract: a date either parses as ISO or it does not, a ward is either an integer in range or it is not. The justification line forces each field to earn its place.

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

Each justification points at a concrete failure from 6.A; the coordinate ranges turn ROW7's latitude 999 from a silent map error into a rejected row. A good reply to a peer's schema: "add a rule for what happens when a row fails a constraint, reject, flag, or quarantine, because a constraint with no consequence is documentation, not enforcement."
