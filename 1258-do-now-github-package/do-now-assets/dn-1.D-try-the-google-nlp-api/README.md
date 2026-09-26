# Do Now 1.D: Try the Google NLP API 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, you only need a browser for the public demo page; observations are captured in Zoom chat (or on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240786066/9b138b3dc8eb259be5ecf9efb2745bf9ae88df5c

## Goal
Run real text through Google's hosted Natural Language demo and see what a managed ML service extracts, entities, sentiment, categories, and moderation flags, without training anything yourself. You walk away with one structured chat observation: the detection that surprised you and why.

**Assets:** Public demo at https://cloud.google.com/natural-language/ (see `board-items.tsv`).

## Run steps 🪜
1. Open https://cloud.google.com/natural-language/ in any browser and scroll to the live demo; no account or setup needed.
2. Run the sample text first and look at all the result tabs: entities, sentiment, syntax, and categories/moderation.
3. Paste a short invented paragraph of government-flavored text, a public press release snippet or a made-up citizen complaint; never real case data or personal information.
4. Compare what the service detected with what you expected: which entities did it find or miss, and did the sentiment score match your own reading?
5. Post one observation in Zoom chat using the capture template: `Surprised me: entities/sentiment/moderation/categories because ___`, one detection, one reason.
6. Find one chat observation that contradicts yours and reply with the type of text you used; keep a mental note that this API is the "buy" option you will compare against train-your-own in the NER lab.

## Key takeaway 💡
A managed NLP API turns unstructured text into entities, sentiment, categories, and moderation flags with zero training, knowing what it sees (and misses) is the baseline for every buy-vs-build decision an agency makes on language data.

## Study further 📚
- [Cloud Natural Language API, Google Cloud](https://cloud.google.com/natural-language/), the managed service you just tried, with its full feature list.
- [Analyzing entities, Google Cloud](https://cloud.google.com/natural-language/docs/analyzing-entities), how entity extraction works and what the API returns.
- [Analyzing sentiment, Google Cloud](https://cloud.google.com/natural-language/docs/analyzing-sentiment), how sentiment scores and magnitudes are computed.

## Common mistake to name ⚠️
Pasting real citizen data into a public demo "to see what happens", or reporting bare scores with no surprise attached; the demo is a third-party service, so invent your text and attach the judgment.

## If finished early ⏩
Run the same text twice with one word changed, a neutral word swapped for a charged one, and report in chat how much the sentiment or moderation output moved.

## ⭐ Bonus (optional)
Find one sentence where the API's entity or sentiment detection is flatly wrong, post the sentence type (not any sensitive content) with your verdict in chat, and name the class of government text, legal, medical, casework, where that error would matter most.

**Solution link in master guide:** `#answer-1-d`
