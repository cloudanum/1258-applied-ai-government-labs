# Do Now 6.B: Propose the Schema 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured in Zoom chat (in-person learners can add their schema as Mural comments on the board).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240805042/a46802631aa3862869e69d7648b8dd0dabb41194

## Goal
By the end of this five-minute drafting sprint you will have proposed a minimum viable schema, five to eight fields, each with a name, a type or constraint, and a one-line justification, for the messy 311 data you triaged in activity 6.A, written *before* any cleaning begins. Your artifact is a short block of schema lines posted in chat, in the form `field: type, why needed`. The instinct this builds is contract-first thinking: a schema turns the vague instruction "clean the data" into an explicit, testable agreement, and writing the contract before touching the data is what separates a defensible pipeline from spreadsheet archaeology.

## Why it matters
Schema-first is a core data-engineering habit: agreeing on field names, types, and constraints up front converts a vague quality complaint into an executable checklist that every cleaning step can be tested against. Doing it in chat makes the reasoning visible and easy to correct line by line.

**Assets:** Sample rows from 6.A (see `board-items.tsv`).

**🌐 With Copilot in the browser:** Copilot is a decent schema-drafting partner: describe your 311-style rows and ask for field names, types, and justifications, then apply the same critique you used here.

## Run steps 🪜
1. Recall the messy rows from 6.A, mixed date formats like `01/03/26`, `Ward five` vs. `Ward 5`, duplicate request IDs, free-text statuses like `Closed?`.
2. Decide which five to eight fields a clean version of this dataset must carry; start from `request_id`, `created_date`, `issue_type`, `ward`, `status` and add anything you believe is missing (e.g. latitude and longitude as floats).
3. Give each field a type or constraint: string, ISO date, an enum of allowed values (`graffiti/pothole/noise/water/lights/garbage/snow/tree`), an integer range 1–10.
4. Add a one-line justification for every field, why does downstream work need it?
5. Post your schema in Zoom chat, one line per field, as `name: type, why needed`; in person, add the same lines as a Mural comment so they stay visible on the board.
6. Read one other learner's schema and reply with a single concrete improvement, a missing field, a tighter constraint, or a justification that doesn't hold up.

## Key takeaway 💡
Write the schema before you clean: an explicit field-name-type-justification contract turns vague data wrangling into testable rules, and it becomes the checklist every later fix is validated against.

## Study further 📚
- [JSON Schema, json-schema.org](https://json-schema.org/), the standard vocabulary for declaring field names, types, and constraints in machine-readable form.
- [Data Catalog Vocabulary (DCAT) Version 3, W3C](https://www.w3.org/TR/vocab-dcat-3/), the W3C standard governments use to describe datasets in catalogs like data.gov.
- [Data on the Web Best Practices, W3C](https://www.w3.org/TR/dwbp/), W3C guidance on publishing structured, well-described, well-typed data.

## Common mistake to name ⚠️
Proposing fields with no type or justification. A schema entry like `date` tells nobody anything, require every field to carry a type or constraint plus a one-line reason for existing, or it goes back for revision.

## If finished early ⏩
Add a constraint to one field that would catch a 6.A issue automatically, e.g. `created_date` must parse as a real calendar date (rejects `2026-13-03`), or `ward` must be an integer between 1 and 10.

## ⭐ Bonus (optional)
Extend your schema with the latitude/longitude pair: give each a type, a plausible numeric range for your city, and a rule for what happens when a row falls outside it, reject, flag, or quarantine?

**Solution link in master guide:** `#answer-6-b`
