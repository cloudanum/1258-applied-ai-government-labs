# Sample / solution

## Why this approach works
The contract-first prompt works because an LLM cleans data exactly as well as the instructions you write for it. Explicit imperative rules, one per column, remove the model's freedom to improvise, and a fixed output schema makes the result checkable by code: the JSON either has the keys rows, flags, and removed_duplicate_ids or it fails validation before a human even looks. The weak version, "please clean this data," returns confident prose or silently mutated rows with no record of what changed and no way to audit it. The flags array is the honest part of the contract: it forces the model to surface rows it cannot fix instead of guessing, which is the difference between assistance and fabrication. Writing the prompt in chat, where peers poke holes in it, rehearses the review habit you want around any LLM output in an agency pipeline.

## A complete solution
A complete cleaning prompt, posted in chat with the rules section and the output contract clearly separated, reads:

```
You are cleaning ten rows of 311 service-request data. Apply these rules exactly; do not invent values.

Rules:
1. Convert created_date to ISO YYYY-MM-DD. Interpret 01/03/26 as 2026-01-03. Flag impossible dates such as 2026-13-03; do not guess a correction.
2. If request_id repeats, keep the most complete row, remove the others, and list their IDs in removed_duplicate_ids.
3. Normalize issue_type to the lowercase enum: graffiti, pothole, noise, water, lights, garbage, snow, tree. Flag any value outside the enum.
4. Normalize ward to an integer 1-10, converting words ("Ward five" becomes 5). Flag blanks and out-of-range values.
5. Normalize status to the lowercase enum: open, closed, pending. Map "OK"/"ok" to open; flag nonstandard values like "Closed?" rather than guessing.
6. Validate latitude and longitude as floats in a plausible city range (latitude 45.0-46.0, longitude -76.0 to -75.0). Flag impossible values such as latitude 999.
7. Never guess a value you cannot derive from the row. Put the row in flags with the reason instead.

Output contract:
Return JSON with keys: rows (the cleaned rows), flags (array of {row_id, field, issue} entries, one per flagged value), removed_duplicate_ids (array of removed request IDs). No prose outside the JSON.
```

Two details carry the weight. Rule 7 is the anti-fabrication clause: without it, the model will happily invent a ward for ROW6 rather than admit the blank, and invented government data is worse than missing government data. The flags schema, `{row_id, field, issue}`, is what makes the output auditable: a reviewer can verify every change by diffing rows against flags, and the pipeline can reject the whole response if a key is missing. The first thing that goes wrong in a weaker prompt is almost always the same, an unspecified failure mode, so the model guesses where it should have flagged.
