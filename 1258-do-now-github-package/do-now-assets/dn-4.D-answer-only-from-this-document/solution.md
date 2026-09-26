# Sample / solution

## Why this approach works
Grounding is only proven by the question the excerpt cannot answer: any model looks faithful on text it covers, so the test is whether it says "not stated" when the text is silent. The rule gives the model an explicit escape hatch and gives the reviewer an audit trail, since the quoted sentence shows what the answer rests on.

## A complete solution
The remote capture, posted as one Zoom chat message: `Answerable: How long are records retained? | Unanswerable: What is the retention rule for police body-worn video? | Rule: Answer only from the text; if not stated, say "not stated" and quote the sentence used.`

The answerable question earns its name because the excerpt states it directly: "Records are retained for seven years unless a litigation hold is active." The unanswerable one is what a real resident or police services board would ask, and the excerpt never mentions it, so the only grounded response is: "Not stated. The excerpt says records are retained for seven years unless a litigation hold is active, but it does not address body-worn video." Without the rule, the model would borrow from general knowledge and answer with confident invented detail, a retention period nobody in this agency ever approved.

Watch the sneaky version too: "Does the seven-year rule apply to email?" feels almost answered, but the excerpt says "records," not email, so the defensible grounded answer is still "not stated," with the seven-year sentence quoted as the closest relevant text.
