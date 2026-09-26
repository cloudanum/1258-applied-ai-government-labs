# Sample / solution

## Why this approach works
Government data fails in boring, repeatable ways, and naming the violated dimension converts a vague "this looks off" into a category you can check systematically across millions of rows. The tag also tells you which validation rule would have caught the issue automatically.

## A complete solution
The full board, postable in chat, reads: `ROW2: consistency, 01/03/26 and "Ward five" (the blank status also fails completeness)`. `ROW3: validity, month 13 in 2026-13-03`. `ROW4: consistency, lowercase "pothole" splits the category`. `ROW5: uniqueness, request ID 311-10485 repeats ROW4`. `ROW6: completeness, ward is blank`. `ROW7: accuracy, latitude 999 is impossible`. `ROW8: validity, "Closed?" is not a standard status`. `ROW10: consistency, lowercase "ok"; plus validity, Ward 10 sits outside the expected range`. ROW1 and ROW9 are clean and take no tag.

A complete defense of ROW2 sounds like this: "The date 01/03/26 does not match the ISO format of the other rows, so a parser either rejects it or silently reads it as March 1 instead of January 3. 'Ward five' will not join to a ward lookup table or group with 'Ward 5,' so ward-level dashboards undercount Ward 5. And the blank status drops this request from any open-versus-closed report." That is three downstream breaks from one short row.

For the worst-offender star, ROW7 is the defensible pick: a missing ward announces itself, but latitude 999 is a confident, wrong value that passes a completeness check and drops a city request into the ocean on every map. ROW5 is the other strong candidate, since a duplicate ID double-counts demand for the same pothole; either pick earns the point if the one-sentence defense names what breaks.
