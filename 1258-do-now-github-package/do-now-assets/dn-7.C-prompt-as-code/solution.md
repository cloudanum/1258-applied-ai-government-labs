# Sample / solution

## Why this approach works
The header converts a prompt from loose text into an artifact under change management: an edit stops being invisible and becomes a deployment you can review, test, and roll back. The test case does the real work, because without an expected output to compare against, prompt drift stays silent.

## A complete solution
Take prompt P1: "Summarize this citizen email for the duty officer." Wrapped in the minimum header: name: citizen-email-summarizer; version: v1.0; owner: the 311 service analytics team lead; purpose: turn a raw citizen email into a three-sentence brief for the duty officer; inputs: one field, email_text, the raw message with PII left in place; output schema: JSON with exactly three keys, summary (string, at most three sentences), category (one of benefits, permits, complaint, other), urgency (one of low, medium, high); rollback note: if any regression test fails after an edit, restore v1.0 from the shared prompt library, trigger is a failed test in weekly production sampling.

The test case: input a sample email appealing a denied benefit, and require category "benefits," the urgency key present, and a summary of three sentences or fewer. If an edit drops the urgency instruction, the JSON arrives without that key and the test fails before the edit ships; if summaries sprawl to five sentences, the length check fails.

Posted in chat: "citizen-email-summarizer/v1.0 | input: email_text (raw citizen email), output JSON {summary ≤ 3 sentences, category: benefits/permits/complaint/other, urgency: low/medium/high} | test: a benefit-appeal email must return category benefits with urgency present; the test fails if an edit drops the urgency field." When replying to colleagues, the most common missing field is the rollback note, which is what turns the header from documentation into change control.
